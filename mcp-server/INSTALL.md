# Installation Guide for Patent Tools MCP Server

## Prerequisites

- Python 3.10 or higher
- [uv](https://github.com/astral-sh/uv) - Fast Python package manager (recommended)
- Claude Desktop (for MCP integration) or Claude Code CLI

## Step-by-Step Installation

### 1. Install uv (if not already installed)

```bash
# Install uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or using pip
pip install uv

# Or using Homebrew (macOS)
brew install uv
```

### 2. Verify Python Installation

```bash
python --version
# or
python3 --version
```

You should see Python 3.10 or higher. If not, install Python from https://www.python.org/

### 3. Navigate to MCP Server Directory

```bash
cd /path/to/patent-lawer-space/mcp-server
```

### 4. Install Dependencies

Choose one of the following methods:

#### Method A: Using uv (Recommended - Fast!)

```bash
uv pip install -r requirements.txt
```

#### Method B: Using uv in editable mode (for development)

```bash
uv pip install -e .
```

#### Method C: Using pip (Alternative)

```bash
pip install -r requirements.txt
```

#### Method D: Install MCP SDK directly

```bash
uv pip install mcp
# or
pip install mcp
```

### 5. Verify Installation

Check that the MCP package is installed:

```bash
uv pip list | grep mcp
# or
pip show mcp
```

You should see output showing the MCP package details.

### 6. Test the Server

Try running the server to ensure it starts without errors:

```bash
python run.py
```

The server should start and wait for input. Press `Ctrl+C` to stop it. If you see any errors, check the troubleshooting section below.

## Configuration

### For Claude Desktop

1. **Locate your Claude Desktop configuration file:**

   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

2. **Edit the configuration file** and add the MCP server:

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

   **Important Notes:**
   - Replace `/absolute/path/to/patent-lawer-space` with the **actual absolute path** to your repository
   - Use forward slashes `/` even on Windows
   - Ensure the path has no spaces, or properly escape them
   - You can find the absolute path by running `pwd` (macOS/Linux) or `cd` (Windows) in the mcp-server directory

3. **Example configurations:**

   **macOS/Linux:**
   ```json
   {
     "mcpServers": {
       "patent-tools": {
         "command": "python3",
         "args": [
           "/home/username/projects/patent-lawer-space/mcp-server/run.py"
         ]
       }
     }
   }
   ```

   **Windows:**
   ```json
   {
     "mcpServers": {
       "patent-tools": {
         "command": "python",
         "args": [
           "C:/Users/username/projects/patent-lawer-space/mcp-server/run.py"
         ]
       }
     }
   }
   ```

4. **Restart Claude Desktop** for the changes to take effect.

### For Claude Code CLI

If you're using Claude Code with MCP support, add the configuration to your project or global config file.

## Verification

### Test in Claude Desktop

1. Open Claude Desktop
2. Start a new conversation
3. Ask Claude: "What MCP tools do you have available?"
4. You should see three patent analysis tools listed:
   - analyze_patent_word_count
   - analyze_patent_claims
   - generate_prior_art_search

### Test with Example

Try this prompt in Claude Desktop:

```
Can you analyze the word count in this text:

## ABSTRACT

This invention relates to a system for processing data using machine learning algorithms...
[add about 100-150 words of sample text]
```

Claude should use the `analyze_patent_word_count` tool and provide an analysis.

## Troubleshooting

### Issue: "MCP package not found"

**Solution:**
```bash
uv pip install mcp
# or
uv pip install --upgrade mcp

# Alternative with pip:
pip install mcp
```

### Issue: "python command not found"

**Solution:**
- Try using `python3` instead of `python` in the configuration
- Verify Python is in your PATH
- Use the full path to Python: `/usr/bin/python3` or `C:\Python311\python.exe`

### Issue: "Permission denied"

**Solution:**
```bash
chmod +x /path/to/patent-lawer-space/mcp-server/run.py
```

### Issue: "Module not found" errors

**Solution:**
Make sure you're installing packages for the correct Python version:
```bash
uv pip install -r requirements.txt
# or
python -m pip install -r requirements.txt
# or
python3 -m pip install -r requirements.txt
```

### Issue: Claude Desktop doesn't show the tools

**Solutions:**
1. Verify the configuration file path is correct
2. Check that you used absolute paths (not relative)
3. Restart Claude Desktop completely (quit and reopen)
4. Check Claude Desktop logs for errors:
   - macOS: `~/Library/Logs/Claude/`
   - Windows: `%APPDATA%\Claude\logs\`

### Issue: "Import error: mcp.server"

**Solution:**
The MCP SDK might not be installed correctly. Try:
```bash
uv pip uninstall mcp
uv pip install mcp

# Or with pip:
pip uninstall mcp
pip install mcp
```

### Issue: Server starts but tools don't work

**Solutions:**
1. Check that the `tools/` directory is accessible
2. Verify file paths when using the tools
3. Ensure files are in the correct format (markdown)
4. Check server logs for specific errors

## Virtual Environment (Recommended)

For a cleaner installation, use a Python virtual environment with uv:

```bash
# Create and use virtual environment with uv (recommended)
cd /path/to/patent-lawer-space/mcp-server

# Create virtual environment
uv venv

# Activate it
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Update Claude Desktop config to use the venv Python:
# "command": "/path/to/patent-lawer-space/mcp-server/.venv/bin/python"
```

**Alternative with standard venv:**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Updating

To update the MCP server or dependencies:

```bash
cd /path/to/patent-lawer-space/mcp-server
git pull  # if using git
uv pip install --upgrade -r requirements.txt

# Or with pip:
pip install --upgrade -r requirements.txt
```

Then restart Claude Desktop.

## Uninstallation

To remove the MCP server:

1. Remove the `patent-tools` entry from Claude Desktop config
2. Restart Claude Desktop
3. Optionally, uninstall the Python package:
   ```bash
   uv pip uninstall mcp
   # or
   pip uninstall mcp
   ```

## Getting Help

If you encounter issues:

1. Check the [main README](README.md) for usage examples
2. Review the [troubleshooting section](#troubleshooting) above
3. Check MCP protocol documentation: https://modelcontextprotocol.io/
4. Verify your Python and uv versions are up to date

## Next Steps

Once installed, see the [main README](README.md) for:
- Usage examples
- Tool descriptions
- Integration with Claude workflows
- Example prompts

---

**Last Updated**: 2026-01-04
**Note**: This guide uses `uv` for faster, more reliable package management. You can still use `pip` if you prefer.
