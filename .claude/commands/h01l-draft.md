---
description: Draft H01L semiconductor device patent application
---

You are helping draft an H01L semiconductor device patent application. Follow these specialized steps for semiconductor patents:

## 1. Gather Semiconductor-Specific Information

Ask the user to provide or clarify:
- **Device Type**: Transistor, memory, LED, power device, sensor, etc.
- **Technology Node/Scale**: 7nm, 5nm, 3nm, power device voltage class, etc.
- **Key Innovation**: Novel structure, material, process, or combination
- **Substrate Type**: Si, SiC, GaN, GaAs, SOI, etc.
- **Application Area**: Logic, memory, power, RF, optoelectronics, etc.
- **Main Advantages**: Performance metrics (speed, power, area, cost, reliability)

## 2. Perform Priority Company Prior Art Check

**CRITICAL**: Before drafting, conduct quick prior art check focusing on:
- **TSMC** (Taiwan Semiconductor Manufacturing)
- **Samsung Electronics**
- **Intel Corporation**
- **ASE Technology** (Advanced Semiconductor Engineering)
- **Amkor Technology**

Use the search guide at `docs/h01l-prior-art-search-guide.md` to:
1. Search each priority company for similar technology
2. Identify key differences from prior art
3. Note specific claims/structures to distinguish from

Quick search queries:
```
assignee:(TSMC OR Samsung OR Intel OR ASE OR Amkor) AND CPC:H01L AND [key technology terms]
```

## 3. Create Working Files

Create semiconductor-specific draft files:

- **Application**: `patents/drafts/[invention-name]-h01l-application.md`
  - Use template: `templates/applications/h01l-semiconductor-template.md`

- **Claims**: `patents/drafts/[invention-name]-h01l-claims.md`
  - Use template: `templates/claims/h01l-claims-template.md`

- **Abstract**: `patents/drafts/[invention-name]-abstract.md`
  - Use template: `templates/abstracts/abstract-template.md`

## 4. Draft Claims Using H01L Best Practices

### Independent Claims to Draft:

**Device Structure Claim (Required):**
- Semiconductor device comprising substrate, layers, regions, electrodes
- Include novel structural features
- Specify materials, doping, dimensions with ranges
- Example: "A semiconductor device comprising: a substrate comprising [material]..."

**Process Method Claim (Required):**
- Method for fabricating the device
- Sequential process steps with parameters
- Include novel process features
- Example: "A method comprising: providing a substrate; forming a [layer] by [process]..."

**Additional Claims (if applicable):**
- Transistor-specific claim (if applicable)
- Memory cell claim (for memory devices)
- Power device claim (for power devices)
- LED/optoelectronic claim (for light-emitting devices)

### Dependent Claims to Add:

For each independent claim, add 5-10 dependent claims covering:
- Specific materials (e.g., "wherein the dielectric comprises HfO₂")
- Dimensional ranges (e.g., "wherein the thickness is in a range of 5-15 nm")
- Doping specifications (e.g., "wherein the doping concentration is 1×10¹⁶ to 1×10¹⁸ cm⁻³")
- Process parameters (e.g., "wherein the temperature is 400-600°C")
- Alternative embodiments
- Combinations of features

### H01L Claim Requirements:

- **Antecedent Basis**: "a gate electrode" first, "the gate electrode" after
- **Consistent Terminology**: Use terms from `docs/h01l-terminology-reference.md`
- **Reference Numbers**: Assign systematically (100s, 200s, etc.)
- **Proper Relationships**: Use "on", "in", "over", "adjacent to" correctly
- **Ranges**: Use "in a range of X to Y" for dimensional tolerances
- **Material Specificity**: Specify materials or material classes

After drafting claims:
```bash
cd tools && python claim-analyzer.py ../patents/drafts/[invention-name]-h01l-claims.md
```

## 5. Draft Detailed Description

Use the H01L template structure:

**Background Section:**
- State the field: "This invention relates to semiconductor devices..."
- Mention CPC classification: "CPC: H01L [specific subclass]"
- Discuss prior art from priority companies (TSMC, Samsung, Intel, ASE, Amkor)
- Explain limitations and problems

**Summary Section:**
- Technical problem solved
- Novel solution (structure/process)
- Quantified advantages (e.g., "30% reduction in leakage", "2x faster switching")

**Detailed Description:**
- **Reference Numbering System**:
  - 100-199: Substrate and base structures
  - 200-299: Active device regions
  - 300-399: Gate structures and dielectrics
  - 400-499: Source/drain regions and contacts
  - 500-599: Interconnect layers
  - 600-699: Alternative embodiment

- **Layer-by-Layer Description**:
  - Start from substrate, work upward
  - For each layer/region specify:
    - Material (with chemical formula if applicable)
    - Thickness or dimensional range
    - Doping type and concentration (for semiconductors)
    - Formation method
    - Purpose/function

- **Novel Features** (2-3 paragraphs each):
  - Detailed explanation of what makes it novel
  - How it differs from prior art (especially priority companies)
  - Why it provides advantages
  - Supporting data if available

- **Manufacturing Process** (detailed steps):
  - Sequential process description
  - Include process parameters (temperature, pressure, time, gas flows)
  - Specify equipment types where relevant
  - Multiple process flows for alternative embodiments

- **Alternative Embodiments** (at least 2-3):
  - Material alternatives
  - Structural variations
  - Process variations
  - Different applications

- **Device Operation**:
  - How the device works electrically
  - Bias conditions
  - Current flow paths
  - Performance characteristics

## 6. Draft Abstract

Create 50-150 word abstract including:
- Device/method type
- Key structural features
- Novel aspects
- Main advantages
- Applications

Check word count:
```bash
cd tools && python word-count.py ../patents/drafts/[invention-name]-abstract.md
```

## 7. H01L-Specific Quality Checks

- [ ] **Terminology Consistency**: Check against `docs/h01l-terminology-reference.md`
- [ ] **Priority Company Distinction**: Clearly different from TSMC, Samsung, Intel, ASE, Amkor patents
- [ ] **Antecedent Basis**: All claims properly use "a/an" then "the"
- [ ] **Reference Numbers**: Consistent and systematic
- [ ] **Material Specifications**: All materials properly identified
- [ ] **Dimensional Ranges**: Realistic for technology node
- [ ] **Doping Concentrations**: In realistic ranges (10¹⁴-10²¹ cm⁻³)
- [ ] **Process Parameters**: Achievable temperatures, pressures, times
- [ ] **CPC Classification**: Appropriate H01L subclass identified
- [ ] **Claims Support**: Specification provides written description for all claim elements
- [ ] **Enablement**: Sufficient detail for person skilled in art to make and use
- [ ] **Abstract**: ≤150 words
- [ ] **Figures Referenced**: All reference numbers appear in specification

## 8. Prior Art Analysis and Claim Strategy

Based on your prior art search of priority companies:

1. **Novelty Check (35 U.S.C. § 102)**:
   - Is each claim element new vs. TSMC, Samsung, Intel, ASE, Amkor patents?
   - Note: Even one prior art reference with all elements defeats novelty

2. **Obviousness Analysis (35 U.S.C. § 103)**:
   - Would combination of references make invention obvious?
   - Are there unexpected results or advantages?
   - Consider secondary considerations (commercial success, long-felt need)

3. **Claim Strategy**:
   - Independent claims: Broad enough for value, narrow enough to avoid prior art
   - Dependent claims: Fallback positions if independent claims rejected
   - Ensure claims cover commercially important embodiments
   - Consider design-around options and block with dependent claims

## 9. Generate Search Queries for User

Provide user with specific search queries to verify no prior art was missed:

**Priority Company Searches:**
```
assignee:TSMC AND CPC:H01L AND [key feature 1] AND [key feature 2]
assignee:Samsung AND CPC:H01L AND [key feature 1] AND [key feature 2]
assignee:Intel AND CPC:H01L AND [key feature 1] AND [key feature 2]
assignee:ASE AND CPC:H01L AND [key feature 1] AND [key feature 2]
assignee:Amkor AND CPC:H01L AND [key feature 1] AND [key feature 2]
```

**Classification Searches:**
```
CPC:[specific H01L subclass] AND [key features]
```

## 10. Recommend Next Steps

Provide recommendations:

1. **Immediate Actions**:
   - Run claim analyzer tool
   - Check abstract word count
   - Review terminology consistency

2. **Prior Art Search**:
   - Comprehensive search following `docs/h01l-prior-art-search-guide.md`
   - Focus on TSMC, Samsung, Intel, ASE, Amkor
   - Document search strategy and results
   - Create claim charts for closest references

3. **Technical Review**:
   - Verify all process parameters are realistic
   - Check material compatibility
   - Ensure dimensional ranges are achievable
   - Validate performance claims

4. **Legal Review**:
   - Professional patent attorney review (REQUIRED before filing)
   - Office action response strategy
   - International filing strategy (PCT, direct filing)
   - Freedom-to-operate analysis if commercializing

5. **Supporting Materials**:
   - Prepare figures/drawings (required for filing)
   - Generate experimental data if available
   - Consider provisional filing for early priority date

6. **Filing Strategy**:
   - Provisional vs. non-provisional
   - US only vs. international (PCT)
   - Consider competitor filing patterns (TSMC, Samsung, Intel, ASE, Amkor file extensively)

## Important Reminders

- **Priority Companies**: TSMC, ASE, Amkor, Samsung, Intel are the most critical to search
- **Use H01L Templates**: `templates/applications/h01l-semiconductor-template.md` and `templates/claims/h01l-claims-template.md`
- **Consistent Terminology**: Reference `docs/h01l-terminology-reference.md`
- **No Legal Advice**: This is assistance only, not legal advice. Professional patent attorney review required.
- **Confidentiality**: Ensure repository is private for confidential inventions
- **Prior Art**: No guarantee of patentability without professional search

## Quick Reference Files

- H01L Application Template: `templates/applications/h01l-semiconductor-template.md`
- H01L Claims Template: `templates/claims/h01l-claims-template.md`
- H01L Terminology Guide: `docs/h01l-terminology-reference.md`
- H01L Prior Art Search Guide: `docs/h01l-prior-art-search-guide.md`
- General Patent Rules: `CLAUDE.md`
