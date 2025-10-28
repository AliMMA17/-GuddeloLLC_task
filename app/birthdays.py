#!/usr/bin/env python3
import os
import sys
import argparse
from datetime import date, datetime, timedelta
import psycopg2

HEADER = ("UserName", "Birthday")

def mmdd(d: date) -> str:
    return d.strftime("%m-%d")

def next_calendar_days(n: int) -> list[str]:
    today = date.today()
    return [mmdd(today + timedelta(days=i)) for i in range(1, n + 1)]

def next_working_days(n: int) -> list[str]:
    today = date.today()
    res = []
    i = 1
    while len(res) < n:
        d = today + timedelta(days=i)
        if d.weekday() < 5:  # 0=Mon .. 6=Sun
            res.append(mmdd(d))
        i += 1
    return res

def fetch_by_mmdd_list(conn, mmdd_list: list[str]):
    """Query users whose month-day matches any in mmdd_list. Compare month-day only.
    """
    with conn.cursor() as cur:
        sql = """
            SELECT "UserName", ("Birthday"::date) AS bday
            FROM users
            WHERE to_char("Birthday", 'MM-DD') = ANY(%s)
            ORDER BY "UserName";
        """
        cur.execute(sql, (mmdd_list,))
        return cur.fetchall()

def print_table(rows):
    col1_w = max(len(HEADER[0]), *(len(r[0]) for r in rows)) if rows else len(HEADER[0])
    col2_w = len("YYYY-MM-DD")
    print(f"{HEADER[0]:<{col1_w}}  {HEADER[1]:<{col2_w}}")
    print(f"{'-'*col1_w}  {'-'*col2_w}")
    for username, bday in rows:
        if isinstance(bday, datetime):
            bday = bday.date()
        print(f"{username:<{col1_w}}  {bday}")

def get_conn():
    dsn = "host={h} port={p} dbname={db} user={u} password={pw}".format(
        h=os.environ.get("PGHOST", "localhost"),
        p=os.environ.get("PGPORT", "5432"),
        db=os.environ.get("PGDATABASE", "testdb"),
        u=os.environ.get("PGUSER", "testuser"),
        pw=os.environ.get("PGPASSWORD", "testpass"),
    )
    return psycopg2.connect(dsn)

def main():
    parser = argparse.ArgumentParser(
        description="Print users with birthdays today / next 3 days / next 3 working days."
    )
    parser.add_argument(
        "mode",
        choices=["today", "next3", "next3workdays"],
        help="Which list to print."
    )
    args = parser.parse_args()

    if args.mode == "today":
        targets = [mmdd(date.today())]
    elif args.mode == "next3":
        targets = next_calendar_days(3)
    elif args.mode == "next3workdays":
        targets = next_working_days(3)
    else:
        print("Unknown mode", file=sys.stderr)
        sys.exit(2)

    with get_conn() as conn:
        rows = fetch_by_mmdd_list(conn, targets)
    print_table(rows)

if __name__ == "__main__":
    main()
