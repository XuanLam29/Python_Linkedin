#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  now = datetime.now()

  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

  print(now.strftime("year: %y" ))
  print(now.strftime(" %a %b %d"))
  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(now.strftime(" date & time %c"))
  print(now.strftime("%x"))
  print(now.strftime("%X"))
  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(now.strftime("%I:%M:%S %p"))
  print(now.strftime("%H:%M"))
if __name__ == "__main__":
  main();
