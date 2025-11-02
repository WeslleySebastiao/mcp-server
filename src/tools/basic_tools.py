from server.mcp_instance import mcp

print(f"[DEBUG] basic_tools importou MCP -> id: {id(mcp)}")


@mcp.tool()
def say_hello(name: str = 'Mundo')  -> str:
    """Returns a greeting message."""
    return f'Hello, {name}!'