#!/usr/bin/env python3
"""
Standalone entry point for the Patent Tools MCP Server.
Can be run directly without package installation.
"""

if __name__ == "__main__":
    from patent_tools_mcp.server import main
    import asyncio

    asyncio.run(main())
