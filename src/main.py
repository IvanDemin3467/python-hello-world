import os
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    port = os.getenv("PORT", "8000")
    print(f"starting hello-world FastAPI app on 0.0.0.0:{port}", flush=True)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/", response_class=PlainTextResponse)
async def root() -> str:
    return "hello world\n"


@app.get("/health", response_class=PlainTextResponse)
async def health() -> str:
    return "ok\n"
