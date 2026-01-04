---
description: Conduct comprehensive prior art search and analysis
---

You are conducting a prior art search and analysis. Follow this systematic approach:

1. **Extract Search Terms**:
   - Read invention description from provided file or user input
   - Identify key technical concepts and features
   - Extract keywords and synonyms
   - Identify related technical fields
   - Run `cd tools && python prior-art-search.py ../patents/drafts/[invention-file].md` if applicable

2. **Generate Search Queries**:
   - Create Boolean search queries combining key terms
   - Use AND, OR, NOT operators strategically
   - Include synonyms and related terms
   - Create queries for different claim aspects
   - Example: `(machine learning OR neural network OR deep learning) AND (optimization OR tuning) AND (hyperparameter OR parameter selection)`

3. **Identify Classifications**:
   - Suggest relevant CPC (Cooperative Patent Classification) codes
   - Suggest relevant IPC (International Patent Classification) codes
   - Explain why each classification is relevant
   - Recommend starting with broader classifications then narrowing

4. **Search Multiple Databases**:
   - USPTO PatFT/AppFT (https://patft.uspto.gov/)
   - Google Patents (https://patents.google.com/)
   - Espacenet (https://worldwide.espacenet.com/)
   - WIPO PatentScope (https://patentscope.wipo.int/)
   - For non-patent literature: Google Scholar, IEEE Xplore, PubMed

5. **Document Search Strategy**:
   - Record all search queries used
   - Note databases searched
   - Document search dates
   - Track number of results per query
   - Create file: `patents/analysis/[invention-name]-search-strategy.md`

6. **Identify Relevant References**:
   - List patents/publications found
   - For each reference, note:
     - Patent/publication number
     - Title
     - Publication date
     - Key relevant features
     - Relevance rating (high/medium/low)

7. **Create Claim Charts**:
   - For high-relevance references, create element-by-element comparison
   - Use template: `templates/analysis/prior-art-analysis.md`
   - Compare each claim element to prior art disclosure
   - Note what is disclosed vs. what is missing

8. **Anticipation Analysis** (35 U.S.C. § 102):
   - Does single reference disclose all claim elements?
   - Check publication date (before or after invention date/filing date)
   - Assess whether reference is enabling
   - Identify any missing elements

9. **Obviousness Analysis** (35 U.S.C. § 103):
   - Consider combinations of references
   - Would combination be obvious to person of ordinary skill?
   - Is there motivation to combine?
   - Are there any unexpected results or advantages?
   - Apply Graham factors

10. **Generate Analysis Report**:
    - Create `patents/analysis/[invention-name]-prior-art.md`
    - List all relevant references with citations
    - Provide claim charts for key references
    - Summarize novelty assessment
    - Identify distinguishing features
    - Recommend claim amendments if needed
    - Suggest arguments to overcome prior art

11. **Update Claims/Specification**:
    - If prior art issues found, suggest claim amendments
    - Recommend adding distinguishing features to specification
    - Suggest emphasizing advantages over prior art

Document everything thoroughly. Prior art analysis is critical for patentability and invalidity defense.
