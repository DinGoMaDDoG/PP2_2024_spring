from datetime import datetime, timedelta

print("Enter date: (Year-month-day-hour-minutes-seconds)")
x=str(input()).split("-")

print("Enter second date: (Year-month-day-hour-minutes-seconds)")
y=str(input()).split("-")

x1=[]
year, month, day, hour, minutes, seconds= [int(i) for i in x]
year2, month2, day2, hour2, minutes2, seconds2= [int(i) for i in y]
date1=datetime(year, month, day, hour, minutes, seconds)
date2=datetime(year2, month2, day2, hour2, minutes2, seconds2)
print((date2-date1).total_seconds())