import datetime
import time

print(dir(datetime))

print(datetime.date.today())

# print(datetime.datetime.now())

"""format date and time"""
now = datetime.datetime.now()
print(f'{now:%Y-%m-%d-%H-%M-%S}')
print(f'{now:%Y}')
print(datetime.datetime.today().strftime("%Y"))
print(datetime.datetime.now().strftime("%d-%m-%Y"))  # we can also use datetime.date.today()
print(datetime.datetime.now().strftime("%B"))  # month name2
print(datetime.datetime.now().strftime("%W"))  # week of the year
print(datetime.datetime.now().strftime("%w"))  # weekday of week
print(datetime.datetime.now().strftime("%j"))  # day of year
print(datetime.datetime.now().strftime("%A"))  # day of week

"""convert a string to datetime"""
date = 'apr 15 2021 1:45pm'
converted = datetime.datetime.strptime(date, '%b %d %Y %I:%M%p')
print(converted)

"""current time"""
print(datetime.datetime.now().time())

"""subtract 5 days from current date"""
today = datetime.date.today()
now = datetime.datetime.now()
subtracted = today - datetime.timedelta(5)  # the argument by default is days. we can add hours, min, sec,
# milliseconds or microseconds
print("two hours before now:", now - datetime.timedelta(hours=2))
print("5 days before now", subtracted)

"""
convert unix timestamp string to readable date
A Unix timestamp string is a way of representing a point in time as the number of seconds that have elapsed since 
January 1, 1970, 00:00:00 UTC (Coordinated Universal Time). It is also known as Unix time, POSIX time, or epoch time.
The Unix timestamp string is a widely used standard for representing date and time data in computer systems and 
programming languages, and it is particularly useful for storing and manipulating date and time data in a simple and 
consistent format.
"""
print(datetime.datetime.fromtimestamp(int("1245673456")).strftime("%d-%m-%Y %H:%m:%S"))


# print(datetime.MINYEAR)
# print(datetime.MAXYEAR)

# for i in range(5):
#     time.sleep(1)
#     print(i)
