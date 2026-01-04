---
description: Review patent document for quality, consistency, and common issues
---

You are reviewing a patent document. Perform comprehensive quality assurance check.

## Review Checklist:

### 1. Structural Completeness

**Required Sections** (verify all present):
- [ ] Title
- [ ] Abstract (if application)
- [ ] Background of the Invention
- [ ] Summary of the Invention
- [ ] Brief Description of the Drawings (if figures)
- [ ] Detailed Description
- [ ] Claims
- [ ] Reference numbers in figures (if applicable)

### 2. Abstract Review

Run word count:
```bash
cd tools && python word-count.py ../patents/drafts/[file].md
```

Check:
- [ ] Length ≤150 words (USPTO requirement)
- [ ] Single paragraph
- [ ] Summarizes what invention is
- [ ] Summarizes what invention does
- [ ] No reference numbers
- [ ] Present tense

### 3. Claims Review

Run claims analyzer:
```bash
cd tools && python claim-analyzer.py ../patents/drafts/[file].md
```

**Structural Issues**:
- [ ] Independent claims are single sentence
- [ ] Dependent claims properly reference parent
- [ ] Claim numbering is sequential
- [ ] Proper punctuation (semicolons, periods)

**Antecedent Basis**:
- [ ] First mention uses "a" or "an"
- [ ] Subsequent mentions use "the"
- [ ] No missing antecedents
- [ ] No new elements in "wherein" clauses

**Claim Quality**:
- [ ] At least 1 independent claim
- [ ] At least 3-5 dependent claims per independent
- [ ] Claims progress from broad to narrow
- [ ] Each dependent claim adds value
- [ ] No redundant claims

**Claim Types**:
- [ ] Apparatus/system claim (if applicable)
- [ ] Method claim (if applicable)
- [ ] Computer-readable medium claim (if software)
- [ ] Multiple independent claims for fallback

**Definiteness**:
- [ ] No vague terms without definition ("substantially," "about")
- [ ] No relative terms without context ("large," "small")
- [ ] No subjective language
- [ ] Clear scope

### 4. Terminology Consistency

**Create Term List**:
- List all key technical terms used
- Check consistency throughout document
- Verify same term used for same concept

**Common Inconsistencies**:
- device / apparatus / system
- method / process / procedure
- data / information
- perform / execute / carry out
- transmit / send / communicate

**Flag**:
- Terms used interchangeably that shouldn't be
- Terms that need definition
- Terms from prior art that should be distinguished

### 5. Specification Review

**Written Description** (§ 112(a)):
- [ ] All claim elements described in specification
- [ ] Sufficient detail to show possession
- [ ] Alternative embodiments described
- [ ] Advantages and benefits explained

**Enablement** (§ 112(a)):
- [ ] Enough detail for skilled person to make/use
- [ ] At least one working example
- [ ] Critical parameters disclosed
- [ ] No undue experimentation required

**Support for Claims**:
- [ ] Each claim element has specification support
- [ ] Broadest claims adequately supported
- [ ] Functional limitations have structural support
- [ ] Alternative embodiments covered

### 6. Reference Numbers

**Consistency Check**:
- [ ] Each component has assigned reference number
- [ ] Same reference number always refers to same component
- [ ] Reference numbers in parentheses: "processor (102)"
- [ ] Reference numbers organized logically (100s, 200s, etc.)
- [ ] All reference numbers in drawings are in description

**Best Practices**:
- 100s for main embodiment
- 200s for alternative embodiment
- 300s for another alternative, etc.

### 7. Technical Accuracy

**Review**:
- [ ] Technical descriptions are accurate
- [ ] No technical errors or impossibilities
- [ ] Terminology matches industry usage
- [ ] Equations/formulas are correct (if any)
- [ ] Units and measurements consistent

### 8. Patent Law Compliance

**Subject Matter** (§ 101):
- [ ] Not abstract idea (or has significantly more)
- [ ] Not law of nature
- [ ] Not natural product
- [ ] Statutory category (process/machine/manufacture/composition)

**Potential Issues**:
- Computer-implemented inventions: Check Alice compliance
- Business methods: Need technical improvement
- Diagnostic methods: Check Mayo compliance
- Software: Must improve computer functioning

### 9. Language and Style

**Patent Conventions**:
- [ ] Present tense throughout
- [ ] Active voice preferred
- [ ] Third person
- [ ] Formal, technical language
- [ ] No marketing language

**Clarity**:
- [ ] Clear, unambiguous language
- [ ] Logical organization
- [ ] Smooth flow between sections
- [ ] Technical terms properly used

**Common Errors**:
- Future tense ("will process")
- Past tense ("processed")
- First person ("we," "our")
- Marketing ("revolutionary," "superior")
- Casual language

### 10. Prior Art Considerations

**Background Section**:
- [ ] Describes technical field
- [ ] Explains problem solved
- [ ] Discusses limitations of prior art
- [ ] Does NOT disparage specific patents/products
- [ ] Sets up need for invention

**Distinguishing Features**:
- [ ] Specification highlights differences from prior art
- [ ] Advantages over prior art explained
- [ ] Unexpected results noted (if any)

### 11. Figures and Drawings

If figures present:
- [ ] All figures referenced in specification
- [ ] Brief Description of Drawings section present
- [ ] Each element in figures has reference number
- [ ] Reference numbers explained in description
- [ ] Multiple views if needed
- [ ] Clear, professional appearance

### 12. Formatting and Grammar

**Check**:
- [ ] No spelling errors
- [ ] No grammatical errors
- [ ] Consistent formatting
- [ ] Proper paragraph breaks
- [ ] Headings properly formatted

**Tools**:
- Run spell-checker
- Review for typos
- Check punctuation

## Generate Review Report:

Provide structured feedback:

**PASSED**:
- List items that meet requirements

**ISSUES FOUND**:
- List specific issues with locations (section, claim number, line)
- Categorize by severity: Critical / Important / Minor

**RECOMMENDATIONS**:
- Specific changes to make
- Prioritized action items
- Suggested improvements

**NEXT STEPS**:
- Required fixes before filing
- Optional improvements
- Recommended additional review (e.g., attorney review)

Be thorough, specific, and constructive in feedback.
