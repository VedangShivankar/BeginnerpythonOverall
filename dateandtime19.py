import datetime


today = datetime.date.today()
print(today)
print(today.year) # can also use ".day" and ".month"
print(today.weekday())


tdelta = datetime.timedelta(days=7)

#section 2 timedeltas


today = datetime.date.today()



tdelta = datetime.timedelta(days=7)

print(today + tdelta)

#section 3 calculations

today = datetime.date.today()

tdelta = datetime.timedelta(days=7)

day = datetime.date(2025, 9, 24)

till_bday = bday - today
print(till_bday)


#section 4 datetime.time

t = datetime.time(10 , 40 , 58 , 100000)
print(t)

#section 5

z = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
print(z)
print(z.time())
print(z.date())

tdelta2 = datetime.timedelta(days=7) #you can do "hours = ___ (amount of hours)"
print(z+tdelta2)

#section 6

x_today = datetime.datetime.today()
x_now = datetime.datetime.now()
x_utcnow = datetime.datetime.utcnow()

print(x_today)
print(x_now)
print(x_utcnow)