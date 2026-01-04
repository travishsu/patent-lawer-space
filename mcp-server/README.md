# Patent Tools MCP Server

A Model Context Protocol (MCP) server that provides patent analysis tools for Claude. This server exposes three powerful patent analysis tools through the MCP protocol, allowing Claude to analyze patent documents, check claims, and generate prior art search strategies.

## Features

### 🔍 Three Powerful Tools

1. **analyze_patent_word_count** - Word count analysis for patent documents
   - Counts total words in patent documents
   - Checks abstracts against USPTO 150-word requirement
   - Identifies document sections (Background, Summary, Description, Claims, Abstract)
   - Validates document structure

2. **analyze_patent_claims** - Claims structure and antecedent basis analysis
   - Extracts and analyzes individual patent claims
   - Checks for proper antecedent basis ("a/an" before "the")
   - Identifies claim dependencies (independent vs dependent claims)
   - Validates claim structure and transition phrases
   - Detects common drafting issues
   - Provides suggestions for improvement

3. **generate_prior_art_search** - Prior art search query generation
   - Extracts keywords and technical terms from inventions
   - Generates Boolean search queries for patent databases
   - Suggests relevant CPC (Cooperative Patent Classification) codes
   - Provides search strategy and recommended databases
   - Helps conduct comprehensive prior art searches

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager

### Quick Install

1. **Navigate to the mcp-server directory:**
   ```bash
   cd mcp-server
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or using the full package:
   ```bash
   pip install -e .
   ```

### Verify Installation

Test the server locally:
```bash
python run.py
```

The server should start and wait for MCP protocol messages via stdin/stdout.

## Configuration

### For Claude Desktop

Add the following to your Claude Desktop configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "patent-tools": {
      "command": "python",
      "args": [
        "/absolute/path/to/patent-lawer-space/mcp-server/run.py"
      ]
    }
  }
}
```

**Important**: Replace `/absolute/path/to/patent-lawer-space` with the actual absolute path to your repository.

### For Claude Code (CLI)

If using Claude Code CLI with MCP support, configure in your project's `.claude/config.json` or global configuration.

## Usage

Once configured, the tools are available in Claude conversations. Here are example prompts:

### Word Count Analysis

```
Can you analyze the word count of my patent abstract at patents/drafts/my-abstract.md?
```

Claude will use the `analyze_patent_word_count` tool and report:
- Total word count
- Whether it meets the 150-word USPTO requirement
- Document structure validation

### Claims Analysis

```
Please analyze the claims in patents/drafts/my-claims.md for structural issues and antecedent basis.
```

Claude will use the `analyze_patent_claims` tool to check:
- Independent vs dependent claims
- Antecedent basis issues
- Claim structure and formatting
- Transition phrases
- Common drafting problems

### Prior Art Search

```
Generate a prior art search strategy for the invention described in patents/drafts/my-invention.md
```

Claude will use the `generate_prior_art_search` tool to provide:
- Top keywords and technical terms
- Boolean search queries
- Suggested CPC classifications
- Recommended databases
- Step-by-step search strategy

## Tool Parameters

### analyze_patent_word_count

```json
{
  "content": "Patent document content...",  // Optional
  "file_path": "/path/to/file.md",         // Optional
  "file_name": "abstract.md"                // Optional
}
```

Either `content` or `file_path` must be provided.

### analyze_patent_claims

```json
{
  "content": "Patent claims content...",   // Optional
  "file_path": "/path/to/claims.md"       // Optional
}
```

Either `content` or `file_path` must be provided.

### generate_prior_art_search

```json
{
  "content": "Invention description...",  // Optional
  "file_path": "/path/to/invention.md"   // Optional
}
```

Either `content` or `file_path` must be provided.

## Architecture

```
mcp-server/
├── patent_tools_mcp/
│   ├── __init__.py          # Package initialization
│   ├── __main__.py          # Package entry point
│   └── server.py            # Main MCP server implementation
├── run.py                   # Standalone entry point
├── pyproject.toml           # Package configuration
├── requirements.txt         # Python dependencies
├── claude-desktop-config.json  # Example configuration
└── README.md               # This file
```

### How It Works

1. **MCP Protocol**: The server communicates with Claude using the Model Context Protocol over stdin/stdout
2. **Tool Registration**: On startup, the server registers three tools with detailed schemas
3. **Tool Execution**: When Claude calls a tool, the server:
   - Reads content from file or receives it directly
   - Runs the appropriate analysis function
   - Returns formatted results to Claude
4. **Results**: Claude receives structured data and presents it to the user

## Development

### Running Tests

```bash
cd mcp-server
python -m pytest tests/
```

### Adding New Tools

To add a new patent analysis tool:

1. Add the analysis function to `server.py`
2. Register the tool in the `list_tools()` function
3. Handle tool calls in the `call_tool()` function
4. Update this README

### Debugging

Enable verbose logging by setting the `MCP_DEBUG` environment variable:

```bash
MCP_DEBUG=1 python run.py
```

## Integration with Existing Tools

This MCP server wraps the existing Python tools in the `tools/` directory:
- `tools/word-count.py`
- `tools/claim-analyzer.py`
- `tools/prior-art-search.py`

The original tools can still be used standalone via command line:

```bash
cd tools
python word-count.py ../patents/drafts/my-abstract.md
python claim-analyzer.py ../patents/drafts/my-claims.md
python prior-art-search.py ../patents/drafts/my-invention.md
```

The MCP server provides the same functionality but makes it accessible to Claude through the MCP protocol.

## Troubleshooting

### Server Won't Start

- Verify Python version: `python --version` (must be 3.10+)
- Check dependencies: `pip install -r requirements.txt`
- Ensure the MCP package is installed: `pip show mcp`

### Claude Can't Find Tools

- Verify the configuration path in Claude Desktop config
- Use absolute paths, not relative paths
- Restart Claude Desktop after configuration changes
- Check Claude Desktop logs for errors

### Tools Return Errors

- Ensure file paths are absolute and files exist
- Check that files are readable by the server process
- Verify file content is in the expected format (markdown)

### Permission Issues

- Ensure the Python script has execute permissions:
  ```bash
  chmod +x run.py
  ```

## Examples

### Example 1: Check Abstract Word Count

**User**: "Check if my abstract meets USPTO requirements"

**Claude** uses `analyze_patent_word_count`:
```
=== Patent Word Count Analysis ===

File: abstract.md
Total words: 142

Abstract Requirements:
  Maximum allowed: 150 words
  Current count: 142 words
  ✓ Within limit (8 words remaining)
```

### Example 2: Analyze Claims

**User**: "Review my patent claims for issues"

**Claude** uses `analyze_patent_claims`:
```
=== Patent Claims Analysis ===

Total claims: 5
Independent claims: 2 - [1, 4]
Dependent claims: 3

=== Claim-by-Claim Analysis ===

Claim 1:
  Type: Independent
  Word count: 87
  Transition: comprising (open-ended)
  ✓ No issues found

Claim 2:
  Type: Dependent
  Depends on: Claim 1
  Word count: 45
  ⚠ Possible antecedent basis issue: 'the processor' without prior 'a/an processor'
```

### Example 3: Generate Prior Art Search

**User**: "Help me search for prior art on my AI-powered image recognition system"

**Claude** uses `generate_prior_art_search`:
```
=== Prior Art Search Strategy ===

1. RECOMMENDED DATABASES:
   - USPTO Patent Full-Text Database
   - Google Patents
   - IEEE Xplore

2. TOP KEYWORDS:
   1. image (15 occurrences)
   2. recognition (12 occurrences)
   3. neural (10 occurrences)
   ...

4. BOOLEAN SEARCH QUERIES:
   Query 1: image AND recognition AND neural AND network AND processing
   Query 2: image OR recognition OR neural
   ...

5. SUGGESTED CPC CLASSIFICATIONS:
   - G06N (matched: neural network)
   - G06T (matched: image processing)
```

## License

This MCP server is part of the patent analysis and writing environment. See the main repository LICENSE for details.

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## Support

For issues, questions, or suggestions:

- Open an issue in the GitHub repository
- Check the main project CLAUDE.md for patent-specific guidelines
- Review MCP protocol documentation at https://modelcontextprotocol.io/

## Version History

### 0.1.0 (2026-01-04)
- Initial release
- Three core tools: word count, claims analysis, prior art search
- Full MCP protocol support
- Compatible with Claude Desktop and Claude Code

---

**Built for patent professionals using Claude** | Model Context Protocol Server
