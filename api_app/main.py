import uvicorn
from dotenv import load_dotenv
import os


if __name__ == "__main__":
    """
        Main entry point for running the FastAPI server using Uvicorn.

        This script starts the FastAPI server using the Uvicorn ASGI server.
        It runs the FastAPI application defined in the "server.app" module.

        Usage:
            python main.py

        Note:
            The server will be accessible at http://localhost:port/.

    """
    load_dotenv()
    port = os.environ.get("PORT")
    uvicorn.run("server.app:app", host="localhost", port=port, reload=True)