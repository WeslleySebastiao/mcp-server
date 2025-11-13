import os
import asyncio
import src.config
from src.server.mcp_instance import mcp
from src.utils.logs.log_config import logging
from src.tools import basic_tools  
from src.utils.mcp_helpers import listar_tools

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    host = os.environ.get("HOST", "0.0.0.0")
    mcp.run(
        transport="sse",
        host=host,
        port=port
    )