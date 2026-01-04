#!/usr/bin/env python3
"""
Prior Art Search Helper
Generates search queries for patent databases based on invention description.
"""

import sys
import re
from pathlib import Path


class SearchQueryGenerator:
    def __init__(self):
        self.keywords = set()
        self.technical_terms = set()
        self.classifications = []

    def extract_keywords(self, text):
        """Extract potential keywords from text."""
        # Remove common words
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

        # Find multi-word technical terms (words connected by hyphens or common tech phrases)
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
                self.technical_terms.add(match.group(0))

        return keywords

    def generate_boolean_queries(self, keywords, max_keywords=5):
        """Generate Boolean search queries."""
        queries = []

        # Get most frequent keywords
        from collections import Counter
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

    def suggest_cpc_classifications(self, text):
        """Suggest potential CPC classifications based on text content."""
        # Common CPC classes and their keywords
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
                    if cpc not in suggested:
                        suggested.append(cpc)
                    break

        return suggested

    def generate_search_strategy(self, text):
        """Generate a comprehensive search strategy."""
        keywords = self.extract_keywords(text)
        queries = self.generate_boolean_queries(keywords)
        cpcs = self.suggest_cpc_classifications(text)

        print(f"\n{'='*70}")
        print("PRIOR ART SEARCH STRATEGY")
        print(f"{'='*70}\n")

        print("1. RECOMMENDED DATABASES:")
        print("   - USPTO Patent Full-Text Database (https://patft.uspto.gov/)")
        print("   - Google Patents (https://patents.google.com/)")
        print("   - Espacenet (https://worldwide.espacenet.com/)")
        print("   - WIPO PatentScope (https://patentscope.wipo.int/)")
        print("   - IEEE Xplore (for non-patent literature)")
        print("   - Google Scholar (for academic papers)")

        print(f"\n2. SUGGESTED KEYWORDS (Top 20):")
        from collections import Counter
        keyword_freq = Counter(keywords)
        for i, (keyword, freq) in enumerate(keyword_freq.most_common(20), 1):
            print(f"   {i:2d}. {keyword} ({freq} occurrences)")

        if self.technical_terms:
            print(f"\n3. TECHNICAL TERMS/PHRASES:")
            for i, term in enumerate(sorted(self.technical_terms), 1):
                print(f"   {i:2d}. {term}")

        print(f"\n4. BOOLEAN SEARCH QUERIES:")
        for i, query in enumerate(queries, 1):
            print(f"   Query {i}: {query}")

        if cpcs:
            print(f"\n5. SUGGESTED CPC CLASSIFICATIONS:")
            for cpc in cpcs:
                print(f"   - {cpc}")
            print(f"\n   Use format: CPC={cpc} in USPTO database")

        print(f"\n6. SEARCH STRATEGY:")
        print("   Step 1: Start with keyword searches using Query 1")
        print("   Step 2: Review results and refine keywords")
        print("   Step 3: Add CPC classification filters")
        print("   Step 4: Search non-patent literature")
        print("   Step 5: Review citations from relevant patents")
        print("   Step 6: Document all searches in prior-art-analysis.md")

        print(f"\n7. DOCUMENTATION TEMPLATE:")
        print("   Use: templates/analysis/prior-art-analysis.md")

        print(f"\n{'='*70}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python prior-art-search.py <file_path>")
        print("Example: python prior-art-search.py ../patents/drafts/my-invention.md")
        print("\nThis tool analyzes your invention description and generates")
        print("search queries and strategies for prior art searching.")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    generator = SearchQueryGenerator()
    generator.generate_search_strategy(content)


if __name__ == "__main__":
    main()
