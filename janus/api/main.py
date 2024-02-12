import logging

from fastapi import FastAPI

from janus.api.endpoints.collect_qc import collect_qc_router

app = FastAPI()

LOG = logging.getLogger("__name__")


@app.get("/")
async def root():
    return {"message": "Welcome to Janus"}


app.include_router(collect_qc_router, prefix="/api", tags=["collect_qc"])
