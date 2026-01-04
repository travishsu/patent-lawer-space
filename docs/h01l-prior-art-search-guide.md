# H01L Prior Art Search Guide

## Overview

This guide provides search strategies specifically for H01L (semiconductor devices and electric solid-state devices) prior art searches. Effective prior art searches are critical for patentability analysis, freedom-to-operate assessments, and drafting strong patent applications.

---

## Priority Companies to Search

### Tier 1: MUST SEARCH - Critical Semiconductor Leaders

These companies represent the most important sources of H01L prior art and should be searched first and most thoroughly:

#### **1. TSMC (Taiwan Semiconductor Manufacturing Company)**
- **Focus Areas:** Advanced process nodes, FinFET, GAA transistors, 3D integration, packaging
- **Assignee Search Terms:**
  - "Taiwan Semiconductor Manufacturing"
  - "TSMC"
  - Assignee code: (varies by jurisdiction)
- **Key Technology Areas:**
  - 7nm, 5nm, 3nm, 2nm process technology
  - EUV lithography implementations
  - 3D IC stacking
  - CoWoS (Chip-on-Wafer-on-Substrate)
  - InFO (Integrated Fan-Out) packaging
- **Search Priority:** HIGHEST
- **Typical Volume:** 2,000+ patents/year

#### **2. Samsung (Samsung Electronics)**
- **Focus Areas:** Memory (DRAM, NAND), logic, advanced nodes, display
- **Assignee Search Terms:**
  - "Samsung Electronics"
  - "Samsung SDI"
  - "Samsung Display"
- **Key Technology Areas:**
  - 3D NAND flash memory
  - DRAM structures
  - FinFET and GAA FET
  - OLED displays
  - Advanced packaging
- **Search Priority:** HIGHEST
- **Typical Volume:** 5,000+ patents/year

#### **3. Intel Corporation**
- **Focus Areas:** Advanced logic, processors, memory, packaging
- **Assignee Search Terms:**
  - "Intel Corporation"
  - "Intel Corp"
- **Key Technology Areas:**
  - RibbonFET (GAA)
  - PowerVia (backside power delivery)
  - Foveros (3D stacking)
  - High-k metal gate
  - Embedded multi-die interconnect bridge (EMIB)
- **Search Priority:** HIGHEST
- **Typical Volume:** 3,000+ patents/year

#### **4. ASE Technology (Advanced Semiconductor Engineering)**
- **Focus Areas:** Packaging, assembly, test
- **Assignee Search Terms:**
  - "ASE Technology"
  - "Advanced Semiconductor Engineering"
  - "ASE Group"
  - "SPIL" (Siliconware Precision Industries, now part of ASE)
- **Key Technology Areas:**
  - Fan-out wafer-level packaging (FOWLP)
  - System-in-Package (SiP)
  - Through-silicon via (TSV)
  - 2.5D and 3D packaging
  - Flip-chip packaging
- **Search Priority:** HIGHEST
- **Typical Volume:** 500+ patents/year

#### **5. Amkor Technology**
- **Focus Areas:** Advanced packaging and test
- **Assignee Search Terms:**
  - "Amkor Technology"
  - "Amkor Tech"
- **Key Technology Areas:**
  - Wafer-level packaging
  - Panel-level packaging
  - SiP (System-in-Package)
  - SLIM (Substrate-Less Integrated Module)
  - SWIFT (Scalable Wafer-level Integrated Fan-out Technology)
- **Search Priority:** HIGHEST
- **Typical Volume:** 200+ patents/year

### Tier 2: High Priority Companies

Also important for comprehensive searches:

- **Micron Technology** - Memory devices (DRAM, NAND)
- **SK Hynix** - Memory devices
- **GlobalFoundries** - Foundry services, specialty processes
- **UMC (United Microelectronics)** - Foundry services
- **STMicroelectronics** - Wide range of semiconductors
- **Texas Instruments** - Analog and embedded processing
- **Qualcomm** - Mobile SoC, RF devices
- **NVIDIA** - GPU, AI processors
- **AMD** - Processors, GPUs
- **NXP Semiconductors** - Automotive, IoT

### Tier 3: Specialized Companies

Important for specific technology areas:

- **Applied Materials** - Process equipment (influences device structure)
- **Lam Research** - Etch and deposition equipment
- **Tokyo Electron (TEL)** - Process equipment
- **ASML** - Lithography equipment
- **KLA** - Process control equipment
- **Infineon** - Power semiconductors, automotive
- **ON Semiconductor** - Power devices, imaging
- **Analog Devices** - Analog and mixed-signal
- **Broadcom** - Communication chips
- **Renesas** - Automotive, MCUs

---

## Search Databases and Resources

### Primary Patent Databases

1. **Google Patents** (patents.google.com)
   - Free, comprehensive coverage
   - Good for initial searches
   - Excellent assignee filtering
   - Prior art finder feature

2. **USPTO PatFT/AppFT**
   - Official US database
   - Full-text search of US patents
   - Good for precise searches

3. **Espacenet** (worldwide.espacenet.com)
   - European Patent Office database
   - International coverage
   - Good classification search

4. **Lens.org**
   - Free comprehensive patent database
   - Excellent for assignee analysis
   - Citation analysis tools

5. **WIPO PatentScope**
   - International (PCT) applications
   - Good for early-stage disclosures

### Commercial Databases (if available)

- **Questel Orbit**
- **PatBase**
- **Derwent Innovation**
- **TotalPatent**

### Technical Literature Databases

1. **IEEE Xplore** - Conference papers (IEDM, VLSI Symposium, etc.)
2. **Google Scholar** - Academic publications
3. **ResearchGate** - Research papers
4. **ArXiv** - Pre-prints

---

## Search Strategy Framework

### Phase 1: Assignee-Focused Search (Priority Companies)

**Step 1: Priority Tier 1 Companies**
Search each of the five priority companies:

```
Example Search Query (Google Patents):
assignee:(TSMC OR "Taiwan Semiconductor Manufacturing") AND CPC:H01L
assignee:(Samsung Electronics) AND CPC:H01L
assignee:(Intel Corporation) AND CPC:H01L
assignee:(ASE Technology OR "Advanced Semiconductor Engineering") AND CPC:H01L
assignee:(Amkor Technology) AND CPC:H01L
```

**Step 2: Narrow by Technology**
Add keywords specific to your invention:

```
assignee:TSMC AND CPC:H01L AND (FinFET OR "fin structure" OR "multi-gate")
assignee:Samsung AND CPC:H01L AND (NAND OR "3D memory" OR "vertical channel")
assignee:Intel AND CPC:H01L AND ("gate stack" OR "high-k metal gate" OR HKMG)
assignee:ASE AND CPC:H01L AND (packaging OR "fan-out" OR FOWLP OR TSV)
assignee:Amkor AND CPC:H01L AND (SiP OR "system in package" OR "wafer level")
```

**Step 3: Date Filtering**
Focus on recent patents for current state of art:

```
assignee:TSMC AND CPC:H01L AND [your keywords] AND filing date:>2018
```

### Phase 2: Keyword-Based Search

**Step 1: Core Technology Keywords**
Identify 5-10 core technical terms from your invention:

```
Example for gate dielectric innovation:
("gate dielectric" OR "gate oxide" OR "gate insulator") AND
(high-k OR "hafnium oxide" OR HfO2) AND
("interface layer" OR "interfacial oxide") AND
CPC:H01L29/66
```

**Step 2: Process Keywords (if applicable)**
For manufacturing processes:

```
("atomic layer deposition" OR ALD) AND
("gate dielectric" OR "high-k") AND
(temperature OR anneal OR "post-deposition") AND
CPC:H01L21/02
```

**Step 3: Structure Keywords**
For device structures:

```
(transistor OR MOSFET OR FinFET) AND
("source region" OR "drain region") AND
("gate electrode" OR "gate stack") AND
[novel feature keywords] AND
CPC:H01L29/78
```

### Phase 3: CPC Classification Search

**Step 1: Identify Relevant CPC Codes**

Key H01L subclasses:

| CPC Code | Technology Area |
|----------|-----------------|
| **H01L 21/02** | Manufacture - deposition, epitaxy |
| **H01L 21/04** | Manufacture - masking, etching |
| **H01L 21/18** | Manufacture - diffusion, implantation |
| **H01L 21/28** | Manufacture - contacts, electrodes |
| **H01L 21/3065** | Manufacture - CVD |
| **H01L 21/768** | Manufacture - interconnects |
| **H01L 21/82** | Manufacture - specific devices |
| **H01L 23/00** | Details of semiconductor devices |
| **H01L 23/48** | Details - leads, contacts |
| **H01L 23/538** | Details - passivation |
| **H01L 25/00** | Assemblies of multiple components |
| **H01L 27/06** | Multiple components - Si devices |
| **H01L 27/088** | Multiple components - memory |
| **H01L 29/40** | Electrodes |
| **H01L 29/41** | Gate electrodes |
| **H01L 29/43** | Source/drain electrodes |
| **H01L 29/49** | Barrier or field effect devices |
| **H01L 29/51** | Bulk devices |
| **H01L 29/66** | Types of semiconductor devices |
| **H01L 29/78** | Field effect transistors |
| **H01L 29/786** | Thin film transistors |
| **H01L 29/792** | MOS transistors |

**Step 2: Search by CPC + Assignee**

```
CPC:H01L29/792 AND assignee:(TSMC OR Samsung OR Intel OR ASE OR Amkor)
```

**Step 3: Expand to Related Classes**

```
(CPC:H01L29/792 OR CPC:H01L29/78 OR CPC:H01L29/66) AND [keywords]
```

### Phase 4: Citation-Based Search

**Step 1: Find Key Patents**
Identify 2-3 highly relevant patents from priority companies

**Step 2: Forward Citations**
Find patents that cite these key patents (Google Patents "Cited by" tab)

**Step 3: Backward Citations**
Review patents cited by these key patents (Google Patents "Prior art" tab)

**Step 4: Family Members**
Check international family members for additional disclosures

---

## Technology-Specific Search Strategies

### For Transistor Structures (FinFET, GAA, etc.)

**Priority Companies:** TSMC, Samsung, Intel

**Search Query Template:**
```
assignee:(TSMC OR Samsung OR Intel) AND
CPC:H01L29/785 AND
(FinFET OR "fin field effect" OR "tri-gate" OR GAA OR
 "gate all around" OR nanosheet OR nanowire OR GAAFET) AND
[specific feature keywords]
```

**Key Terms:**
- fin structure, fin width, fin height
- multi-gate, tri-gate, gate-all-around
- nanosheet, nanowire, ribbon
- source/drain epitaxy, raised source/drain
- strain engineering, SiGe source/drain

### For Packaging Technologies

**Priority Companies:** ASE, Amkor, TSMC

**Search Query Template:**
```
assignee:(ASE OR Amkor OR TSMC OR "Taiwan Semiconductor") AND
(CPC:H01L23/00 OR CPC:H01L25/00 OR CPC:H01L21/56) AND
(packaging OR "fan-out" OR FOWLP OR "wafer level" OR
 "chip stacking" OR TSV OR "through silicon via" OR
 SiP OR "system in package" OR CoWoS OR InFO) AND
[specific feature keywords]
```

**Key Terms:**
- fan-out wafer-level packaging (FOWLP)
- panel-level packaging
- through-silicon via (TSV)
- redistribution layer (RDL)
- bump, pillar, micro-bump
- underfill, molding compound
- interposer, silicon interposer

### For Memory Devices

**Priority Companies:** Samsung, Micron, SK Hynix

**Search Query Template:**
```
assignee:(Samsung OR Micron OR "SK Hynix") AND
CPC:H01L27/1085 AND
(NAND OR "3D NAND" OR "vertical NAND" OR VNAND OR
 "charge trap" OR "floating gate" OR
 "word line" OR "bit line" OR "channel hole") AND
[specific feature keywords]
```

**For DRAM:**
```
assignee:(Samsung OR Micron OR "SK Hynix") AND
CPC:H01L27/108 AND
(DRAM OR "dynamic random access" OR
 "storage capacitor" OR "cell capacitor" OR
 "buried word line" OR "vertical transistor") AND
[specific feature keywords]
```

### For Power Devices

**Priority Companies:** Infineon, ON Semiconductor, STMicroelectronics

**Search Query Template:**
```
assignee:(Infineon OR "ON Semiconductor" OR STMicroelectronics) AND
CPC:H01L29/7806 AND
(power OR IGBT OR LDMOS OR "trench gate" OR
 "superjunction" OR "drift region" OR
 "breakdown voltage" OR "on-resistance") AND
[specific feature keywords]
```

### For Optoelectronics (LEDs, etc.)

**Priority Companies:** Samsung, Nichia, Cree, Osram

**Search Query Template:**
```
assignee:(Samsung OR Nichia OR Cree OR Osram) AND
CPC:H01L33/00 AND
(LED OR "light emitting" OR GaN OR InGaN OR AlGaN OR
 "quantum well" OR "active region" OR
 "p-contact" OR "n-contact" OR "current spreading") AND
[specific feature keywords]
```

---

## Advanced Search Techniques

### Boolean Operators

- **AND** - Both terms must appear
- **OR** - Either term can appear
- **NOT** - Exclude term
- **Parentheses** - Group terms

```
(TSMC OR Samsung) AND (FinFET OR GAA) NOT planar
```

### Proximity Operators (database-specific)

- **NEAR/n** - Terms within n words
- **ADJ** - Terms adjacent

```
gate NEAR/5 dielectric
high-k ADJ metal
```

### Wildcards

- **\*** - Multiple characters
- **?** - Single character

```
transistor* → transistor, transistors
fin?et → FinFET, finFET
```

### Phrase Searching

Use quotes for exact phrases:
```
"gate-all-around transistor"
"through-silicon via"
```

---

## Priority Company Patent Portfolios - Quick Reference

### TSMC Patent Characteristics
- **Strong in:** Advanced nodes, process integration, packaging
- **Filing Strategy:** Broad coverage with many continuations
- **Key Inventors to Watch:** C. H. Yu, M. H. Tsai, C. H. Wang
- **Typical Claims:** Detailed process flows, specific dimensional ranges
- **Search Tip:** Check for CoWoS and InFO related patents for packaging

### Samsung Patent Characteristics
- **Strong in:** Memory, displays, advanced logic
- **Filing Strategy:** High volume, incremental improvements
- **Key Divisions:** Samsung Electronics, Samsung Display
- **Typical Claims:** Memory structures, layered devices
- **Search Tip:** Check both Korean and US filings for completeness

### Intel Patent Characteristics
- **Strong in:** Logic devices, processors, novel architectures
- **Filing Strategy:** Strategic patents with broad claims
- **Key Inventors to Watch:** R. Chau, M. Bohr, S. Natarajan
- **Typical Claims:** Novel device structures, integration schemes
- **Search Tip:** Look for RibbonFET (GAA) and Foveros (3D) patents

### ASE Patent Characteristics
- **Strong in:** Packaging assembly, testing
- **Filing Strategy:** Focus on manufacturing processes
- **Typical Claims:** Process steps, equipment configurations
- **Search Tip:** Include SPIL (now part of ASE) in searches
- **Key Technologies:** FOWLP, SiP, TSV

### Amkor Patent Characteristics
- **Strong in:** Advanced packaging, wafer-level packaging
- **Filing Strategy:** Focus on packaging innovations
- **Typical Claims:** Package structures, interconnect methods
- **Search Tip:** Check for SWIFT and SLIM technology patents
- **Key Technologies:** Panel-level packaging, SiP

---

## Search Documentation Template

Document your search thoroughly:

```markdown
## H01L Prior Art Search Report

**Date:** [Date]
**Invention:** [Brief description]
**Searcher:** [Name]

### Search Strategy

**Priority Company Searches:**
1. TSMC: [Query] - [Results count] - [Key patents found]
2. Samsung: [Query] - [Results count] - [Key patents found]
3. Intel: [Query] - [Results count] - [Key patents found]
4. ASE: [Query] - [Results count] - [Key patents found]
5. Amkor: [Query] - [Results count] - [Key patents found]

**Keyword Searches:**
1. [Query 1] - [Database] - [Results count]
2. [Query 2] - [Database] - [Results count]
...

**CPC Classification Searches:**
1. [CPC code] + [keywords] - [Results count]
...

### Key Prior Art References

**Most Relevant (5-10 references):**
1. [Patent Number] - [Assignee] - [Title] - [Relevance]
2. [Patent Number] - [Assignee] - [Title] - [Relevance]
...

**Potentially Relevant (10-20 references):**
...

### Technical Literature
1. [Citation] - [Relevance]
...

### Analysis
[Element-by-element comparison with key prior art]

### Conclusion
[Novelty assessment and recommended claim strategy]
```

---

## Common H01L Search Pitfalls

1. **Not Searching Priority Companies First**
   - Always check TSMC, Samsung, Intel, ASE, Amkor before broader searches

2. **Using Only Keywords**
   - Must also search by CPC classification

3. **Ignoring Process Patents**
   - Manufacturing process patents can impact device structure claims

4. **Missing Equipment Patents**
   - Applied Materials, Lam, TEL patents reveal device structures

5. **Not Checking Continuations**
   - Priority companies file many continuations with evolving claims

6. **Ignoring Non-Patent Literature**
   - IEDM, VLSI Symposium papers often disclose before patents

7. **Missing International Filings**
   - Check PCT, EP, JP, KR, CN applications

8. **Overlooking Acquired Companies**
   - ASE acquired SPIL, Intel acquired Altera, etc.

---

## Quick Search Checklist

Before completing H01L prior art search:

- [ ] Searched all Tier 1 priority companies (TSMC, Samsung, Intel, ASE, Amkor)
- [ ] Searched relevant Tier 2 companies based on technology
- [ ] Performed keyword searches in multiple databases
- [ ] Searched by relevant CPC classifications
- [ ] Checked technical literature (IEDM, VLSI Symposium)
- [ ] Performed citation-based searches on key patents
- [ ] Documented all search queries and results
- [ ] Created element-by-element comparison with closest prior art
- [ ] Identified differences from prior art
- [ ] Assessed patentability under 35 U.S.C. § 102, 103

---

## Resources and Links

**Patent Databases:**
- Google Patents: https://patents.google.com
- USPTO: https://www.uspto.gov/patents/search
- Espacenet: https://worldwide.espacenet.com
- Lens.org: https://www.lens.org
- WIPO PatentScope: https://patentscope.wipo.int

**CPC Classification:**
- CPC Browser: https://www.cooperativepatentclassification.org

**Technical Conferences:**
- IEDM (International Electron Devices Meeting)
- VLSI Technology Symposium
- ISSCC (International Solid-State Circuits Conference)
- ECTC (Electronic Components and Technology Conference) - for packaging

**Company Patent Pages:**
- TSMC: Search by assignee in patent databases
- Samsung: www.samsung.com (IP section)
- Intel: www.intel.com/patents
- ASE: www.aseglobal.com
- Amkor: www.amkor.com

---

**Last Updated:** 2026-01-04
**Version:** 1.0
**Priority Companies:** TSMC, ASE, Amkor, Samsung, Intel
