"""FastAPI app for ClimateFarm."""
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from .routers import ingest, alerts, sms, farmers
import yaml

def create_app() -> FastAPI:
    app = FastAPI(title="ClimateFarm", version="0.1.0")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    app.include_router(ingest.router)
    app.include_router(alerts.router)
    app.include_router(sms.router)
    app.include_router(farmers.router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app

app = create_app()
