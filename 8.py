#8. Write the python program to test whether a given year is leap year or not
x=int(input("Enter any year:"))
if((x%400==0)or(x%100!=0)and(x%4==0)):
    print("It is a leap year")
else:
    print("Not a leap year")
