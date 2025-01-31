#FutureTime.py
#Name:Cooper Kinnan
#Date:1/30/2025
#Assignment:Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute
Question1 = input("What hour is it?")
Question2 = input("What minute is it?")
Question3 = input("How many hours into the future do you want to see?")
Question4 = input("How many minutes into the future do you want to see?")
hourCurrent = int(Question1)
minuteCurrent = int(Question2)
extraHour = (minuteCurrent + int(Question4))//60
hourFuture = (hourCurrent + int(Question3) + extraHour)%24
minuteFuture = (minuteCurrent + int(Question4))%60
print(hourFuture, ":", minuteFuture)



if __name__ == '__main__':
  main()
