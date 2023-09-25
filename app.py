import time
from datetime import datetime, timedelta
import pytz
import scraper_engine
# Define the start and end times in GMT+6 time zone
start_time = datetime.now(pytz.timezone('Asia/Dhaka')).replace(hour=10, minute=30, second=0)
end_time = datetime.now(pytz.timezone('Asia/Dhaka')).replace(hour=23, minute=00, second=0)

# Function to execute the task
def execute_task():
    current_time = datetime.now(pytz.timezone('Asia/Dhaka'))
    if start_time <= current_time <= end_time:
        print("Scraper is running...")
        scraper_engine.scraper_engine() 
        print("Data updated")
    else:
        print("Scraper is closed.")

# Run the task every 5 minutes
while True:
    execute_task()
    time.sleep(300)  # Sleep for 5 minutes (300 seconds)
