# Claude Code Skills for Patent Workspace

This directory contains autonomous agent skills for specialized patent work. Skills are invoked programmatically and work autonomously to complete complex, multi-step tasks.

## Available Skills

### `patent-drafter`
**Autonomous patent application drafting agent**

Drafts complete, filing-ready patent applications including:
- Independent and dependent claims (system, method, CRM)
- Detailed specification with multiple embodiments
- Abstract (verified ≤150 words)
- Background and summary sections
- Quality checks and tool integration

**When to use**: When you need a complete patent application drafted from an invention description.

**What it does autonomously**:
- Analyzes invention disclosure
- Drafts comprehensive claim set (15-20+ claims)
- Creates detailed specification
- Writes abstract
- Runs quality tools (claim-analyzer, word-count)
- Verifies antecedent basis and terminology consistency
- Provides filing recommendations

---

### `prior-art-hunter`
**Autonomous prior art search and analysis agent**

Conducts comprehensive prior art searches and creates detailed analysis:
- Multi-database searching (USPTO, Google Patents, Espacenet, etc.)
- CPC/IPC classification identification
- Claim chart creation
- Anticipation (§ 102) and obviousness (§ 103) analysis
- Prosecution strategy recommendations

**When to use**: Before drafting or filing to understand the prior art landscape.

**What it does autonomously**:
- Generates search queries and strategy
- Searches multiple patent databases
- Finds 5-15 most relevant references
- Creates element-by-element claim charts
- Analyzes novelty and non-obviousness
- Recommends claim amendments
- Provides prosecution arguments

---

### `claims-engineer`
**Autonomous claims drafting and optimization agent**

Specialized in drafting and optimizing patent claims:
- Multiple claim types (system, method, CRM)
- Proper legal structure and antecedent basis
- Claim differentiation and hierarchy
- Coverage optimization
- Definiteness verification

**When to use**: When you need high-quality claims drafted or existing claims optimized.

**What it does autonomously**:
- Develops claim strategy (3+ independent, 15+ total)
- Drafts independent claims (broad to narrow)
- Creates dependent claim hierarchy
- Verifies antecedent basis throughout
- Checks definiteness (no vague terms)
- Runs claim-analyzer.py
- Ensures claim differentiation
- Provides coverage analysis

---

### `fto-analyst`
**Autonomous Freedom to Operate analysis agent**

Conducts FTO/clearance analysis for product commercialization:
- Identifies potentially blocking patents
- Performs claim-by-claim infringement analysis
- Assesses risk levels (high/medium/low)
- Evaluates validity of concerning patents
- Recommends mitigation strategies

**When to use**: Before launching a product to assess patent infringement risk.

**What it does autonomously**:
- Extracts product features
- Searches for relevant active patents
- Creates claim charts for infringement analysis
- Applies "all elements rule" and doctrine of equivalents
- Assigns risk levels with justification
- Analyzes validity of high-risk patents
- Identifies design-around options
- Evaluates licensing opportunities
- Provides comprehensive risk mitigation strategy

⚠️ **Note**: FTO analysis is complex and this is informational only. Always recommend professional patent attorney review.

---

### `patent-examiner`
**Autonomous patent examination simulation agent**

Simulates USPTO examination to identify issues before filing:
- Subject matter eligibility (§ 101) - Alice/Mayo test
- Prior art search and novelty analysis (§ 102)
- Non-obviousness evaluation (§ 103)
- Written description, enablement, definiteness (§ 112)
- Drafts simulated office action with rejections

**When to use**: Before filing to identify and fix potential issues.

**What it does autonomously**:
- Reviews application for formalities
- Applies § 101 Alice/Mayo framework
- Conducts prior art search
- Creates claim charts vs. prior art
- Performs § 102 anticipation analysis
- Performs § 103 obviousness analysis (Graham factors, KSR)
- Checks § 112(a) written description and enablement
- Checks § 112(b) definiteness
- Drafts simulated office action with specific rejections
- Suggests amendments to overcome rejections
- Provides prosecution strategy
- Estimates likelihood of allowance

---

## How to Use Skills

Skills are invoked programmatically by Claude Code. They work autonomously to complete their assigned tasks and return comprehensive results.

### Example Workflow

1. **Start with Invention Disclosure**
   ```
   "I have an invention for [description]. Please use the patent-drafter skill to create a complete patent application."
   ```

2. **Conduct Prior Art Search**
   ```
   "Use the prior-art-hunter skill to search for prior art related to [invention]."
   ```

3. **Optimize Claims**
   ```
   "Use the claims-engineer skill to draft optimized claims for [invention]."
   ```

4. **Simulate Examination**
   ```
   "Use the patent-examiner skill to simulate USPTO examination of my application."
   ```

5. **Before Product Launch**
   ```
   "Use the fto-analyst skill to analyze FTO risk for [product]."
   ```

## Skill Integration

Skills work together and with slash commands:

- **patent-drafter** → Creates draft → **patent-examiner** → Identifies issues → **claims-engineer** → Refines claims
- **/prior-art** command → **prior-art-hunter** skill → Detailed autonomous search
- **/fto** command → **fto-analyst** skill → Comprehensive FTO analysis

## Tools Integration

Skills automatically use tools from `tools/`:
- `claim-analyzer.py`: Checks claims for structural issues
- `word-count.py`: Verifies abstract word count
- `prior-art-search.py`: Generates search strategies

## Templates Integration

Skills automatically use templates from `templates/`:
- `applications/utility-patent-template.md`
- `claims/claims-template.md`
- `abstracts/abstract-template.md`
- `analysis/*.md`

## Output Locations

Skills create files in standard locations:

**Drafts**:
- `patents/drafts/[invention-name]-application.md`
- `patents/drafts/[invention-name]-claims.md`
- `patents/drafts/[invention-name]-abstract.md`

**Analysis**:
- `patents/analysis/[invention-name]-prior-art.md`
- `patents/analysis/[invention-name]-fto-analysis.md`
- `patents/analysis/[invention-name]-office-action-simulation.md`
- `patents/analysis/[invention-name]-search-strategy.md`

## Success Criteria

Each skill has defined success criteria and deliverables. Skills work autonomously but will:
- Request clarification for unclear inputs
- Report progress on complex tasks
- Provide comprehensive final reports
- Recommend next steps

## Best Practices

1. **Provide Clear Input**: Give skills detailed invention descriptions or product specifications
2. **Sequential Use**: Use skills in logical order (disclosure → draft → examine → refine)
3. **Review Outputs**: Skills are autonomous but outputs should be reviewed
4. **Professional Review**: Skills assist but don't replace patent attorney review
5. **Iterate**: Use skills multiple times to refine work

## Limitations

- Skills provide informational assistance, not legal advice
- Prior art searches may not be exhaustive
- FTO analysis requires attorney review for final opinion
- Office action simulation may differ from actual USPTO examination
- Professional patent attorney review recommended before filing

## See Also

- **Slash Commands**: `.claude/commands/` - Interactive workflows
- **CLAUDE.md**: Rules and guidelines for patent work
- **Main README**: Overview of patent workspace

---

**Version**: 1.0
**Last Updated**: 2026-01-04
