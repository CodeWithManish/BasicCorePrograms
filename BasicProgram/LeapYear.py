
year = int(input("Enter the Number: "))
if((year % 4 == 0) and (year % 100 != 0 ) or(year % 400 == 0)):

    print("this is leap year", year)
else:
    print("this is not Leap year", year)