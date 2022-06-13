from datetime import datetime

# convert string date to timestamp
def date_to_string(date: datetime) -> str:
    print(date.strftime("%Y-%m-%d"))
