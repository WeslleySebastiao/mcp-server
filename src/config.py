import os
from dotenv import load_dotenv
load_dotenv()


#Port and host configuration
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", 8000)

#MCP Server name
SERVER_NAME = os.getenv("SERVER_NAME", "mcp-server")

#Logging configuration
LOG_LEVEL = os.getenv("LOG_LEVEL", "info")



