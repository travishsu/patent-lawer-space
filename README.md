# Patent Analysis and Writing Environment

A comprehensive workspace for patent analysis, prior art searching, and patent application drafting using Claude Code.

## Overview

This repository provides a structured environment for conducting patent-related work, including:

- Patent application drafting
- Prior art analysis
- Freedom to operate (FTO) analysis
- Patentability assessments
- Invention disclosure management
- Claims analysis and drafting

## Directory Structure

```
patent-lawer-space/
├── patents/              # Patent documents
│   ├── drafts/          # Work in progress
│   ├── filed/           # Filed applications
│   └── analysis/        # Analysis reports
├── templates/           # Document templates
│   ├── applications/    # Patent application templates
│   ├── claims/         # Claims templates and examples
│   ├── abstracts/      # Abstract templates
│   ├── specifications/ # Detailed description templates
│   └── analysis/       # Analysis templates
├── tools/              # Utility scripts
├── mcp-server/         # Model Context Protocol server
├── docs/               # Documentation
└── examples/           # Example documents
```

## Templates

### Patent Application Templates

- **`templates/applications/utility-patent-template.md`**
  - Complete utility patent application template
  - Includes all required sections (Background, Summary, Detailed Description, Claims, Abstract)
  - Guidelines for each section

### Claims Templates

- **`templates/claims/claims-template.md`**
  - Independent and dependent claims structure
  - Claims drafting guidelines
  - Examples of different claim types (system, method, computer-readable medium)

### Analysis Templates

- **`templates/analysis/prior-art-analysis.md`**
  - Systematic prior art evaluation
  - Element-by-element claim charts
  - Obviousness analysis framework

- **`templates/analysis/patentability-analysis.md`**
  - Comprehensive patentability assessment
  - 35 U.S.C. § 101, 102, 103, 112 analysis
  - Prosecution strategy recommendations

- **`templates/analysis/freedom-to-operate.md`**
  - FTO/clearance analysis template
  - Risk assessment framework
  - Mitigation strategies

- **`templates/analysis/invention-disclosure.md`**
  - Invention disclosure form
  - Captures all necessary invention details
  - Prior art documentation

## Tools

The repository includes both standalone Python tools and an MCP server that exposes these tools to Claude.

### MCP Server (Recommended for Claude Desktop)

The **Model Context Protocol (MCP) server** makes all patent analysis tools available directly to Claude through the MCP protocol. This is the recommended way to use the tools with Claude Desktop.

**Quick Setup:**

1. Install dependencies:
   ```bash
   cd mcp-server
   pip install -r requirements.txt
   ```

2. Configure Claude Desktop (see `mcp-server/README.md` for details):
   ```json
   {
     "mcpServers": {
       "patent-tools": {
         "command": "python",
         "args": ["/absolute/path/to/patent-lawer-space/mcp-server/run.py"]
       }
     }
   }
   ```

3. Restart Claude Desktop and the tools will be available automatically!

**Available MCP Tools:**
- `analyze_patent_word_count` - Word count and structure validation
- `analyze_patent_claims` - Claims analysis with antecedent basis checking
- `generate_prior_art_search` - Prior art search query generation

See [mcp-server/README.md](mcp-server/README.md) for complete documentation.

### Standalone Python Tools

These tools can also be run directly from the command line:

### Word Count Tool

Analyzes patent documents and checks word count against requirements.

```bash
cd tools
python word-count.py ../templates/abstracts/my-abstract.md
```

Features:
- Counts words excluding markdown formatting
- Checks abstracts against 150-word limit
- Verifies document structure

### Claims Analyzer

Analyzes patent claims for common issues and best practices.

```bash
cd tools
python claim-analyzer.py ../templates/claims/my-claims.md
```

Features:
- Identifies independent vs. dependent claims
- Checks antecedent basis
- Analyzes claim structure
- Provides suggestions for improvement

### Prior Art Search Helper

Generates search queries and strategies for prior art searching.

```bash
cd tools
python prior-art-search.py ../patents/drafts/my-invention.md
```

Features:
- Extracts keywords from invention description
- Generates Boolean search queries
- Suggests CPC classifications
- Recommends search databases and strategy

## Quick Start Guide

### 1. Start a New Patent Application

```bash
# Create a new draft from template
cp templates/applications/utility-patent-template.md patents/drafts/my-invention.md

# Edit the file with your invention details
```

### 2. Draft Claims

```bash
# Create claims document
cp templates/claims/claims-template.md patents/drafts/my-invention-claims.md

# Analyze your claims
cd tools
python claim-analyzer.py ../patents/drafts/my-invention-claims.md
```

### 3. Conduct Prior Art Search

```bash
# Generate search strategy
cd tools
python prior-art-search.py ../patents/drafts/my-invention.md

# Document findings
cp templates/analysis/prior-art-analysis.md patents/analysis/my-invention-prior-art.md
```

### 4. Analyze Patentability

```bash
# Create patentability analysis
cp templates/analysis/patentability-analysis.md patents/analysis/my-invention-patentability.md

# Fill out the analysis based on prior art findings
```

### 5. Write Abstract

```bash
# Create abstract
cp templates/abstracts/abstract-template.md patents/drafts/my-invention-abstract.md

# Check word count
cd tools
python word-count.py ../patents/drafts/my-invention-abstract.md
```

## Best Practices

### Patent Drafting

1. **Start with Invention Disclosure**: Use the invention disclosure template to capture all details
2. **Conduct Prior Art Search First**: Understand the landscape before drafting
3. **Draft Claims Early**: Claims define the scope - start here
4. **Multiple Embodiments**: Describe various implementations
5. **Consistent Terminology**: Use the same terms throughout
6. **Reference Numbers**: Assign and use systematically
7. **Figures**: Create clear diagrams with proper labeling

### Claims Drafting

1. **Independent Claims**: Start broad, cover core inventive concept
2. **Dependent Claims**: Add specific implementations and alternatives
3. **Claim Differentiation**: Each claim should add value
4. **Clear Language**: Avoid ambiguity
5. **Antecedent Basis**: Proper use of "a/an" and "the"
6. **Multiple Claim Types**: Include system, method, and CRM claims if applicable

### Prior Art Analysis

1. **Systematic Search**: Use multiple databases and search strategies
2. **Document Everything**: Record search queries and results
3. **Element-by-Element**: Compare each claim element to prior art
4. **Consider Combinations**: Analyze obviousness from combinations
5. **Update Regularly**: Prior art landscape changes

### Analysis Documentation

1. **Be Thorough**: Complete all sections of analysis templates
2. **Objective Assessment**: Honest evaluation of strengths and weaknesses
3. **Support Conclusions**: Provide evidence and reasoning
4. **Consider Alternatives**: Multiple strategies and approaches
5. **Regular Updates**: Keep analyses current

## Working with Claude Code

This environment is optimized for use with Claude Code. Here are some effective prompts:

### Drafting

```
"Help me draft a patent application for [invention description].
Use the utility-patent-template.md as the starting point."
```

### Analysis

```
"Analyze the patentability of my invention in patents/drafts/my-invention.md.
Consider the prior art I've documented in patents/analysis/prior-art-findings.md."
```

### Claims

```
"Draft patent claims for my invention. Create at least 3 independent claims
covering apparatus, method, and computer-readable medium, plus dependent claims."
```

### Prior Art Search

```
"Help me find prior art for [invention]. Generate search queries and
search USPTO, Google Patents, and recommend academic sources."
```

### Review

```
"Review my patent claims in patents/drafts/my-claims.md. Check for:
- Antecedent basis issues
- Claim differentiation
- Proper structure
- Potential invalidity issues"
```

## Patent Law Fundamentals

### Patentability Requirements (U.S.)

1. **35 U.S.C. § 101 - Eligible Subject Matter**
   - Process, machine, manufacture, or composition of matter
   - Not abstract idea, law of nature, or natural phenomenon

2. **35 U.S.C. § 102 - Novelty**
   - New (not in prior art)
   - Each claim element must be novel

3. **35 U.S.C. § 103 - Non-Obviousness**
   - Not obvious to person skilled in the art
   - Must have inventive step beyond prior art

4. **35 U.S.C. § 112 - Written Description, Enablement, Definiteness**
   - Adequate description of invention
   - Enables others to make and use
   - Claims are clear and definite

### Key Deadlines

- **Provisional to Non-Provisional**: 12 months
- **Public Disclosure**: File before or within grace period (1 year in U.S.)
- **PCT Filing**: 12 months from priority date
- **Office Action Response**: Typically 3-6 months
- **Foreign Filings**: 30 months from priority (via PCT)

### Patent Types

- **Utility Patent**: Functional inventions (20 years)
- **Design Patent**: Ornamental designs (15 years)
- **Plant Patent**: New plant varieties (20 years)
- **Provisional**: Placeholder (not examined, 12-month term)

## Common Workflows

### New Invention Workflow

1. Fill out invention disclosure form
2. Conduct preliminary prior art search
3. Assess patentability
4. Draft claims
5. Draft specification
6. Create abstract
7. Prepare figures
8. Review and refine
9. File provisional or non-provisional application

### Prior Art Analysis Workflow

1. Extract keywords from invention
2. Generate search queries
3. Search USPTO, Google Patents, academic databases
4. Document each relevant reference
5. Create claim charts
6. Assess anticipation and obviousness risks
7. Identify distinguishing features
8. Update claims and specification

### FTO Analysis Workflow

1. Identify product features
2. Search for relevant patents
3. Analyze each patent claim-by-claim
4. Assess infringement risk
5. Evaluate validity of high-risk patents
6. Consider design-around options
7. Assess licensing opportunities
8. Develop risk mitigation strategy

## Resources

### Patent Databases

- **USPTO**: https://patft.uspto.gov/
- **Google Patents**: https://patents.google.com/
- **Espacenet**: https://worldwide.espacenet.com/
- **WIPO PatentScope**: https://patentscope.wipo.int/

### Classification Systems

- **CPC** (Cooperative Patent Classification): https://www.cooperativepatentclassification.org/
- **IPC** (International Patent Classification): https://www.wipo.int/classifications/ipc/

### Non-Patent Literature

- **IEEE Xplore**: https://ieeexplore.ieee.org/
- **Google Scholar**: https://scholar.google.com/
- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/

### Guidelines and Rules

- **MPEP** (Manual of Patent Examining Procedure): https://www.uspto.gov/web/offices/pac/mpep/
- **USPTO Rules**: https://www.uspto.gov/patents/laws

## Tips for Success

1. **Document Everything**: Keep detailed records of all work
2. **Version Control**: Track changes to applications and analyses
3. **Consistent Naming**: Use clear, descriptive file names
4. **Regular Backups**: Protect your work
5. **Collaborate**: Use this environment for team collaboration
6. **Stay Current**: Patent law and technology evolve
7. **Professional Review**: Consider professional patent attorney review for final applications

## Contributing

This is a template environment. Customize it for your specific needs:

- Add industry-specific templates
- Create custom analysis tools
- Develop additional scripts
- Add reference materials
- Include sample patents from your field

## License

This template repository is provided as-is for patent analysis and drafting work.

## Disclaimer

This environment and its templates are for informational purposes only and do not constitute legal advice. For actual patent applications, consult with a registered patent attorney or agent. Patent laws vary by jurisdiction and change over time.

---

**Version**: 1.0
**Last Updated**: 2026-01-04
**Maintained for**: Claude Code patent analysis and writing workflows
