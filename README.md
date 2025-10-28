
## How to Run and Test
```bash
docker compose --env-file .env up  --build

#now in another terminal 

# Run
python app/birthdays.py today
python app/birthdays.py next3
python app/birthdays.py next3workdays
```