---
description: Draft a new patent application from invention description
---

You are helping draft a new patent application. Follow these steps:

1. **Gather Information**:
   - Ask for invention description or read from provided file
   - Clarify the inventive concept and key distinguishing features
   - Identify potential embodiments and variations
   - Understand the technical field and problem solved

2. **Create Working Files**:
   - Create new draft in `patents/drafts/[invention-name]-application.md` using `templates/applications/utility-patent-template.md`
   - Create claims file in `patents/drafts/[invention-name]-claims.md` using `templates/claims/claims-template.md`
   - Create abstract file in `patents/drafts/[invention-name]-abstract.md` using `templates/abstracts/abstract-template.md`

3. **Draft Claims First**:
   - Draft at least 3 independent claims (apparatus, method, computer-readable medium if applicable)
   - Add 5-10 dependent claims for each independent claim
   - Ensure proper antecedent basis ("a/an" for first mention, "the" for subsequent)
   - Keep claims broad but patentable
   - Run `cd tools && python claim-analyzer.py ../patents/drafts/[invention-name]-claims.md`

4. **Draft Specification**:
   - Title: Concise, descriptive (2-7 words)
   - Background: Technical field, problem, limitations of prior art
   - Summary: Overview of invention and advantages (2-3 paragraphs)
   - Detailed Description: Multiple embodiments, reference numbers, how it works
   - Ensure specification supports all claim limitations

5. **Draft Abstract**:
   - Single paragraph, 50-150 words
   - Summarize what invention is and what it does
   - Run `cd tools && python word-count.py ../patents/drafts/[invention-name]-abstract.md`
   - Ensure ≤150 words

6. **Quality Checks**:
   - Verify consistent terminology throughout
   - Check all reference numbers used consistently
   - Ensure claims fully supported by specification
   - Verify proper antecedent basis in all claims
   - Check abstract word count

7. **Recommend Next Steps**:
   - Prior art search (if not already done)
   - Professional patent attorney review
   - Figure preparation
   - Provisional vs non-provisional filing decision

Always use templates, maintain consistency, and follow patent drafting best practices per CLAUDE.md.
