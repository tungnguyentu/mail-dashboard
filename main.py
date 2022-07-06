from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from config.environment import Settings
from mail_dashboard_service.api.routers.free_mail import (
    router as free_mail_router,
)
from mail_dashboard_service.api.routers.upgrade_account import (
    router as upgrade_account_router,
)
from mail_dashboard_service.api.routers.subscription import (
    router as subscription_router,
)

app = FastAPI()

app.include_router(free_mail_router, prefix="/api/v1")
app.include_router(upgrade_account_router, prefix="/api/v1")
app.include_router(subscription_router, prefix="/api/v1")


@app.get("/")
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

uvicorn.run(
    app, 
    host=Settings.API_HOST,
    port=Settings.API_PORT,
    debug=Settings.API_DEBUG_MODE,
    reload=Settings.API_AUTO_RELOAD
)