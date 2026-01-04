# Claude Code Configuration for Patent Workspace

This directory contains Claude Code custom commands and configuration for the patent analysis and writing environment.

## Available Commands

Use these slash commands to access specialized patent workflows:

### `/draft-patent`
Draft a new patent application from invention description.
- Creates application, claims, and abstract files
- Follows USPTO format and best practices
- Ensures proper structure and quality checks

### `/analyze-claims`
Analyze patent claims for structural issues and best practices.
- Checks antecedent basis
- Verifies claim differentiation
- Identifies definiteness issues
- Runs automated claim-analyzer.py tool

### `/prior-art`
Conduct comprehensive prior art search and analysis.
- Generates search queries and strategies
- Identifies relevant CPC/IPC classifications
- Creates claim charts
- Performs anticipation and obviousness analysis

### `/fto`
Conduct Freedom to Operate (FTO) / clearance analysis.
- Identifies potentially conflicting patents
- Performs infringement analysis
- Assesses risk levels
- Recommends mitigation strategies

### `/patentability`
Conduct comprehensive patentability analysis.
- Analyzes subject matter eligibility (§ 101)
- Assesses novelty (§ 102)
- Evaluates non-obviousness (§ 103)
- Checks written description, enablement, definiteness (§ 112)

### `/invention-disclosure`
Guide user through completing invention disclosure form.
- Systematic interview process
- Captures all necessary details
- Creates disclosure document
- Recommends next steps

### `/review`
Review patent document for quality, consistency, and common issues.
- Comprehensive quality assurance
- Checks all patent law requirements
- Verifies terminology consistency
- Validates proper formatting

### `/cpc-classify`
Identify relevant CPC/IPC patent classifications.
- Analyzes invention technical field
- Suggests primary and secondary classifications
- Provides search recommendations
- Helps navigate classification hierarchy

## Usage

Simply type the slash command in your conversation with Claude:

```
/draft-patent
```

Claude will then follow the detailed workflow defined for that command.

## Configuration Files

- **CLAUDE.md**: Rules and guidelines for Claude when working in this patent environment
- **.claude/commands/**: Slash command definitions
- **.claude/skills/**: Custom agent skills (if any)

## Customization

You can create additional custom commands by adding new `.md` files to `.claude/commands/`:

```markdown
---
description: Brief description of what this command does
---

Detailed instructions for Claude to follow...
```

## Tools Integration

Commands automatically integrate with the Python tools in `tools/`:

- `word-count.py`: Validates abstract length and document structure
- `claim-analyzer.py`: Analyzes claims for common issues
- `prior-art-search.py`: Generates search queries and classifications

## Best Practices

1. Always start with `/invention-disclosure` for new inventions
2. Run `/prior-art` before drafting to understand the landscape
3. Use `/draft-patent` with template-based approach
4. Run `/review` before finalizing any document
5. Use `/patentability` for comprehensive assessment
6. Run `/fto` before product commercialization

## Templates Used

Commands reference templates from:
- `templates/applications/`: Patent application templates
- `templates/claims/`: Claims templates
- `templates/analysis/`: Analysis templates
- `templates/abstracts/`: Abstract templates

## See Also

- Main README.md: Overview of patent workspace
- CLAUDE.md: Detailed rules for Claude
- docs/getting-started.md: Getting started guide

---

**Version**: 1.0
**Last Updated**: 2026-01-04
