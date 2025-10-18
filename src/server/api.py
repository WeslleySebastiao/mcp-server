from fastapi import FastAPI
from config import SERVER_NAME
from utils.logs.log_config import logging


logger = logging.getLogger(__name__)

app = FastAPI(
    title = SERVER_NAME,
    descriptions = f"MCP server for running tool and more with agents - {SERVER_NAME}",
    version = "0.1.0",
)

#Routes

@app.get("/", tags=["system"])
async def root():
    "Root endpoint"
    return {"message": f"Welcome to {SERVER_NAME}!"}


@app.get("/health", tags=["system"])
async def health_check():
    "System activation check endpoint"
    logger.info("Health check endpoint called")
    return {"status": "ok", "message": "MCP Server is running"}


