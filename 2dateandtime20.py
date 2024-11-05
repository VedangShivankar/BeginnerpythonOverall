import datetime
import pytz # to run this type "pip install pytz" in terminal to use pytz

#section 1

dt = datetime.datetime(2024, 7, 27, 12, 30, 45, tzinfo=pytz.UTC)
print(dt)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)


#section 2

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
print(dt_utcnow)

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))


for tz in pytz.all_timezones:
    print(tz)

#section 3

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
#print(dt_utcnow)

dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)


#section 4 iso format

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.isoformat())
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'June 21, 2024'
dt = datetime.datetime.strptime(dt_str,'%B %d, %Y' )
print(dt)

