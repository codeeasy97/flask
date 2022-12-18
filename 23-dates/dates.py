#Python Datetime

#Date Output

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
#Creating Date Objects
x = datetime.datetime(2022,4,12)
print(x)

#The strftime() Method

x = datetime.datetime(2022,7,13)
print(x.strftime("%p"))

#Ex:-
"""
1. %a	Weekday, short version	Wed
2. %A	Weekday, full version	Wednesday
3. %d	Day of month 01-31	31	
4. %b	Month name, short version	Dec	
5. %B	Month name, full version	December
6. %m	Month as a number 01-12	12	
7. %y	Year, short version, without century	18	
8. %Y	Year, full version	2018
9. %p	AM/PM	PM	
10. %M	Minute 00-59	41	
11. %S	Second 00-59	08
"""