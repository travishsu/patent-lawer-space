# H01L Semiconductor Patent Support - Quick Start Guide

## Overview

This repository is now enhanced with comprehensive support for H01L (semiconductor devices and electric solid-state devices) patent work. This guide will help you quickly get started with semiconductor patent drafting and analysis.

---

## What's New for H01L

### 1. Specialized Templates

#### H01L Patent Application Template
**Location:** `templates/applications/h01l-semiconductor-template.md`

**Features:**
- Semiconductor-specific structure and sections
- Reference numbering conventions (100s for substrate, 200s for active regions, etc.)
- Layer-by-layer description framework
- Material specifications with proper notation
- Process parameter templates
- CPC classification guidance
- Device operation descriptions
- Multiple embodiment templates

**When to use:** Starting any semiconductor device patent application (transistors, memory, LEDs, power devices, sensors, etc.)

#### H01L Claims Template
**Location:** `templates/claims/h01l-claims-template.md`

**Features:**
- Device structure claim examples (transistors, memory cells, power devices, etc.)
- Manufacturing process claim templates
- Proper antecedent basis examples
- Dimensional range formatting
- Material specification examples
- Doping concentration notation
- Complete FinFET example claim set
- Dependent claim strategies

**When to use:** Drafting claims for any H01L semiconductor patent

### 2. Reference Guides

#### H01L Terminology Reference
**Location:** `docs/h01l-terminology-reference.md`

**Contents:**
- 300+ standardized semiconductor terms
- Substrate types and specifications
- Dielectric materials and properties
- Conductive materials and silicides
- Transistor structures and types
- Fabrication process terminology
- Electrical parameters and units
- Material properties tables
- Common abbreviations
- Best practices for consistent terminology

**When to use:** While drafting to ensure correct and consistent terminology

#### H01L Prior Art Search Guide
**Location:** `docs/h01l-prior-art-search-guide.md`

**Features:**
- **Priority Company Focus:** TSMC, Samsung, Intel, ASE, Amkor
- Detailed search strategies for each priority company
- Technology-specific search queries
- CPC classification quick reference
- Database recommendations
- Search documentation templates
- Common pitfalls to avoid

**When to use:** Before and during patent drafting, for FTO analysis, for patentability assessment

### 3. Slash Command

#### /h01l-draft Command
**Usage:** Type `/h01l-draft` in Claude Code

**What it does:**
- Guides you through semiconductor patent drafting
- Prompts for device-specific information
- Recommends priority company prior art searches
- Creates H01L-specific draft files
- Provides claim drafting guidance
- Generates search queries
- Recommends next steps

**When to use:** Starting a new semiconductor patent application

---

## Quick Start Workflows

### Workflow 1: Draft a New Semiconductor Device Patent

**Step 1: Prepare Your Invention Description**
- Device type (transistor, memory, LED, power device, etc.)
- Key innovative features
- Technical advantages
- Application area

**Step 2: Launch the H01L Drafting Assistant**
```
/h01l-draft
```

**Step 3: Perform Priority Company Prior Art Search**

Focus on these companies first:
1. **TSMC** - Advanced process technology, packaging
2. **Samsung** - Memory, logic, displays
3. **Intel** - Processors, advanced logic
4. **ASE** - Packaging and assembly
5. **Amkor** - Advanced packaging

Use search guide: `docs/h01l-prior-art-search-guide.md`

Example search query:
```
assignee:(TSMC OR Samsung OR Intel OR ASE OR Amkor) AND CPC:H01L AND [your technology keywords]
```

**Step 4: Draft Using H01L Templates**

The `/h01l-draft` command will create files using:
- `templates/applications/h01l-semiconductor-template.md`
- `templates/claims/h01l-claims-template.md`

**Step 5: Ensure Terminology Consistency**

Reference: `docs/h01l-terminology-reference.md`
- Use consistent terms throughout
- Follow standard semiconductor notation
- Use proper units and ranges

**Step 6: Quality Check**
- Run claim analyzer: `cd tools && python claim-analyzer.py ../patents/drafts/[file].md`
- Check abstract length: `cd tools && python word-count.py ../patents/drafts/[file].md`
- Verify against checklist in templates

**Step 7: Professional Review**
- Have patent attorney review
- Verify prior art search is comprehensive
- Confirm patentability
- Prepare for filing

### Workflow 2: Prior Art Search for Semiconductor Technology

**Step 1: Identify Technology Area**
- Transistor structures? → Focus on TSMC, Samsung, Intel
- Packaging? → Focus on ASE, Amkor, TSMC
- Memory? → Focus on Samsung, Micron, SK Hynix
- Power devices? → Include Infineon, ON Semi, STMicro
- Optoelectronics? → Include Nichia, Cree, Samsung

**Step 2: Use Priority Company Searches**

From `docs/h01l-prior-art-search-guide.md`, use templates like:

```
# For transistor structures:
assignee:(TSMC OR Samsung OR Intel) AND CPC:H01L29/78 AND (FinFET OR GAA)

# For packaging:
assignee:(ASE OR Amkor OR TSMC) AND CPC:H01L23/00 AND (fan-out OR FOWLP OR TSV)

# For memory:
assignee:(Samsung OR Micron OR "SK Hynix") AND CPC:H01L27/108 AND (NAND OR DRAM)
```

**Step 3: Expand Search**
- Check CPC classifications
- Keyword variations
- Citation-based searches
- Technical literature (IEDM, VLSI Symposium)

**Step 4: Document Results**

Use template from search guide:
- List all search queries
- Document key patents found
- Note relevance to your invention
- Create claim charts for closest references

### Workflow 3: Analyze Patentability

**Step 1: Comprehensive Prior Art Search**
Follow Workflow 2 above, focusing on priority companies

**Step 2: Element-by-Element Comparison**

For each of your claims:
1. List each claim element
2. Find corresponding disclosure in closest prior art
3. Identify elements NOT in prior art (novelty)
4. Consider combinations (obviousness)

**Step 3: Use Analysis Templates**

From main templates:
- `templates/analysis/patentability-analysis.md`
- `templates/analysis/prior-art-analysis.md`

**Step 4: Assess Under Patent Law**
- **35 U.S.C. § 101**: Patent-eligible subject matter
- **35 U.S.C. § 102**: Novelty (no single prior art has all elements)
- **35 U.S.C. § 103**: Non-obviousness (combinations)
- **35 U.S.C. § 112**: Written description, enablement, definiteness

**Step 5: Develop Claim Strategy**
- Broad independent claims that avoid prior art
- Dependent claims as fallback positions
- Alternative claim sets
- Cover commercial embodiments

---

## Technology-Specific Quick References

### For Advanced Logic (FinFET, GAA, etc.)

**Priority Companies:** TSMC, Samsung, Intel

**Key Search Terms:**
- FinFET, fin structure, multi-gate, tri-gate
- GAA, GAAFET, gate-all-around, nanosheet, nanowire
- source/drain epitaxy, raised source/drain
- high-k metal gate (HKMG)

**CPC Classes:** H01L 29/785, H01L 29/792, H01L 21/823

**Templates:**
- Use FinFET example in `templates/claims/h01l-claims-template.md`
- See transistor sections in `templates/applications/h01l-semiconductor-template.md`

### For Packaging Technologies

**Priority Companies:** ASE, Amkor, TSMC

**Key Search Terms:**
- fan-out, FOWLP, fan-out wafer-level packaging
- TSV, through-silicon via
- SiP, system in package
- redistribution layer (RDL)
- CoWoS, InFO (TSMC-specific)

**CPC Classes:** H01L 23/00, H01L 25/00, H01L 21/56

**Templates:**
- See packaging sections in H01L templates
- Focus on 3D structures and interconnects

### For Memory Devices

**Priority Companies:** Samsung, Micron, SK Hynix

**Key Search Terms:**
- 3D NAND, vertical NAND, VNAND
- DRAM, storage capacitor, vertical transistor
- word line, bit line, string select line
- charge trap, floating gate

**CPC Classes:** H01L 27/108 (DRAM), H01L 27/1085 (NAND)

**Templates:**
- See memory cell examples in claims template
- Focus on vertical structures and capacitors

### For Power Devices

**Priority Companies:** Infineon, ON Semiconductor, STMicroelectronics

**Key Search Terms:**
- IGBT, LDMOS, VDMOS, superjunction
- trench gate, drift region
- breakdown voltage, on-resistance
- SiC, GaN (wide bandgap materials)

**CPC Classes:** H01L 29/7806, H01L 29/66

**Templates:**
- See power device examples in claims template
- Focus on drift regions and breakdown voltage

### For Optoelectronics (LEDs)

**Priority Companies:** Samsung, Nichia, Cree, Osram

**Key Search Terms:**
- LED, light-emitting diode
- GaN, InGaN, AlGaN
- quantum well, active region
- current spreading, p-contact, n-contact

**CPC Classes:** H01L 33/00

**Templates:**
- See LED examples in claims template
- Focus on active region and III-V materials

---

## Best Practices for H01L Patents

### 1. Terminology Consistency
**Rule:** Once you define a term, use it consistently throughout

✓ **Good:**
- Specification: "The gate electrode (108) comprises..."
- Claims: "...the gate electrode..."
- Everywhere: "gate electrode"

✗ **Bad:**
- Mixing: "gate electrode", "gate conductor", "gate terminal"

**Reference:** `docs/h01l-terminology-reference.md`

### 2. Prioritize Company Searches

**Always search these five companies first:**
1. TSMC
2. Samsung
3. Intel
4. ASE
5. Amkor

**Why:** These companies dominate semiconductor patents and represent the most relevant prior art

### 3. Use Dimensional Ranges

✓ **Good:** "thickness in a range of 5 nm to 15 nm"

✗ **Bad:** "thickness of approximately 10 nm"

**Why:** Ranges allow manufacturing tolerance and broader claim scope

### 4. Specify Materials Properly

✓ **Good:**
- "high-k dielectric comprising hafnium oxide (HfO₂)"
- "gate electrode comprising a metal selected from titanium nitride, tantalum nitride, and tungsten"

✗ **Bad:**
- "insulating material"
- "metal"

**Why:** Specificity is required for enablement but still allows alternatives

### 5. Include Process Parameters

✓ **Good:** "depositing by atomic layer deposition at a temperature in a range of 250°C to 400°C"

✗ **Bad:** "depositing at a suitable temperature"

**Why:** Enablement requirement under 35 U.S.C. § 112(a)

### 6. Reference Numbers

**System:**
- 100-199: Substrate and base
- 200-299: Active regions
- 300-399: Gate structures
- 400-499: Source/drain
- 500-599: Interconnects
- 600-699: Alternative embodiments

**Why:** Systematic numbering aids clarity and examination

---

## Common Mistakes to Avoid

### ❌ Not Searching Priority Companies
**Problem:** Missing critical prior art from TSMC, Samsung, Intel, ASE, Amkor

**Solution:** Always start with priority company searches

### ❌ Inconsistent Terminology
**Problem:** Using "substrate", "wafer", "base" interchangeably

**Solution:** Pick one term and use consistently; reference terminology guide

### ❌ Vague Claim Language
**Problem:** "thin layer", "small dimension", "high doping"

**Solution:** Use specific ranges: "thickness less than 50 nm", "doping concentration greater than 1×10¹⁹ cm⁻³"

### ❌ Missing Antecedent Basis
**Problem:** Introducing "the gate electrode" without first using "a gate electrode"

**Solution:** Always use "a/an" for first mention, "the" for subsequent

### ❌ Inadequate Prior Art Search
**Problem:** Searching only keywords, missing classification-based patents

**Solution:** Use combination of keyword, assignee, and CPC classification searches

### ❌ Overclaiming
**Problem:** Claiming results without supporting structure

**Solution:** Tie performance claims to specific structures

---

## File Organization

```
patent-lawer-space/
├── templates/
│   ├── applications/
│   │   ├── utility-patent-template.md
│   │   └── h01l-semiconductor-template.md        ← NEW: H01L-specific
│   └── claims/
│       ├── claims-template.md
│       └── h01l-claims-template.md               ← NEW: H01L-specific
├── docs/
│   ├── getting-started.md
│   ├── h01l-quick-start.md                       ← NEW: This guide
│   ├── h01l-terminology-reference.md             ← NEW: Terminology
│   └── h01l-prior-art-search-guide.md            ← NEW: Search guide
└── .claude/
    └── commands/
        ├── draft-patent.md
        └── h01l-draft.md                          ← NEW: H01L command
```

---

## Resources and Next Steps

### Internal Resources
1. **H01L Templates:**
   - `templates/applications/h01l-semiconductor-template.md`
   - `templates/claims/h01l-claims-template.md`

2. **H01L Guides:**
   - `docs/h01l-terminology-reference.md`
   - `docs/h01l-prior-art-search-guide.md`
   - `docs/h01l-quick-start.md` (this file)

3. **Commands:**
   - `/h01l-draft` - Start H01L patent drafting
   - `/draft-patent` - General patent drafting
   - `/prior-art` - Prior art search
   - `/patentability` - Patentability analysis

### External Resources

**Patent Databases:**
- Google Patents: https://patents.google.com
- USPTO: https://www.uspto.gov/patents/search
- Espacenet: https://worldwide.espacenet.com
- Lens.org: https://www.lens.org

**Technical Conferences:**
- IEDM (International Electron Devices Meeting)
- VLSI Technology Symposium
- ISSCC (International Solid-State Circuits Conference)
- ECTC (Electronic Components and Technology Conference)

**CPC Classification:**
- CPC Browser: https://www.cooperativepatentclassification.org

### Getting Help

1. **For H01L-specific questions:**
   - Use `/h01l-draft` command
   - Reference the terminology guide
   - Check the prior art search guide

2. **For general patent questions:**
   - See `CLAUDE.md` for overall rules
   - Use other slash commands (`/patentability`, `/prior-art`, etc.)
   - Reference general templates

3. **For specific company searches:**
   - See priority company sections in `docs/h01l-prior-art-search-guide.md`
   - Use provided search query templates
   - Check company-specific tips

---

## Priority Company Contact Points

### TSMC
- **Focus:** Advanced process nodes, 3D IC, advanced packaging
- **Key Technologies:** FinFET, GAA, CoWoS, InFO, SOIC
- **Search Tip:** Check both process and packaging patents

### Samsung
- **Focus:** Memory (DRAM, NAND), logic, displays
- **Key Technologies:** 3D NAND, GAA, OLED
- **Search Tip:** Check Samsung Electronics and Samsung Display separately

### Intel
- **Focus:** Processors, advanced logic, packaging
- **Key Technologies:** RibbonFET (GAA), PowerVia, Foveros, EMIB
- **Search Tip:** Look for architecture innovations beyond just process

### ASE (Advanced Semiconductor Engineering)
- **Focus:** Packaging, assembly, test
- **Key Technologies:** FOWLP, SiP, TSV, 2.5D/3D packaging
- **Search Tip:** Include SPIL (now part of ASE) in searches

### Amkor
- **Focus:** Advanced packaging
- **Key Technologies:** SWIFT, SLIM, panel-level packaging, SiP
- **Search Tip:** Focus on wafer-level and panel-level packaging innovations

---

## Checklist: Before Filing H01L Patent

- [ ] Comprehensive prior art search completed
- [ ] All five priority companies searched (TSMC, Samsung, Intel, ASE, Amkor)
- [ ] Additional relevant companies searched based on technology
- [ ] Terminology consistent throughout (checked against terminology guide)
- [ ] Claims have proper antecedent basis
- [ ] Reference numbers systematic and consistent
- [ ] Dimensional ranges are realistic for technology node
- [ ] Doping concentrations in appropriate ranges
- [ ] Process parameters are achievable
- [ ] Materials properly specified
- [ ] CPC classification identified
- [ ] Claims analyzer run (no errors)
- [ ] Abstract ≤150 words (word count verified)
- [ ] Specification supports all claim limitations
- [ ] Multiple embodiments described
- [ ] Figures prepared and referenced
- [ ] Professional patent attorney review scheduled
- [ ] Filing strategy determined (provisional, non-provisional, PCT)
- [ ] Confidentiality verified (private repository for confidential work)

---

## FAQ

**Q: Do I always need to search TSMC, Samsung, Intel, ASE, and Amkor?**
A: For H01L semiconductor patents, yes. These companies dominate the field and represent the most critical prior art sources.

**Q: Can I use the general patent templates instead of H01L-specific ones?**
A: You can, but the H01L templates provide semiconductor-specific guidance that will result in better patents.

**Q: How detailed should my process parameters be?**
A: Detailed enough for enablement. Include temperature ranges, pressures, times, and materials. See examples in H01L template.

**Q: What if my invention is packaging-related?**
A: Focus heavily on ASE and Amkor, also check TSMC. Use packaging-specific search queries from the search guide.

**Q: Should I include performance data in my patent?**
A: If available, yes. It strengthens the application and can help with non-obviousness arguments.

**Q: How many embodiments should I describe?**
A: At least 2-3 alternative embodiments to show breadth and support broader claims.

---

**Last Updated:** 2026-01-04
**Version:** 1.0
**Priority Companies:** TSMC, ASE, Amkor, Samsung, Intel

**Ready to start? Type `/h01l-draft` to begin drafting your semiconductor patent!**
