# Claude Code Rules for Patent Analysis and Writing

## Project Context

This is a patent analysis and writing environment designed for:
- Drafting patent applications (utility, design, provisional)
- Conducting prior art searches and analysis
- Performing freedom to operate (FTO) assessments
- Analyzing patentability under 35 U.S.C. § 101, 102, 103, 112
- Managing invention disclosures
- Claims drafting and analysis

## Core Principles

### 1. Legal Precision and Accuracy

- **Terminology Consistency**: Maintain consistent terminology throughout all patent documents. Once a term is defined (e.g., "computing device"), use it consistently.
- **Antecedent Basis**: Always ensure proper antecedent basis in claims. First mention uses "a/an," subsequent mentions use "the."
- **Definiteness**: Avoid vague terms like "substantially," "approximately," unless necessary and properly defined.
- **No Legal Advice Disclaimer**: Remember that Claude provides informational assistance only, not legal advice. Recommend professional patent attorney review for filing.

### 2. Patent-Specific Writing Standards

- **Claims Format**: Independent claims should be single sentence. Dependent claims reference parent claim number.
- **Present Tense**: Use present tense in specifications and claims.
- **Active Voice Preferred**: "The processor executes" not "is executed by the processor."
- **Reference Numbers**: Use parenthetical reference numbers consistently (e.g., "processor (102)").
- **Section Ordering**: Follow standard patent structure: Title, Abstract, Background, Summary, Brief Description of Drawings, Detailed Description, Claims.

### 3. Analysis Rigor

- **Element-by-Element Analysis**: When comparing claims to prior art, analyze each claim element individually.
- **Document Sources**: Always cite specific patent numbers, publication dates, and relevant sections.
- **Obviousness Analysis**: Consider Graham factors (scope/content of prior art, differences, skill level, secondary considerations).
- **Multiple Perspectives**: Consider both patentability and invalidity angles.

### 4. File Organization

- **Drafts Location**: Work-in-progress goes in `patents/drafts/`
- **Analysis Location**: Analyses go in `patents/analysis/`
- **Use Templates**: Always start from templates in `templates/` directory
- **Naming Convention**: Use descriptive names: `[invention-name]-[document-type].md`

## Specific Instructions

### When Drafting Patent Applications

1. **Start with Templates**: Always use `templates/applications/utility-patent-template.md` as starting point
2. **Claims First**: Draft claims before detailed description when possible
3. **Multiple Embodiments**: Describe at least 2-3 alternative embodiments
4. **Broad to Narrow**: Start with broad description, then provide specific details
5. **Support Claims**: Ensure specification provides written description and enablement for all claim elements
6. **Consistent Terminology**: Create a term glossary for complex inventions
7. **Reference Numbers**: Assign reference numbers systematically (100s for main invention, 200s for alternative embodiment, etc.)

### When Drafting Claims

1. **Independent Claims**: Start with broadest reasonable interpretation
2. **Claim Set Strategy**: Draft at least:
   - 1 apparatus/system claim
   - 1 method claim
   - 1 computer-readable medium claim (for software)
3. **Dependent Claims**: Each should add meaningful limitation
4. **Claim Differentiation**: Ensure dependent claims don't merely restate independent claim
5. **Functional Language**: Use functional language sparingly; prefer structural limitations
6. **Use Templates**: Reference `templates/claims/claims-template.md`

### When Conducting Prior Art Analysis

1. **Comprehensive Search**: Search USPTO, Google Patents, and academic databases
2. **Document Search Strategy**: Record all search queries and databases used
3. **Claim Charts**: Create element-by-element claim charts for each relevant reference
4. **Date Verification**: Check publication dates for 102 analysis
5. **Combination Analysis**: Consider obviousness from combinations under 103
6. **Use Template**: Follow `templates/analysis/prior-art-analysis.md` structure

### When Performing Patentability Analysis

1. **All Requirements**: Address § 101, 102, 103, and 112 requirements
2. **Evidence-Based**: Support conclusions with specific prior art references
3. **Identify Gaps**: Highlight what makes invention novel and non-obvious
4. **Prosecution Strategy**: Suggest amendments or arguments if issues found
5. **Use Template**: Follow `templates/analysis/patentability-analysis.md`

### When Conducting FTO Analysis

1. **Identify All Features**: List all potentially infringing product/method features
2. **Claim Mapping**: Map each patent claim to product features
3. **Infringement Analysis**: Apply literal infringement and doctrine of equivalents
4. **Validity Check**: Assess validity of concerning patents
5. **Design-Around**: Suggest design-around options if high risk
6. **Use Template**: Follow `templates/analysis/freedom-to-operate.md`

## Tool Usage

### Word Count Tool
```bash
cd tools && python word-count.py ../patents/drafts/[file].md
```
Use for abstracts (must be ≤150 words) and checking document structure.

### Claims Analyzer
```bash
cd tools && python claim-analyzer.py ../patents/drafts/[file].md
```
Use to check antecedent basis, claim structure, and identify issues.

### Prior Art Search Helper
```bash
cd tools && python prior-art-search.py ../patents/drafts/[file].md
```
Use to generate search queries and CPC classifications.

## Quality Checks

Before considering any patent document complete, verify:

- [ ] Consistent terminology throughout
- [ ] All claims have proper antecedent basis
- [ ] Reference numbers assigned and used consistently
- [ ] Abstract is ≤150 words (use word-count.py)
- [ ] All required sections present
- [ ] Claims analyzed with claim-analyzer.py
- [ ] Prior art documented and analyzed
- [ ] Figures referenced in specification
- [ ] No typos or grammatical errors
- [ ] Professional review recommended before filing

## Common Pitfalls to Avoid

1. **Inconsistent Terms**: Using "device," "apparatus," "system" interchangeably
2. **Missing Antecedent Basis**: Introducing element with "the" instead of "a/an"
3. **Vague Limitations**: Terms like "about," "near," "close to" without definition
4. **Missing Written Description**: Claims not supported by specification
5. **Insufficient Detail**: Not enough detail to enable person of skill to practice
6. **Overlooking Prior Art**: Incomplete search leading to anticipation/obviousness issues
7. **Abstract Too Long**: USPTO requires ≤150 words
8. **Poor Claim Differentiation**: Dependent claims that don't add value

## Patent Law References

When analyzing or drafting, consider:

- **35 U.S.C. § 101**: Patent-eligible subject matter (avoid abstract ideas, laws of nature)
- **35 U.S.C. § 102**: Novelty (each element must be new)
- **35 U.S.C. § 103**: Non-obviousness (inventive step required)
- **35 U.S.C. § 112(a)**: Written description and enablement
- **35 U.S.C. § 112(b)**: Definiteness of claims
- **35 U.S.C. § 112(f)**: Means-plus-function claiming (interpret carefully)

Consult MPEP (Manual of Patent Examining Procedure) for examination guidelines.

## Interaction Guidelines

### When User Asks for Patent Drafting
1. Ask for invention disclosure or description
2. Clarify the inventive concept and key features
3. Discuss potential claim scope
4. Draft claims first, then specification
5. Recommend prior art search if not done
6. Use appropriate templates
7. Run quality checks

### When User Asks for Analysis
1. Request relevant documents (invention description, prior art references)
2. Clarify analysis type (patentability, FTO, prior art)
3. Use appropriate template
4. Provide thorough, evidence-based analysis
5. Support conclusions with specific citations
6. Suggest next steps or strategies

### When User Asks for Prior Art Search
1. Extract keywords and concepts from invention
2. Generate Boolean search queries
3. Suggest CPC/IPC classifications
4. Search multiple databases
5. Document search methodology
6. Create claim charts for relevant references
7. Assess novelty and non-obviousness

## Customization

Users can extend this environment by:
- Adding industry-specific templates in `templates/`
- Creating custom analysis tools in `tools/`
- Adding reference materials in `docs/`
- Including sample patents as examples in `examples/`

## Version Control Best Practices

- Commit after major sections completed
- Use descriptive commit messages (e.g., "Draft claims for [invention]")
- Tag versions for filed applications
- Keep separate branches for different inventions
- Never commit confidential client information to public repos

## Confidentiality Reminder

Patent applications contain confidential and potentially valuable intellectual property. Always:
- Confirm repository is private for client work
- Avoid exposing trade secrets
- Redact sensitive information in examples
- Follow firm/organization confidentiality policies
- Consider provisional filing before public disclosure

---

**Last Updated**: 2026-01-04
**For**: Claude Code patent analysis and writing workflows
**Status**: Active configuration
