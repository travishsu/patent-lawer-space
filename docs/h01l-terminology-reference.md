# H01L Semiconductor Terminology Reference Guide

## Introduction

This guide provides standardized terminology for drafting H01L semiconductor device patent applications. Consistent use of these terms is critical for clarity, patentability, and avoiding rejections.

**Key Principle:** Once a term is defined in a patent application, use it consistently throughout. Do not alternate between synonyms (e.g., don't switch between "substrate" and "wafer").

---

## A. Substrate and Base Materials

### Substrate Types

| Term | Definition | When to Use |
|------|------------|-------------|
| **substrate** | The base semiconductor wafer on which devices are built | Generic term for any starting wafer |
| **semiconductor substrate** | Substrate made of semiconductor material | When emphasizing semiconductor properties |
| **silicon substrate** | Substrate comprising single-crystal or polycrystalline silicon | When specifically silicon |
| **SOI substrate** | Silicon-on-insulator substrate with buried oxide | When using SOI technology |
| **compound semiconductor substrate** | Substrate of III-V or II-VI materials | For GaAs, GaN, InP, etc. |
| **handle wafer** | Supporting substrate in bonded wafer structures | In wafer bonding contexts |

### Crystal Properties

| Term | Definition | Typical Usage |
|------|------------|---------------|
| **crystal orientation** | Direction of crystal plane (e.g., (100), (111)) | "silicon substrate having a (100) crystal orientation" |
| **single-crystal** | Continuous crystal lattice throughout | "single-crystal silicon" |
| **polycrystalline** | Multiple crystal grains | "polycrystalline silicon gate electrode" |
| **amorphous** | No long-range crystal order | "amorphous silicon layer" |
| **epitaxial layer** | Single-crystal layer grown with specific orientation | "epitaxial layer formed on the substrate" |

### Conductivity and Doping

| Term | Standard Format | Example |
|------|----------------|---------|
| **n-type** | Electron-majority semiconductor | "n-type silicon substrate" |
| **p-type** | Hole-majority semiconductor | "p-type silicon substrate" |
| **intrinsic** | Undoped semiconductor | "intrinsic silicon region" |
| **doping concentration** | Number of dopant atoms per cm³ | "doping concentration of 1×10¹⁶ cm⁻³" |
| **resistivity** | Electrical resistivity in Ω-cm | "resistivity in a range of 1 to 10 Ω-cm" |

**Common Doping Concentration Ranges:**
- Highly doped (n⁺ or p⁺): 10¹⁹ - 10²¹ cm⁻³
- Moderately doped: 10¹⁶ - 10¹⁸ cm⁻³
- Lightly doped (n⁻ or p⁻): 10¹⁴ - 10¹⁶ cm⁻³
- Very lightly doped: < 10¹⁴ cm⁻³

---

## B. Semiconductor Regions and Structures

### Active Device Regions

| Term | Definition | Typical Context |
|------|------------|-----------------|
| **well region** | Doped region for transistor formation | "n-well region", "p-well region" |
| **channel region** | Region where current flows in FET | "channel region between source and drain" |
| **drift region** | Lightly doped region in power devices | "drift region for voltage blocking" |
| **body region** | Bulk semiconductor region | Often in power MOSFETs |
| **depletion region** | Region depleted of mobile carriers | "depletion region at the p-n junction" |

### Source/Drain Terminology

| Term | When to Use | Notes |
|------|-------------|-------|
| **source region** | In FET structures | Carrier source |
| **drain region** | In FET structures | Carrier collection |
| **source/drain regions** | When referring to both collectively | Common in symmetric structures |
| **source/drain extension** | Shallow doped regions for short channel control | Also called LDD |
| **lightly doped drain (LDD)** | Extension regions with lighter doping | Reduces hot carrier effects |

### BJT Terminology

| Term | Definition |
|------|------------|
| **emitter region** | Region where carriers are injected |
| **base region** | Thin region controlling current flow |
| **collector region** | Region where carriers are collected |

---

## C. Dielectric Materials and Layers

### Generic Dielectric Terms

| Term | Definition | Usage |
|------|------------|-------|
| **dielectric layer** | Insulating layer | Generic term |
| **insulating layer** | Same as dielectric layer | Use interchangeably with dielectric |
| **oxide layer** | Layer of oxide material | When specifically oxide |
| **nitride layer** | Layer of nitride material | When specifically nitride |

### Gate Dielectrics

| Term | Material | Properties |
|------|----------|------------|
| **gate oxide** | Traditionally SiO₂ | k ≈ 3.9 |
| **gate dielectric** | Any gate insulator | Preferred generic term |
| **thermal oxide** | Thermally grown SiO₂ | "thermal oxide formed at 900°C" |
| **high-k dielectric** | High dielectric constant material | k > 7; HfO₂, Al₂O₃, ZrO₂ |
| **low-k dielectric** | Low dielectric constant material | k < 3.0; for interconnect |
| **interfacial layer** | Thin layer between Si and high-k | Often SiO₂ or SiOₓNᵧ |
| **equivalent oxide thickness (EOT)** | Effective thickness in SiO₂ units | "EOT less than 1 nm" |

### Specific Dielectric Materials

| Material | Chemical Formula | Dielectric Constant | Common Uses |
|----------|------------------|---------------------|-------------|
| Silicon dioxide | SiO₂ | 3.9 | Gate oxide, isolation |
| Silicon nitride | Si₃N₄ | 7.5 | Spacers, etch stop, passivation |
| Silicon oxynitride | SiOₓNᵧ | 4-7 | Gate dielectric |
| Hafnium oxide | HfO₂ | 20-25 | High-k gate dielectric |
| Aluminum oxide | Al₂O₃ | 9 | High-k gate dielectric |
| Zirconium oxide | ZrO₂ | 25 | High-k gate dielectric |
| Tantalum oxide | Ta₂O₅ | 26 | Capacitor dielectric |

---

## D. Conductive Materials and Layers

### Gate Electrodes

| Term | Composition | When to Use |
|------|-------------|-------------|
| **gate electrode** | Generic conductive gate | Preferred general term |
| **polysilicon gate** | Doped polycrystalline silicon | Traditional gate material |
| **poly-Si gate** | Abbreviation for polysilicon | Same as polysilicon gate |
| **metal gate** | Metal or metal compound gate | Modern replacement for poly-Si |
| **work function metal** | Metal selected for specific work function | In metal gate stacks |

### Metal Materials

| Material | Formula/Type | Work Function (eV) | Common Uses |
|----------|--------------|-------------------|-------------|
| Aluminum | Al | 4.1 | Interconnect (older tech) |
| Copper | Cu | 4.65 | Interconnect (modern) |
| Tungsten | W | 4.5-5.0 | Contacts, vias, gates |
| Titanium nitride | TiN | 4.6 | Barrier, gate electrode |
| Tantalum nitride | TaN | 4.7 | Barrier, gate electrode |
| Titanium | Ti | 4.3 | Adhesion layer |
| Tantalum | Ta | 4.25 | Barrier layer |

### Silicides

| Term | Formula | Sheet Resistance | Usage |
|------|---------|------------------|-------|
| **nickel silicide** | NiSi | Low | Modern contact silicide |
| **cobalt silicide** | CoSi₂ | Low | Contact silicide |
| **titanium silicide** | TiSi₂ | Medium | Gate and contact silicide |
| **tungsten silicide** | WSi₂ | Medium | Gate electrode |
| **salicide** | Self-aligned silicide | N/A | Process terminology |

---

## E. Isolation and Separation Structures

| Term | Acronym | Description | Typical Dimensions |
|------|---------|-------------|-------------------|
| **shallow trench isolation** | STI | Trench filled with oxide | Depth: 200-500 nm |
| **local oxidation of silicon** | LOCOS | Thermally grown oxide isolation | Legacy technology |
| **field oxide** | FOX | Thick oxide for isolation | Thickness: 300-1000 nm |
| **deep trench isolation** | DTI | Deep isolation trench | Depth: 1-10 μm |
| **mesa isolation** | N/A | Etched mesa structure | For compound semiconductors |

---

## F. Transistor Structures and Types

### MOSFET Terminology

| Term | Full Name | Description |
|------|-----------|-------------|
| **MOSFET** | Metal-Oxide-Semiconductor FET | Generic MOS transistor |
| **NMOS** | N-channel MOSFET | Electrons are majority carriers |
| **PMOS** | P-channel MOSFET | Holes are majority carriers |
| **CMOS** | Complementary MOS | Both NMOS and PMOS on same chip |
| **FinFET** | Fin Field-Effect Transistor | 3D multi-gate transistor |
| **GAAFET** | Gate-All-Around FET | Nanowire/nanosheet transistor |
| **FDSOI** | Fully-Depleted SOI | Ultra-thin body SOI transistor |

### Power Device Types

| Term | Description | Typical Voltage |
|------|-------------|-----------------|
| **LDMOS** | Laterally Diffused MOS | 20-100 V |
| **VDMOS** | Vertical DMOS | 50-500 V |
| **IGBT** | Insulated Gate Bipolar Transistor | 600-6500 V |
| **SJ-MOSFET** | Superjunction MOSFET | 500-900 V |

### Specialized Transistors

| Term | Description | Application |
|------|-------------|-------------|
| **HEMT** | High Electron Mobility Transistor | RF, millimeter-wave |
| **HBT** | Heterojunction Bipolar Transistor | RF amplifiers |
| **MESFET** | Metal-Semiconductor FET | GaAs technology |
| **JFET** | Junction FET | Analog circuits |

---

## G. Fabrication Processes

### Deposition Methods

| Term | Acronym | Description | Typical Use |
|------|---------|-------------|-------------|
| **chemical vapor deposition** | CVD | Chemical reaction deposition | Oxide, nitride, poly-Si |
| **plasma-enhanced CVD** | PECVD | CVD with plasma enhancement | Lower temperature deposition |
| **atomic layer deposition** | ALD | Layer-by-layer atomic deposition | High-k dielectrics, conformal films |
| **physical vapor deposition** | PVD | Physical evaporation/sputtering | Metals |
| **molecular beam epitaxy** | MBE | Atomic layer epitaxial growth | High-quality epitaxy |
| **metal-organic CVD** | MOCVD | CVD with metal-organic precursors | III-V epitaxy |

### Etching Processes

| Term | Description | Characteristics |
|------|-------------|-----------------|
| **dry etch** | Plasma/reactive ion etching | Anisotropic, high selectivity |
| **wet etch** | Chemical solution etching | Often isotropic |
| **reactive ion etching** (RIE) | Plasma-based directional etch | Anisotropic |
| **deep reactive ion etching** (DRIE) | RIE for high aspect ratio | Deep trenches |
| **anisotropic etch** | Directional etch | Vertical sidewalls |
| **isotropic etch** | Non-directional etch | Rounded profiles |

### Doping Processes

| Term | Description | Energy/Conditions |
|------|-------------|-------------------|
| **ion implantation** | Accelerated ion bombardment | 1-500 keV typical |
| **diffusion** | Thermal dopant diffusion | 900-1200°C |
| **in-situ doping** | Doping during growth | During epitaxy/deposition |
| **spin-on dopant** | Liquid dopant source | Low-temperature doping |

### Thermal Processes

| Term | Description | Temperature Range |
|------|-------------|-------------------|
| **thermal oxidation** | Growing oxide in O₂/H₂O | 800-1200°C |
| **annealing** | Heat treatment for various purposes | 400-1100°C |
| **rapid thermal annealing** (RTA) | Fast heating/cooling | 900-1100°C, seconds |
| **spike anneal** | Very brief high-temperature anneal | Peak 1050-1100°C |
| **laser anneal** | Laser-based local heating | Surface melting |
| **furnace anneal** | Slow furnace-based anneal | Hours duration |

### Lithography Terms

| Term | Description |
|------|-------------|
| **photolithography** | Light-based pattern transfer |
| **optical lithography** | Same as photolithography |
| **extreme ultraviolet lithography** (EUV) | 13.5 nm wavelength lithography |
| **e-beam lithography** | Electron beam writing |
| **critical dimension** (CD) | Smallest feature size |
| **mask** | Pattern template (also called "reticle") |
| **photoresist** | Light-sensitive polymer |

### Planarization

| Term | Acronym | Description |
|------|---------|-------------|
| **chemical-mechanical polishing** | CMP | Mechanical grinding + chemical etching |
| **chemical-mechanical planarization** | CMP | Same as above (alternate name) |
| **etch-back** | N/A | Planarization by etching |

---

## H. Interconnect and Contact Structures

### Vertical Connections

| Term | Definition | Usage |
|------|------------|-------|
| **contact** | Connection from device to first metal | "contact to source/drain" |
| **via** | Connection between metal layers | "via connecting M1 to M2" |
| **through-silicon via** (TSV) | Vertical connection through wafer | 3D integration |
| **plug** | Filled contact or via | "tungsten plug" |

### Horizontal Interconnects

| Term | Definition |
|------|------------|
| **metal line** | Horizontal conductor in metal layer |
| **interconnect** | General term for wiring |
| **wiring** | Same as interconnect |
| **trace** | Conductive path (often in package) |

### Interconnect Structures

| Term | Description |
|------|-------------|
| **damascene** | Inlaid metal process (trench-first) |
| **dual damascene** | Combined via and trench filling |
| **subtractive** | Metal deposition then etch |

### Layers

| Term | Common Notation | Description |
|------|----------------|-------------|
| **metal layer** | M1, M2, M3, etc. | Numbered from bottom |
| **first metal layer** | M1 | Closest to devices |
| **back-end-of-line** (BEOL) | N/A | Interconnect formation |
| **front-end-of-line** (FEOL) | N/A | Device formation |

---

## I. Device Geometries and Dimensions

### Length and Width

| Term | Common Symbol | Definition |
|------|---------------|------------|
| **gate length** | L or Lg | Length of gate along current flow |
| **gate width** | W or Wg | Width perpendicular to current |
| **channel length** | Lch | Electrical channel length |
| **fin width** | Wfin | Width of fin in FinFET |
| **fin height** | Hfin | Height of fin in FinFET |
| **fin pitch** | Pfin | Center-to-center fin spacing |

### Thickness

| Term | Usage |
|------|-------|
| **thickness** | General term for layer height |
| **equivalent oxide thickness** (EOT) | Normalized gate dielectric thickness |
| **physical thickness** | Actual measured thickness |

### Spacing and Pitch

| Term | Definition |
|------|------------|
| **spacing** | Edge-to-edge distance |
| **pitch** | Center-to-center distance |
| **minimum feature size** | Smallest manufacturable dimension |
| **critical dimension** (CD) | Key dimension for device performance |

---

## J. Electrical Parameters

### Current and Voltage

| Parameter | Symbol | Units | Definition |
|-----------|--------|-------|------------|
| **threshold voltage** | Vth, Vt | V | Voltage to turn on transistor |
| **drain-source voltage** | Vds | V | Voltage between drain and source |
| **gate-source voltage** | Vgs | V | Voltage between gate and source |
| **breakdown voltage** | BV, Vbr | V | Maximum voltage before breakdown |
| **on-current** | Ion | A, A/μm | Current in on-state |
| **off-current** | Ioff | A, A/μm | Leakage current in off-state |
| **saturation current** | Isat | A | Current in saturation region |

### Resistance

| Parameter | Symbol | Units | Definition |
|-----------|--------|-------|------------|
| **on-resistance** | Ron | Ω, mΩ-cm² | Resistance in on-state |
| **sheet resistance** | Rsh, Rs | Ω/sq | Resistance per square |
| **contact resistance** | Rc | Ω-μm | Resistance at contact interface |
| **specific contact resistivity** | ρc | Ω-cm² | Contact resistance metric |

### Capacitance

| Parameter | Symbol | Units | Definition |
|-----------|--------|-------|------------|
| **gate capacitance** | Cg | F, fF | Total gate capacitance |
| **oxide capacitance** | Cox | F/cm² | Gate dielectric capacitance per area |
| **junction capacitance** | Cj | F, fF | P-n junction capacitance |

### Transconductance and Gain

| Parameter | Symbol | Units | Definition |
|-----------|--------|-------|------------|
| **transconductance** | gm | S, mS | dId/dVgs |
| **subthreshold swing** | SS, S | mV/dec | Switching steepness |
| **current gain** | β, hFE | N/A | For BJTs |

---

## K. Material Properties

### Dielectric Properties

| Property | Symbol | Units |
|----------|--------|-------|
| **dielectric constant** | k, εr | Dimensionless |
| **permittivity** | ε | F/m |
| **breakdown field** | Ebr | MV/cm |
| **bandgap** | Eg | eV |

### Conductor Properties

| Property | Symbol | Units |
|----------|--------|-------|
| **work function** | Φ, φm | eV |
| **resistivity** | ρ | Ω-cm |
| **conductivity** | σ | S/cm |

### Semiconductor Properties

| Property | Symbol | Units |
|----------|--------|-------|
| **bandgap** | Eg | eV |
| **electron mobility** | μn | cm²/V-s |
| **hole mobility** | μp | cm²/V-s |
| **carrier concentration** | n, p | cm⁻³ |
| **minority carrier lifetime** | τ | s, ns |

---

## L. Compound Semiconductors (III-V, II-VI)

### Common Materials

| Material | Type | Bandgap (eV) | Applications |
|----------|------|--------------|--------------|
| **GaAs** | III-V | 1.42 | RF, solar cells |
| **GaN** | III-V | 3.4 | Power devices, LEDs |
| **InP** | III-V | 1.35 | High-speed devices |
| **AlGaN** | III-V | 3.4-6.2 | HEMT barrier |
| **InGaN** | III-V | 0.7-3.4 | LED active region |
| **SiC** | IV-IV | 3.26 | Power devices |
| **AlN** | III-V | 6.2 | Deep UV LEDs |

### Heterostructure Terms

| Term | Definition |
|------|------------|
| **heterojunction** | Junction between different bandgap materials |
| **quantum well** | Thin layer between higher bandgap barriers |
| **two-dimensional electron gas** (2DEG) | High-mobility electron layer at heterojunction |
| **superlattice** | Periodic layered structure |
| **multiple quantum well** (MQW) | Multiple quantum wells |

---

## M. Optoelectronic Devices

### LED/Laser Terms

| Term | Definition |
|------|------------|
| **active region** | Light-emitting region |
| **quantum well** | Thin active layer |
| **p-contact** | Contact to p-type layer |
| **n-contact** | Contact to n-type layer |
| **transparent conductive oxide** | ITO, AZO for current spreading |
| **distributed Bragg reflector** (DBR) | Multi-layer mirror |

### Solar Cell Terms

| Term | Definition |
|------|------------|
| **p-n junction** | Basic solar cell structure |
| **emitter** | Front surface region |
| **base** | Bulk absorber region |
| **back surface field** (BSF) | Rear passivation layer |
| **anti-reflection coating** | Reduces reflection losses |

---

## N. Process Integration Terms

| Term | Definition |
|------|------------|
| **self-aligned** | Automatically aligned by process |
| **replacement gate** | Gate-last process |
| **gate-first** | Gate formed before source/drain |
| **gate-last** | Gate formed after source/drain |
| **high-k metal gate** (HKMG) | Combined high-k and metal gate |
| **source/drain epitaxy** | Raised source/drain by epitaxy |
| **strain engineering** | Stress for mobility enhancement |

---

## O. Common Abbreviations

| Abbreviation | Full Term |
|--------------|-----------|
| BEOL | Back-End-Of-Line |
| FEOL | Front-End-Of-Line |
| MOL | Middle-Of-Line |
| CMOS | Complementary Metal-Oxide-Semiconductor |
| SOI | Silicon-On-Insulator |
| FDSOI | Fully-Depleted SOI |
| FinFET | Fin Field-Effect Transistor |
| HKMG | High-k Metal Gate |
| STI | Shallow Trench Isolation |
| LDD | Lightly Doped Drain |
| RTA | Rapid Thermal Anneal |
| CMP | Chemical-Mechanical Polishing/Planarization |
| ALD | Atomic Layer Deposition |
| CVD | Chemical Vapor Deposition |
| PECVD | Plasma-Enhanced CVD |
| PVD | Physical Vapor Deposition |
| MBE | Molecular Beam Epitaxy |
| MOCVD | Metal-Organic CVD |
| EUV | Extreme Ultraviolet |

---

## P. Best Practices for Patent Drafting

### Terminology Consistency Rules

1. **Pick One Term and Stick to It**
   - ✓ Use "gate electrode" throughout
   - ✗ Don't alternate between "gate electrode," "gate conductor," and "gate"

2. **Define Terms in Specification**
   - First use: "The gate electrode (108) comprises..."
   - Subsequent: "The gate electrode (108) is formed..."

3. **Use Industry-Standard Terms**
   - ✓ "source region" (standard)
   - ✗ "current source area" (non-standard)

4. **Be Specific When Necessary**
   - ✓ "hafnium oxide gate dielectric"
   - Less specific: "high-k dielectric"
   - Too vague: "insulating material"

5. **Use Ranges for Manufacturing Tolerance**
   - ✓ "thickness in a range of 5 nm to 15 nm"
   - ✗ "thickness of approximately 10 nm"

6. **Distinguish Similar Terms**
   - "on" = direct contact
   - "over" = may have intervening layers
   - "in" = within or below surface
   - "above" = higher in vertical stack

### Common Mistakes to Avoid

1. ❌ Mixing "substrate" and "wafer"
2. ❌ Using "thin" instead of specific thickness
3. ❌ Inconsistent notation (switching between "n+" and "n-type heavily doped")
4. ❌ Undefined acronyms in claims
5. ❌ Using trade names instead of generic terms
6. ❌ Confusing process terms (e.g., "implanting" vs "doping")

---

## Q. Quick Reference: Common H01L Claim Language

**Substrate:**
"a substrate comprising [material] having a [orientation] crystal orientation"

**Doped Region:**
"a [conductivity type] region having a doping concentration in a range of [X] to [Y] cm⁻³"

**Layer Formation:**
"a [material] layer formed on the [underlying element], the [material] layer having a thickness in a range of [X] to [Y] nm"

**Transistor:**
"a transistor comprising a gate electrode, a gate dielectric layer, a source region, a drain region, and a channel region"

**Process Step:**
"forming a [element] by [process] at a temperature in a range of [X] to [Y] °C"

**Performance:**
"wherein the device has a [parameter] in a range of [X] to [Y] [units] when [conditions]"

---

**Last Updated:** 2026-01-04
**Version:** 1.0
**For:** H01L Patent Drafting Reference
