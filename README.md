
## How to Run and Test
```bash
docker compose up --build

#now in another terminal in the same folder

# Test

#Method 1
docker compose exec app python3 birthdays.py ARG

#Method 2 - run the bash script 
docker compose exec app ./birthdays_today.sh
docker compose exec app ./birthdays_next3.sh
docker compose exec app ./birthdays_next3_workdays.sh
```