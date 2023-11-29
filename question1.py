a=int(input("Enter the month in the numeric form: "))
if a>12 or a==0 or a<0:
    print("Error: Invalid Month Input")  
else:
    print("Month: ",a)
b=int(input("Enter the day in numeric form: "))
if b>31 or b==0 or b<0:
    print("Error: Invalid Day Input")
else:
    print("Day: ",b)
c=int(input("Enter the year in two numeric digits (for example: 98, 20, 21): "))
if c>99 or c<0:
    print("Error: Invalid Year Input")
else:
    print("year: ",c)
    
if a==2:
    if c%4==0:
        if 0>b>29:
            print("Error: There is no such date in the calendar.")
        else:
            print("Success: Congratulations! You entered a correct date & the date is ",b,"/",a,"/",c)
    else:
        if 0>b>28:
            print("Error: There is no such date in the calendar.")
        else:
            print("Success: Congratulations! You entered a correct date & the date is ",b,"/",a,"/",c)
elif a==1 or a==3 or a==5 or a==7 or a==9 or a==11:
    print("Success: Congratulations! You entered a correct date & the date is ",b,"/",a,"/",c)
else:
    print("Success: Congratulations! You entered a correct date & the date is ",b,"/",a,"/",c)