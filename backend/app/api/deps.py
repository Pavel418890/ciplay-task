import asyncpg

from app.core.config import config


async def get_db() -> asyncpg.Connection:
    async with asyncpg.create_pool(dsn=config.POSTGRES_DSN) as conn:
        yield conn
