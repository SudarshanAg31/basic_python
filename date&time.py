import datetime
today=datetime.date.today()
print(today)#for current date
time=datetime.datetime.now()
print(time)#for current date & time
time=time.strftime("%H:%M:%S %m-%d-%Y")
print(time)# change format of date and time

print("Example")

target_datetime=datetime.datetime(2020,1,31,12,0,0)
current_time=datetime.datetime.now()
if target_datetime<current_time:
    print("target passed")
else:
    print("target is not passed")