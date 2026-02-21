# leap year 
# 20240802652
year = int(input("enter the year :"))

rem1 = year % 4
rem2 =year % 100 
rem3 = year % 400 

if rem3 == 0:
    print("leap year ")
else:
    if rem1 == 0 and  rem2 !=0:
        print ("leap year ")
    else:
        print ("not a leap year ")