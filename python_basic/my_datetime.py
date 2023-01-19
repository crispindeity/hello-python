import datetime

start_time = datetime.datetime.now()
print(start_time)

updated_date_time = start_time.replace(year=2023, month=2, day=1)
print(updated_date_time)

custom_datetime = datetime.datetime(2023, 1, 28)
print(custom_datetime)

how_long = custom_datetime - datetime.datetime.now()
print(how_long.days)
