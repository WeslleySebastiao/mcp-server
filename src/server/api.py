from server.mcp_instance import mcp
import logging
logger = logging.getLogger(__name__)


@mcp.get("/health", tags=["system"])
async def health_check():
    "System activation check endpoint"
    logger.info("Health check endpoint called")
    return {"status": "ok", "message": "MCP Server is running"}


