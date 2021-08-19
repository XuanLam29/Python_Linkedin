#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=2, minutes=56, seconds=30))

# print today's date
now = datetime.now()
print("today " + str(now))

# print today's date one year from now
print("1 year from now " + str(now+ timedelta(days=365)))

print ("in two weeks and 3 days it will be: " + str(now - timedelta(days=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(days=3)
s = t.strftime("%A %B %d, %Y")
print(s)
### How many days until April Fools' Day?
today = date.today()
'''ani = date(today.year, 3,14)
if ani<today:
    print("went by %d day ago"% ((today-ani).days))
    ani = ani.replace(year = today.year +1)
time_to_ani = ani - today
print((time_to_ani.days)," days until next ani")'''

ani = date(2020, 3,14)
print("went by %d day ago"% ((today-ani).days))

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day  

