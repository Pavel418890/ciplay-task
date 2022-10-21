from typing import Optional

import asyncpg
from asyncpg import Record

from app.schemas.stats import CreateStats, GetStats


class CRUDStats:
    async def create(
        self, c: asyncpg.Connection, *, data: CreateStats
    ) -> Optional[Record]:
        return await c.fetchrow(
            """
            INSERT INTO stats(date, cost, clicks, views)
            VALUES ($1, $2, $3, $4)
            RETURNING *;
            """,
            data.date,
            data.cost,
            data.clicks,
            data.views,
        )

    async def get_by_id(self, c: asyncpg.Connection, *, id_) -> Optional[Record]:
        return await c.fetchrow(
            """
            SELECT id, date, cost, views, clicks 
            FROM stats 
            WHERE id = $1;
            """,
            id_,
        )

    async def show_stats(
        self, c: asyncpg.Connection, *, data: GetStats
    ) -> Optional[list[Record]]:
        if data.order_by is None:
            data.order_by = "date"

        return await c.fetch(
            """
            SELECT date,
                   SUM(cost) AS cost,
                   SUM(clicks) AS clicks,
                   SUM(views) AS views,
                   (SUM(cost) / SUM(clicks))::DECIMAL(20, 2) AS cpc,
                   ((SUM(cost) / SUM(views))* 1000)::DECIMAL(20, 2) AS cpm
            FROM stats
            WHERE date BETWEEN $1 AND $2
            GROUP BY date
            ORDER BY $3;
            """,
            data.from_date,
            data.to_date,
            data.order_by,
        )

    async def delete(self, c: asyncpg.Connection):
        return await c.execute("TRUNCATE stats;")


stats = CRUDStats()
