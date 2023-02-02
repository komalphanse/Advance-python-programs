import datetime #returns the current datetime object
print(datetime.datetime.now())
#return the date time object for the specified date
print(datetime.datetime(2020,12,4))
#return the date time object for the specified time
print(datetime.datetime(2020,4,4,1,26,40))
d1=datetime.datetime(2018,5,3)
d2=datetime.datetime(2018,6,1)
print("d1 is greater than d2:",d1>d2)
print("d1 is less than d2:",d1<d2)
print("d1 is not equal to d2:",d1!=d2)