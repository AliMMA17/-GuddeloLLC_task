from datetime import date
from typing import List

from fastapi import FastAPI, Query, Path 
from pydantic import BaseModel

from birthdays import (
    mmdd,
    next_calendar_days,
    next_working_days,
    fetch_by_mmdd_list,
    get_conn,
)

app = FastAPI(title="Birthdays API", version="1.0.0")

class Birthday(BaseModel):
    username: str
    birthday: date

def query_birthdays(mmdd_list: List[str]) -> List[Birthday]:
    if not mmdd_list:
        return []
    with get_conn() as conn:
        rows = fetch_by_mmdd_list(conn, mmdd_list)
    out: List[Birthday] = []
    for username, bday in rows:
        if hasattr(bday, "date"):
            bday = bday.date() 
        out.append(Birthday(username=username, birthday=bday))
    return out

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/birthdays/today", response_model=list[Birthday])
def birthdays_today():
    return query_birthdays([mmdd(date.today())])

@app.get("/birthdays/next/{days}", response_model=list[Birthday])
def birthdays_next(days: int = Path(..., ge=1, le=31)):
    return query_birthdays(next_calendar_days(days))

@app.get("/birthdays/next-workdays/{days}", response_model=list[Birthday])
def birthdays_next_workdays(days: int = Path(..., ge=1, le=31)):
    return query_birthdays(next_working_days(days))
