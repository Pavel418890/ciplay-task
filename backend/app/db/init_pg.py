import asyncio

import asyncpg

from app.core.config import config


async def init_pg() -> None:
    conn: asyncpg.Connection = await asyncpg.connect(dsn=config.POSTGRES_DSN)
    await conn.execute(
        """
    CREATE TABLE IF NOT EXISTS stats (
        id SERIAL PRIMARY KEY,
        date DATE NOT NULL,
        cost DECIMAL(10, 2), 
        clicks INT,
        views INT
    )
    """
    )
    await conn.close()


async def main() -> None:
    print("Initialize database.")
    await init_pg()
    print("Initial database was created.")


if __name__ == "__main__":
    asyncio.run(main())
