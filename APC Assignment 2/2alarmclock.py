# 20240802660
day_vac = eval(input("enter the input : " ))

weekdays = [1,2,3,4,5]
weekend = [6,7]

if day_vac[1]== False:
    if day_vac[0] in weekdays:
        print("07:00")
    elif day_vac[0] in weekend :
        print("10:00")
    else:
        print ("invalid number ")

elif day_vac [1]== True:
    if day_vac[0] in weekdays :
        print("10:00 ")
    elif day_vac[0] in weekend:
        print("off")
    else:
        print("invalid number")