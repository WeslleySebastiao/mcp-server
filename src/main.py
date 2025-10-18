import uvicorn
from config import *
from utils.logs.log_config import logging


logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info(f"Initializing MCP Server: {SERVER_NAME} on {HOST}:{PORT}")
    uvicorn.run(
        "server.api:app",
        host=HOST,
        port=PORT,
        log_level=LOG_LEVEL,
        reload=True,
    )