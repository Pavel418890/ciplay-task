import random
from datetime import datetime, timedelta

MIN_YEAR = 2021


def create_random_stat() -> dict:
    return {
        "date": gen_datetime(),
        "cost": round(random.uniform(42.42, 10000000.00), 2),
        "views": random.randint(1, 99),
        "clicks": random.randint(1, 99),
    }


def gen_datetime(min_year: int = MIN_YEAR, max_year: int = datetime.now().year) -> str:
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return (start + (end - start) * random.random()).strftime("%Y-%m-%d")
