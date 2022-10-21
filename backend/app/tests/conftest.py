import asyncio
import urllib.parse
from typing import AsyncGenerator, Iterator

import asyncpg
import pytest_asyncio
from httpx import AsyncClient

from app.core.config import config
from app.main import app


@pytest_asyncio.fixture(scope="session")
async def db() -> asyncpg.Connection:
    async with asyncpg.create_pool(config.POSTGRES_DSN) as conn:
        yield conn


@pytest_asyncio.fixture(scope="module")
async def client() -> AsyncGenerator:
    print(config.BASE_CLIENT_URL, config.API_V1)
    async with AsyncClient(
        app=app, base_url=f"{config.BASE_CLIENT_URL}{config.API_V1}"
    ) as cli:
        yield cli


@pytest_asyncio.fixture(scope="session")
def event_loop() -> Iterator[asyncio.events.AbstractEventLoop]:
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()
