from typing import Any

import asyncpg
from fastapi import APIRouter, Depends, Query, status

from app import crud
from app.api import deps
from app.schemas.stats import CreateStats, GetStats, Stats, StatsInDB

router = APIRouter()


@router.post("/", response_model=StatsInDB, status_code=status.HTTP_201_CREATED)
async def create_new_stats(
    *, db: asyncpg.Connection = Depends(deps.get_db), data: CreateStats
) -> Any:
    result = await crud.stats.create(db, data=data)
    return result


@router.get("/", response_model=list[Stats], status_code=status.HTTP_200_OK)
async def show_stats(
    *,
    db: asyncpg.Connection = Depends(deps.get_db),
    from_date=Query(..., alias="from"),
    to_date=Query(..., alias="to"),
    order_by=Query(alias="order-by"),
) -> Any:
    data = GetStats(from_date=from_date, to_date=to_date, order_by=order_by)
    return await crud.stats.show_stats(db, data=data)


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def remove_stats(
    *,
    db: asyncpg.Connection = Depends(deps.get_db),
) -> Any:
    return await crud.stats.delete(db)
