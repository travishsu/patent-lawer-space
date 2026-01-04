#!/usr/bin/env python3
"""
Patent Tools MCP Server

Exposes patent analysis tools through the Model Context Protocol (MCP).
Provides three main tools:
1. analyze_patent_word_count - Word count analysis for patent documents
2. analyze_patent_claims - Claims structure and antecedent basis analysis
3. generate_prior_art_search - Prior art search query generation
"""

import sys
import re
from pathlib import Path
from collections import defaultdict, Counter
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


# Import the analysis functions from the tools directory
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "tools"))


def count_words(text: str) -> int:
    """Count words in text, excluding markdown formatting."""
    # Remove markdown headers
    text = re.sub(r'#+\s+', '', text)
    # Remove markdown links but keep the text
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove markdown bold/italic
    text = re.sub(r'\*\*([^\*]+)\*\*', r'\1', text)
    text = re.sub(r'\*([^\*]+)\*', r'\1', text)
    # Remove code blocks
    text = re.sub(r'```[^`]*```', '', text, flags=re.DOTALL)
    text = re.sub(r'`[^`]+`', '', text)
    # Split on whitespace and count
    words = text.split()
    return len(words)


def analyze_word_count(content: str, file_name: str = "") -> dict[str, Any]:
    """Analyze word count in a patent document."""
    total_words = count_words(content)

    result = {
        "total_words": total_words,
        "file_name": file_name,
        "sections_found": {},
        "abstract_check": None
    }

    # Check if it's an abstract
    if 'abstract' in file_name.lower() or re.search(r'##\s+ABSTRACT', content, re.IGNORECASE):
        max_words = 150
        result["abstract_check"] = {
            "max_allowed": max_words,
            "current_count": total_words,
            "within_limit": total_words <= max_words,
            "remaining": max_words - total_words if total_words <= max_words else None,
            "exceeds_by": total_words - max_words if total_words > max_words else None
        }

    # Check for sections
    sections = {
        'Background': r'##\s+BACKGROUND',
        'Summary': r'##\s+.*SUMMARY',
        'Description': r'##\s+.*DESCRIPTION',
        'Claims': r'##\s+CLAIMS',
        'Abstract': r'##\s+ABSTRACT'
    }

    for section_name, pattern in sections.items():
        result["sections_found"][section_name] = bool(re.search(pattern, content, re.IGNORECASE))

    return result


def extract_claims(content: str) -> dict[int, str]:
    """Extract individual claims from the document."""
    claims = {}
    # Match claim numbers and their content
    pattern = r'\*\*Claim\s+(\d+)\.\*\*\s+(.*?)(?=\*\*Claim\s+\d+\.\*\*|$)'
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        claim_num = int(match.group(1))
        claim_text = match.group(2).strip()
        claims[claim_num] = claim_text

    return claims


def analyze_antecedent_basis(claim_text: str) -> list[str]:
    """Check for antecedent basis issues."""
    issues = []

    # Find all uses of "the" followed by a noun
    the_pattern = r'\bthe\s+([a-z]+(?:\s+[a-z]+)?)'
    the_matches = re.finditer(the_pattern, claim_text, re.IGNORECASE)

    for match in the_matches:
        element = match.group(1)
        # Check if "a" or "an" appears before this element
        a_pattern = r'\b(?:a|an)\s+' + re.escape(element)
        if not re.search(a_pattern, claim_text, re.IGNORECASE):
            issues.append(f"Possible antecedent basis issue: 'the {element}' without prior 'a/an {element}'")

    return issues


def analyze_claim_structure(claim_num: int, claim_text: str) -> dict[str, Any]:
    """Analyze claim structure and formatting."""
    issues = []
    warnings = []
    suggestions = []

    # Check for preamble
    if not re.match(r'^A\s+\w+|^The\s+\w+|^\d+\.', claim_text):
        issues.append("Missing or unclear preamble")

    # Check for transition phrase
    has_transition = False
    transition_type = None
    if 'comprising' in claim_text.lower():
        has_transition = True
        transition_type = "comprising (open-ended)"
    elif 'consisting of' in claim_text.lower():
        has_transition = True
        transition_type = "consisting of (closed)"
    elif 'consisting essentially of' in claim_text.lower():
        has_transition = True
        transition_type = "consisting essentially of (partially closed)"

    if not has_transition:
        warnings.append("No clear transition phrase (comprising, consisting of, etc.)")

    # Check claim length
    word_count = len(claim_text.split())
    if word_count > 200:
        warnings.append(f"Very long ({word_count} words) - consider simplifying")

    # Check for unclear antecedents
    if claim_text.count('said') > 0:
        suggestions.append("Consider replacing 'said' with 'the' for clarity")

    return {
        "issues": issues,
        "warnings": warnings,
        "suggestions": suggestions,
        "word_count": word_count,
        "transition_type": transition_type
    }


def check_claim_dependencies(claims: dict[int, str]) -> tuple[list[int], dict[int, list[int]]]:
    """Check claim dependency tree."""
    independent_claims = []
    dependent_claims = defaultdict(list)

    for claim_num, claim_text in claims.items():
        # Check if claim depends on another
        dep_match = re.search(r'claim\s+(\d+)', claim_text, re.IGNORECASE)
        if dep_match:
            depends_on = int(dep_match.group(1))
            dependent_claims[depends_on].append(claim_num)
        else:
            independent_claims.append(claim_num)

    return independent_claims, dict(dependent_claims)


def analyze_claims(content: str) -> dict[str, Any]:
    """Analyze patent claims for structure, antecedent basis, and dependencies."""
    claims = extract_claims(content)

    if not claims:
        return {
            "error": "No claims found in document",
            "claims_count": 0
        }

    independent, dependent = check_claim_dependencies(claims)

    result = {
        "total_claims": len(claims),
        "independent_claims": independent,
        "independent_count": len(independent),
        "dependent_count": len(claims) - len(independent),
        "claim_analysis": {}
    }

    for claim_num in sorted(claims.keys()):
        claim_text = claims[claim_num]

        # Determine claim type
        claim_type = "independent"
        depends_on = None
        if claim_num not in independent:
            dep_match = re.search(r'claim\s+(\d+)', claim_text, re.IGNORECASE)
            if dep_match:
                claim_type = "dependent"
                depends_on = int(dep_match.group(1))

        # Analyze structure
        structure = analyze_claim_structure(claim_num, claim_text)

        # Check antecedent basis
        antecedent_issues = analyze_antecedent_basis(claim_text)

        result["claim_analysis"][claim_num] = {
            "type": claim_type,
            "depends_on": depends_on,
            "word_count": structure["word_count"],
            "transition_type": structure["transition_type"],
            "structure_issues": structure["issues"],
            "warnings": structure["warnings"],
            "suggestions": structure["suggestions"],
            "antecedent_issues": antecedent_issues
        }

    return result


def extract_keywords(text: str) -> list[str]:
    """Extract potential keywords from text."""
    common_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'be',
        'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
        'would', 'should', 'could', 'may', 'might', 'can', 'this', 'that',
        'these', 'those', 'it', 'its', 'which', 'what', 'who', 'when', 'where',
        'why', 'how', 'said', 'such', 'other', 'also', 'into', 'through'
    }

    # Extract words (2+ characters, alphabetic)
    words = re.findall(r'\b[a-z]{2,}\b', text.lower())

    # Filter out common words
    keywords = [w for w in words if w not in common_words]

    return keywords


def extract_technical_terms(text: str) -> list[str]:
    """Extract multi-word technical terms."""
    technical_terms = set()

    tech_patterns = [
        r'\b\w+-\w+(?:-\w+)?\b',  # hyphenated terms
        r'\b(?:neural|machine|deep|artificial)\s+(?:network|learning|intelligence)\b',
        r'\b(?:data|image|signal|video)\s+(?:processing|compression|analysis)\b',
        r'\b(?:user|graphical)\s+interface\b',
        r'\b(?:computer|processor|memory|storage)\s+\w+\b',
    ]

    for pattern in tech_patterns:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for match in matches:
            technical_terms.add(match.group(0))

    return sorted(technical_terms)


def generate_boolean_queries(keywords: list[str], max_keywords: int = 5) -> list[str]:
    """Generate Boolean search queries."""
    queries = []

    keyword_freq = Counter(keywords)
    top_keywords = [k for k, v in keyword_freq.most_common(max_keywords)]

    if len(top_keywords) >= 2:
        # AND query with top keywords
        queries.append(" AND ".join(top_keywords))

        # OR variations
        queries.append(" OR ".join(top_keywords[:3]))

        # Mixed queries
        if len(top_keywords) >= 3:
            queries.append(f"{top_keywords[0]} AND ({top_keywords[1]} OR {top_keywords[2]})")

    return queries


def suggest_cpc_classifications(text: str) -> list[dict[str, str]]:
    """Suggest potential CPC classifications based on text content."""
    cpc_keywords = {
        'G06F': ['computer', 'data processing', 'computing', 'processor', 'software'],
        'G06N': ['artificial intelligence', 'machine learning', 'neural network', 'AI'],
        'G06T': ['image processing', 'graphics', 'visualization', 'rendering'],
        'G06Q': ['business', 'commerce', 'management', 'financial', 'payment'],
        'H04L': ['communication', 'network', 'transmission', 'protocol', 'data transfer'],
        'H04N': ['video', 'television', 'streaming', 'broadcasting'],
        'H04W': ['wireless', 'mobile', 'cellular', 'radio'],
        'A61B': ['medical', 'diagnostic', 'healthcare', 'patient', 'clinical'],
        'G01N': ['measuring', 'testing', 'analysis', 'detection', 'sensor'],
        'G05B': ['control', 'automation', 'regulating', 'feedback'],
        'G16H': ['healthcare IT', 'medical records', 'health informatics'],
        'B60W': ['vehicle', 'automotive', 'driving', 'autonomous'],
        'E21B': ['drilling', 'mining', 'extraction', 'well'],
    }

    text_lower = text.lower()
    suggested = []

    for cpc, keywords in cpc_keywords.items():
        for keyword in keywords:
            if keyword in text_lower:
                suggested.append({
                    "classification": cpc,
                    "matched_keyword": keyword
                })
                break

    return suggested


def generate_prior_art_search(content: str) -> dict[str, Any]:
    """Generate prior art search strategy."""
    keywords = extract_keywords(content)
    technical_terms = extract_technical_terms(content)
    queries = generate_boolean_queries(keywords)
    cpcs = suggest_cpc_classifications(content)

    keyword_freq = Counter(keywords)
    top_keywords = [{"keyword": k, "frequency": v} for k, v in keyword_freq.most_common(20)]

    result = {
        "recommended_databases": [
            "USPTO Patent Full-Text Database (https://patft.uspto.gov/)",
            "Google Patents (https://patents.google.com/)",
            "Espacenet (https://worldwide.espacenet.com/)",
            "WIPO PatentScope (https://patentscope.wipo.int/)",
            "IEEE Xplore (for non-patent literature)",
            "Google Scholar (for academic papers)"
        ],
        "top_keywords": top_keywords,
        "technical_terms": technical_terms,
        "boolean_queries": queries,
        "suggested_cpc_classifications": cpcs,
        "search_strategy": [
            "Start with keyword searches using the first Boolean query",
            "Review results and refine keywords",
            "Add CPC classification filters",
            "Search non-patent literature",
            "Review citations from relevant patents",
            "Document all searches in prior-art-analysis.md"
        ]
    }

    return result


# Create the MCP server
app = Server("patent-tools-mcp-server")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available patent analysis tools."""
    return [
        Tool(
            name="analyze_patent_word_count",
            description=(
                "Analyzes word count in patent documents. "
                "Checks if abstracts meet the 150-word USPTO requirement. "
                "Identifies document sections (Background, Summary, Description, Claims, Abstract). "
                "Useful for ensuring patent documents meet formatting requirements."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The patent document content to analyze (markdown format)"
                    },
                    "file_path": {
                        "type": "string",
                        "description": "Optional file path to read content from. If provided, content parameter is ignored."
                    },
                    "file_name": {
                        "type": "string",
                        "description": "Optional file name for context (helps identify if document is an abstract)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="analyze_patent_claims",
            description=(
                "Analyzes patent claims for structure, antecedent basis, and dependencies. "
                "Checks for proper claim formatting, transition phrases (comprising, consisting of). "
                "Identifies antecedent basis issues (using 'the' without prior 'a/an'). "
                "Analyzes claim dependencies and categorizes as independent or dependent claims. "
                "Essential for drafting and reviewing patent claims."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The patent document content containing claims to analyze"
                    },
                    "file_path": {
                        "type": "string",
                        "description": "Optional file path to read content from. If provided, content parameter is ignored."
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="generate_prior_art_search",
            description=(
                "Generates prior art search strategy from invention description. "
                "Extracts keywords and technical terms from the invention. "
                "Generates Boolean search queries for patent databases. "
                "Suggests relevant CPC (Cooperative Patent Classification) codes. "
                "Provides recommended databases and search strategy steps. "
                "Critical for conducting thorough prior art searches."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "content": {
                        "type": "string",
                        "description": "The invention description or patent document to analyze for prior art searching"
                    },
                    "file_path": {
                        "type": "string",
                        "description": "Optional file path to read content from. If provided, content parameter is ignored."
                    }
                },
                "required": []
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""

    # Get content from file_path or content parameter
    content = None
    file_name = arguments.get("file_name", "")

    if "file_path" in arguments and arguments["file_path"]:
        file_path = Path(arguments["file_path"])
        if not file_path.exists():
            return [TextContent(
                type="text",
                text=f"Error: File '{file_path}' not found."
            )]
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        if not file_name:
            file_name = file_path.name
    elif "content" in arguments and arguments["content"]:
        content = arguments["content"]
    else:
        return [TextContent(
            type="text",
            text="Error: Either 'content' or 'file_path' parameter is required."
        )]

    # Route to appropriate analysis function
    try:
        if name == "analyze_patent_word_count":
            result = analyze_word_count(content, file_name)

            # Format result as readable text
            output_lines = [
                "=== Patent Word Count Analysis ===\n",
                f"File: {result['file_name'] or 'Provided content'}",
                f"Total words: {result['total_words']}\n"
            ]

            if result["abstract_check"]:
                check = result["abstract_check"]
                output_lines.append("Abstract Requirements:")
                output_lines.append(f"  Maximum allowed: {check['max_allowed']} words")
                output_lines.append(f"  Current count: {check['current_count']} words")
                if check['within_limit']:
                    output_lines.append(f"  ✓ Within limit ({check['remaining']} words remaining)")
                else:
                    output_lines.append(f"  ✗ EXCEEDS limit by {check['exceeds_by']} words")
                output_lines.append("")

            output_lines.append("Document Structure:")
            for section, found in result["sections_found"].items():
                marker = "✓" if found else "-"
                output_lines.append(f"  {marker} {section} section {'found' if found else 'not found'}")

            return [TextContent(
                type="text",
                text="\n".join(output_lines)
            )]

        elif name == "analyze_patent_claims":
            result = analyze_claims(content)

            if "error" in result:
                return [TextContent(
                    type="text",
                    text=f"Error: {result['error']}"
                )]

            # Format result as readable text
            output_lines = [
                "=== Patent Claims Analysis ===\n",
                f"Total claims: {result['total_claims']}",
                f"Independent claims: {result['independent_count']} - {result['independent_claims']}",
                f"Dependent claims: {result['dependent_count']}\n",
                "=== Claim-by-Claim Analysis ===\n"
            ]

            for claim_num, analysis in result["claim_analysis"].items():
                output_lines.append(f"Claim {claim_num}:")
                output_lines.append(f"  Type: {analysis['type'].capitalize()}")
                if analysis['depends_on']:
                    output_lines.append(f"  Depends on: Claim {analysis['depends_on']}")
                output_lines.append(f"  Word count: {analysis['word_count']}")
                if analysis['transition_type']:
                    output_lines.append(f"  Transition: {analysis['transition_type']}")

                if analysis['structure_issues']:
                    for issue in analysis['structure_issues']:
                        output_lines.append(f"  ⚠ {issue}")

                if analysis['antecedent_issues']:
                    for issue in analysis['antecedent_issues']:
                        output_lines.append(f"  ⚠ {issue}")

                if analysis['warnings']:
                    for warning in analysis['warnings']:
                        output_lines.append(f"  ⚠ {warning}")

                if analysis['suggestions']:
                    for suggestion in analysis['suggestions']:
                        output_lines.append(f"  💡 {suggestion}")

                output_lines.append("")

            return [TextContent(
                type="text",
                text="\n".join(output_lines)
            )]

        elif name == "generate_prior_art_search":
            result = generate_prior_art_search(content)

            # Format result as readable text
            output_lines = [
                "=== Prior Art Search Strategy ===\n",
                "1. RECOMMENDED DATABASES:"
            ]
            for db in result["recommended_databases"]:
                output_lines.append(f"   - {db}")

            output_lines.append("\n2. TOP KEYWORDS:")
            for i, kw in enumerate(result["top_keywords"][:20], 1):
                output_lines.append(f"   {i:2d}. {kw['keyword']} ({kw['frequency']} occurrences)")

            if result["technical_terms"]:
                output_lines.append("\n3. TECHNICAL TERMS/PHRASES:")
                for i, term in enumerate(result["technical_terms"], 1):
                    output_lines.append(f"   {i:2d}. {term}")

            output_lines.append("\n4. BOOLEAN SEARCH QUERIES:")
            for i, query in enumerate(result["boolean_queries"], 1):
                output_lines.append(f"   Query {i}: {query}")

            if result["suggested_cpc_classifications"]:
                output_lines.append("\n5. SUGGESTED CPC CLASSIFICATIONS:")
                for cpc in result["suggested_cpc_classifications"]:
                    output_lines.append(f"   - {cpc['classification']} (matched: {cpc['matched_keyword']})")

            output_lines.append("\n6. SEARCH STRATEGY:")
            for i, step in enumerate(result["search_strategy"], 1):
                output_lines.append(f"   Step {i}: {step}")

            return [TextContent(
                type="text",
                text="\n".join(output_lines)
            )]

        else:
            return [TextContent(
                type="text",
                text=f"Error: Unknown tool '{name}'"
            )]

    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error during analysis: {str(e)}"
        )]


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
