from datetime import datetime, timedelta

x=datetime.now()
five_days=x-timedelta(days=5)

print(x)
print(five_days)