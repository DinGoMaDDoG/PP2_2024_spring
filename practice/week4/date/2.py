from datetime import datetime, timedelta

x=datetime.now()
y=x-timedelta(days=1)
z=x+timedelta(days=1)
print(x.strftime("%x"))
print(y.strftime("%x"))
print(z.strftime("%x"))

