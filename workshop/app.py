from fastapi import FastAPI
from workshop.api import router
import uvicorn
from workshop.settings import settings

app = FastAPI(title='User API', description='REST API')
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run(
        "workshop.app:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
