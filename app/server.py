from fastmcp import FastMCP
from .brave_search import search_pdfs  # 相対インポートに変更

mcp = FastMCP("PDFSearcher")

@mcp.tool()
async def find_pdf(prompt: str) -> list[dict]:
    """指定されたトピックに関するPDFを検索します。"""
    return await search_pdfs(prompt)



if __name__ == "__main__":
    mcp.run(transport='stdio')

