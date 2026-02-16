from fastmcp import FastMCP

# 初始化 MCP 伺服器
mcp = FastMCP("Stock_Strategy_Agent")

# 測試用工具：加法
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """這是一個測試工具，用來確認 n8n 與 MCP 連接成功。"""
    return a + b

# 預留給成員 B 的工具接口
@mcp.tool()
def placeholder_for_member_b(ticker: str) -> str:
    """這是成員 B 未來要填入 yfinance 邏輯的地方。"""
    return f"正在準備 {ticker} 的數據分析..."

if __name__ == "__main__":
    # 使用 sse 模式啟動
    mcp.run(transport="sse", host="0.0.0.0", port=8000)