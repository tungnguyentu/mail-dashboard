from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from config.environment import Settings


app = FastAPI()


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=Settings.API_HOST,
        port=Settings.API_PORT,
        reload=True,
        debug=True
    )
