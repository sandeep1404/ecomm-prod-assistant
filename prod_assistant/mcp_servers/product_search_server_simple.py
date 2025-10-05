import sys
import os
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(project_root))

from mcp.server.fastmcp import FastMCP
from langchain_community.tools import DuckDuckGoSearchRun

# Initialize MCP server
mcp = FastMCP("hybrid_search")

# LangChain DuckDuckGo tool
duckduckgo = DuckDuckGoSearchRun()

# ---------- MCP Tools ----------
@mcp.tool()
async def get_product_info(query: str) -> str:
    """Retrieve product information for a given query using web search."""
    try:
        # For now, just use web search as a fallback
        result = duckduckgo.run(query)
        return f"Web search results for '{query}':\n{result}"
    except Exception as e:
        return f"Error retrieving product info: {str(e)}"

@mcp.tool()
async def web_search(query: str) -> str:
    """Search the web using DuckDuckGo."""
    try:
        return duckduckgo.run(query)
    except Exception as e:
        return f"Error during web search: {str(e)}"

# ---------- Run Server ----------
if __name__ == "__main__":
    mcp.run(transport="stdio")
