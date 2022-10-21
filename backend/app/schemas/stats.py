import re
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, validator


class BaseStats(BaseModel):
    date: date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[float] = None


class CreateStats(BaseStats):
    @validator("cost")
    def check_cost(cls, cost: float):
        correct_cost = re.match(r"\d+(?:[.]\d{2})?$", str(cost))
        if correct_cost is None:
            raise ValueError("Invalid cost")
        return cost


class GetStats(BaseModel):
    from_date: str
    to_date: str
    order_by: Optional[str] = None

    @validator("order_by")
    def check_order_by(cls, v: str) -> str:
        if v not in ("date", "cost", "views", "clicks"):
            raise ValueError("Allowed fields (date, views, clicks, cost)")
        return v

    @validator("from_date", "to_date")
    def check_is_date(cls, date: str) -> date:
        try:
            parsed = datetime.strptime(date, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            raise
        else:
            return parsed


class Stats(BaseStats):
    cpc: Optional[float]
    cpm: Optional[float]


class StatsInDB(BaseStats):
    id: int
