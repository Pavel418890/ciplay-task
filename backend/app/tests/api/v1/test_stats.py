import datetime

import asyncpg
import httpx

from app.crud.stats import stats
from app.schemas.stats import StatsInDB
from app.tests.utils.stats import MIN_YEAR, create_random_stat


async def test_create_stat(db: asyncpg.Connection, client: httpx.AsyncClient):
    data = create_random_stat()
    response = await client.post("/stats/", json=data)
    result = response.json()
    stat = await stats.get_by_id(db, id_=result["id"])
    stat = StatsInDB(**stat)
    assert response.status_code == 201
    assert stat
    date = datetime.datetime.strptime(data["date"], "%Y-%m-%d").date()
    assert stat.date == date
    assert stat.cost == data["cost"]
    assert stat.views == data["views"]
    assert stat.clicks == data["clicks"]


async def test_show_stats(client: httpx.AsyncClient):
    for _ in range(10):
        data = create_random_stat()
        await client.post("/stats/", json=data)

    from_ = f"{MIN_YEAR}-01-01"
    to = f"{datetime.datetime.now().strftime('%Y-%m-%d')}"
    response = await client.get(
        f"/stats/?from={from_}&to={to}&order-by=cost",
    )
    result = response.json()
    assert response.status_code == 200
    assert result


async def test_delete_stats(db: asyncpg.Connection, client: httpx.AsyncClient):
    response = await client.delete("/stats/")
    assert response.status_code == 204
    assert await db.fetchrow("SELECT * FROM stats WHERE id IS NOT NULL;") is None
