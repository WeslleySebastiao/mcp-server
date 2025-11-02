async def listar_tools(mcp):
    tools = await mcp.list_tools()  # retorna lista de ToolDescription
    tool_names = [tool.name for tool in tools]
    return len(tool_names), tool_names