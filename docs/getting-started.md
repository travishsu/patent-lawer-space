# Getting Started with Patent Analysis Environment

## Introduction

Welcome to your patent analysis and writing environment! This guide will help you get started with using this workspace effectively with Claude Code.

## What You Can Do Here

This environment supports the complete patent lifecycle:

1. **Invention Capture**: Document new inventions systematically
2. **Prior Art Research**: Find and analyze existing patents and publications
3. **Patentability Analysis**: Assess whether an invention is patentable
4. **Application Drafting**: Write complete patent applications
5. **Claims Development**: Create strong, defensible patent claims
6. **Freedom to Operate**: Analyze potential infringement risks
7. **Portfolio Management**: Organize multiple patent projects

## Your First Patent Analysis

Let's walk through analyzing and documenting a new invention.

### Step 1: Capture the Invention

Start by documenting the invention details:

```bash
# Copy the invention disclosure template
cp templates/analysis/invention-disclosure.md patents/drafts/my-first-invention-disclosure.md
```

Open the file and fill in:
- What problem does it solve?
- How does it work?
- What makes it novel?
- Who are the inventors?
- When was it conceived?

### Step 2: Generate Prior Art Search Strategy

Use the prior art search tool to get started:

```bash
cd tools
python prior-art-search.py ../patents/drafts/my-first-invention-disclosure.md
```

This will:
- Extract keywords from your invention
- Generate search queries
- Suggest patent classifications
- Recommend databases to search

### Step 3: Conduct Prior Art Search

Search these databases with the generated queries:

1. **USPTO** (https://patft.uspto.gov/)
   - Use the quick search with Boolean queries
   - Try advanced search with CPC classifications

2. **Google Patents** (https://patents.google.com/)
   - More user-friendly interface
   - Good for initial exploration

3. **Google Scholar** (https://scholar.google.com/)
   - Find academic papers and non-patent literature

Document your findings:

```bash
# Create a new analysis file for each relevant patent/publication
cp templates/analysis/prior-art-analysis.md patents/analysis/prior-art-ref-001.md
```

### Step 4: Assess Patentability

After reviewing prior art, perform a patentability analysis:

```bash
cp templates/analysis/patentability-analysis.md patents/analysis/my-first-invention-patentability.md
```

Fill in the analysis considering:
- Is it eligible subject matter?
- Is it novel compared to prior art?
- Would it be obvious to combine prior art references?
- Can you describe it completely?

### Step 5: Draft Claims

Based on your patentability analysis, draft patent claims:

```bash
cp templates/claims/claims-template.md patents/drafts/my-first-invention-claims.md
```

Start with independent claims covering:
- System/apparatus claim
- Method claim
- Computer-readable medium claim (if software-related)

Then add dependent claims with:
- Specific implementations
- Alternative embodiments
- Additional features

Analyze your claims:

```bash
cd tools
python claim-analyzer.py ../patents/drafts/my-first-invention-claims.md
```

### Step 6: Draft the Specification

Create a complete patent application:

```bash
cp templates/applications/utility-patent-template.md patents/drafts/my-first-invention-application.md
```

Fill in all sections:
- **Background**: What's the problem and current solutions?
- **Summary**: What's your solution?
- **Detailed Description**: How does it work in detail?
- **Examples**: Specific implementations
- **Advantages**: Why is it better?

### Step 7: Write the Abstract

Create a concise abstract:

```bash
cp templates/abstracts/abstract-template.md patents/drafts/my-first-invention-abstract.md
```

Check the word count:

```bash
cd tools
python word-count.py ../patents/drafts/my-first-invention-abstract.md
```

Must be 150 words or less!

## Working with Claude Code

### Effective Prompts

Here are proven prompts for patent work:

**For Invention Analysis:**
```
Analyze the invention described in patents/drafts/my-invention.md and identify:
1. The core inventive concept
2. Key technical features
3. Potential novelty over prior art
4. Suggested claim scope
```

**For Prior Art Analysis:**
```
I found a relevant patent [US1234567]. Compare it to my invention in
patents/drafts/my-invention.md. Create an element-by-element claim chart
showing what's disclosed and what's different.
```

**For Claims Drafting:**
```
Draft patent claims for the invention in patents/drafts/my-invention.md.
Include:
- 3 independent claims (system, method, computer-readable medium)
- 7-10 dependent claims covering specific features and alternatives
- Use proper claim formatting and antecedent basis
```

**For Specification Writing:**
```
Write the detailed description section for my patent application based on
patents/drafts/my-invention.md. Include:
- Multiple embodiments
- Implementation details
- Reference to figures (which I'll create)
- At least 2000 words of technical detail
```

**For Review and Improvement:**
```
Review my patent application in patents/drafts/my-invention-application.md.
Check for:
- Enablement issues
- Missing claim support
- Definiteness problems
- Inconsistent terminology
- Areas needing more detail
```

### Iterative Refinement

Patent drafting is iterative. Work with Claude Code to:

1. **Expand Descriptions**: "Add more detail to the implementation section"
2. **Add Embodiments**: "Describe an alternative embodiment using [technology X]"
3. **Strengthen Claims**: "Make claim 1 broader while avoiding [prior art reference]"
4. **Fill Gaps**: "What aspects of the invention need more explanation?"

## Common Scenarios

### Scenario 1: I Have a New Invention Idea

1. Fill out invention disclosure form
2. Run prior art search tool
3. Search USPTO and Google Patents
4. If looks novel → draft provisional application
5. If questionable → do deeper patentability analysis

### Scenario 2: I Found Relevant Prior Art

1. Create prior-art-analysis.md for the reference
2. Do element-by-element comparison
3. Identify what's different
4. Adjust claims to emphasize differences
5. Update specification to highlight novelty

### Scenario 3: I Need to File Quickly

Focus on:
1. Invention disclosure (capture everything)
2. Quick prior art search (1-2 hours)
3. Draft broad independent claims
4. Write basic specification
5. File provisional application (lower cost, buys time)
6. Refine over next 12 months before non-provisional

### Scenario 4: Checking Freedom to Operate

1. Define your product features clearly
2. Use FTO analysis template
3. Search for patents covering those features
4. Analyze each concerning patent
5. Develop risk mitigation strategy
6. Consider design-arounds or licenses

## Best Practices

### Organization

- **One folder per invention project**: Keep related files together
- **Clear naming**: `invention-name-document-type-version.md`
- **Version control**: Use git to track changes
- **Regular commits**: Save progress frequently

### Documentation

- **Document searches**: Record what you searched and when
- **Save references**: Keep copies of key prior art
- **Track decisions**: Note why you made claim scope choices
- **Maintain timeline**: Document conception, disclosure, filing dates

### Quality

- **Be thorough**: Better to over-document than under-document
- **Be precise**: Use exact technical terminology
- **Be consistent**: Same term for same concept throughout
- **Be complete**: Every claim element should be in the specification

### Collaboration

- **Share findings**: Document prior art for the team
- **Review each other's work**: Fresh eyes catch issues
- **Use templates**: Consistency across the team
- **Centralize knowledge**: Keep all patent work in this repo

## Tools Reference

### word-count.py

**Purpose**: Check word counts and document structure

**Usage**:
```bash
python word-count.py <path-to-markdown-file>
```

**When to use**:
- Before finalizing abstracts (must be ≤150 words)
- To check document completeness
- To verify all sections are present

### claim-analyzer.py

**Purpose**: Analyze patent claims for issues

**Usage**:
```bash
python claim-analyzer.py <path-to-claims-file>
```

**When to use**:
- After drafting claims
- Before filing
- When revising claims in response to rejections
- To catch antecedent basis issues

### prior-art-search.py

**Purpose**: Generate search strategies

**Usage**:
```bash
python prior-art-search.py <path-to-invention-description>
```

**When to use**:
- At the start of any prior art search
- When searching a new technical area
- To identify relevant CPC classifications
- To generate comprehensive search queries

## Next Steps

Now that you're familiar with the environment:

1. **Try the workflow** with a sample invention
2. **Customize templates** for your field
3. **Build your reference library** of key patents
4. **Develop domain expertise** in your technical area
5. **Integrate with your IP strategy**

## Getting Help

If you have questions:

1. Check the main README.md
2. Review template comments and guidelines
3. Consult the MPEP (Manual of Patent Examining Procedure)
4. Ask Claude Code for help with specific tasks
5. Consult with a patent attorney for legal questions

## What's Next?

- **Learn more**: Read docs/patent-law-basics.md
- **See examples**: Check the examples/ directory (when populated)
- **Advanced topics**: Review docs/advanced-topics.md (coming soon)
- **Customize**: Adapt templates to your needs

Happy inventing and documenting!
