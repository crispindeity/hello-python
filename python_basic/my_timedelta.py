import datetime
hundred = datetime.timedelta(days=100)
now_hundred = datetime.datetime.now() + hundred
print(now_hundred)

tomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days=1)
print(tomorrow)
