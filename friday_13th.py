#Given the month and year as numbers, check whether that month contains a 'Friday 13th'.
import calendar
month,year = input().split(",")
val = calendar.weekday(int(year),int(month),13)
if val ==4 :
    print("True")
else:
    print("False")