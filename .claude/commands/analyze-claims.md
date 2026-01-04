---
description: Analyze patent claims for structural issues and best practices
---

You are analyzing patent claims. Perform the following comprehensive analysis:

1. **Run Automated Analysis**:
   ```bash
   cd tools && python claim-analyzer.py ../patents/drafts/[claims-file].md
   ```

2. **Structural Analysis**:
   - Count independent vs dependent claims
   - Verify single-sentence format for independent claims
   - Check proper claim numbering and dependencies
   - Ensure dependent claims reference correct parent claims

3. **Antecedent Basis Check**:
   - Verify first introduction uses "a" or "an"
   - Verify subsequent uses employ "the"
   - Identify any missing antecedent basis
   - Flag improper element introductions

4. **Claim Differentiation Analysis**:
   - Ensure each dependent claim adds meaningful limitation
   - Check for redundant claims
   - Verify claim set provides adequate fallback positions
   - Assess breadth-to-narrow progression

5. **Terminology Consistency**:
   - Identify all key terms used
   - Check for inconsistent usage (e.g., "device" vs "apparatus")
   - Verify terms are properly defined if necessary
   - Flag potentially indefinite terms

6. **Functional Claiming**:
   - Identify functional limitations
   - Check for means-plus-function claims (35 U.S.C. § 112(f))
   - Verify adequate structural support in specification
   - Suggest structural alternatives if over-reliant on functional language

7. **Claim Types Coverage**:
   - Verify apparatus/system claims present
   - Verify method claims present
   - Check for computer-readable medium claims (if software)
   - Suggest additional claim types if gaps exist

8. **Definiteness Check** (35 U.S.C. § 112(b)):
   - Flag vague terms: "substantially," "approximately," "about"
   - Identify relative terms needing context: "large," "small," "thin"
   - Check for ambiguous claim scope
   - Suggest clarifications

9. **Breadth Assessment**:
   - Evaluate independent claim breadth
   - Check for overly narrow limitations
   - Identify opportunities to broaden
   - Assess anticipation/obviousness risk if too broad

10. **Generate Report**:
    - Summarize findings
    - List specific issues with claim numbers
    - Provide concrete suggestions for improvement
    - Prioritize issues by severity

Provide detailed, actionable feedback to improve claim quality and patentability.
