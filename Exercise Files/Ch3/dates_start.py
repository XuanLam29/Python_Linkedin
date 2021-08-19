#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = date.today()
  print("today is", today)
  # print out the date's individual components
  print("component ",today.day, today.month, today.year )

  # retrieve today's weekday (0=Monday, 6=Sunday)

  print(today.weekday())
  days =["mon","tus","wed","thus","fri","sat","sun"]
  print("index", days[today.weekday()])
  ## DATETIME OBJECTS

  # Get today's date from the datetime class

  today = datetime.now()
  print  ("The current date and time is ", today)
  
  # Get the current time
  t = datetime.time(datetime.now())
  print ("The current time is ", t)
  # Get the current time

 

  
if __name__ == "__main__":
  main();
  