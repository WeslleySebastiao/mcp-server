import asyncio
from server.mcp_instance import mcp
from config import *
from utils.logs.log_config import logging
from tools import basic_tools  
from utils.mcp_helpers import listar_tools

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    mcp.run(transport="sse")