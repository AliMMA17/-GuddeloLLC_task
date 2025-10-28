
## How to Run and Test
```bash
docker compose --env-file .env up  --build

#now in another terminal in the same folder

# Run
docker compose exec app ./birthdays_today.sh
docker compose exec app ./birthdays_next3.sh
docker compose exec app ./birthdays_next3_workdays.sh
```