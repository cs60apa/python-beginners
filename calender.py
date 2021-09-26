# python calender module functions
import calendar
# import datetime
# import time

print(calendar.weekheader(2)) #this will print the days from mo-su
print()

print(calendar.weekheader(3)) #this will print the days from mon-sun
print()

print(calendar.firstweekday()) #this will print the index of days
print()

print(calendar.month(2021, 3)) #this will print the days of march 2021
print()

print(calendar.monthcalendar(2021, 3)) #two dimensional array for weeks
print()

print(calendar.calendar(2021)) #this will print the full calender of the year 2021
print()

day_of_the_week = calendar.weekday(2021,3,9)
print(day_of_the_week)
print()

leap = calendar.isleap(2021)#this code will show if the year is the leap
print(leap)

how_many_leap_days = calendar.leapdays(2000,2021)#this codes will show you how many leap days since 2000 upto 2021
print(how_many_leap_days)

#THE END
#try to check out time and datetime modules for calender thats your challenge










