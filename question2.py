RED = "red"
BLUE = "blue"
YELLOW = "yellow"

a=str(input("Enter color 1: ")).lower()
if a==RED or a==BLUE or a==YELLOW:
    print("Color 1: ",a)
else:
    print("Error: Invalid Colour1.")
b=str(input("Enter color 2: ")).lower
if b==RED or b==BLUE or b==YELLOW:
    print("Color 2: ",b)
else:
    print("Error: Invalid Colour2.")

if a==RED and b==RED or a==BLUE and b==BLUE or a==YELLOW and b==YELLOW:
    print("Error: The two colours you entered are the same.")
else:
    
    if a==RED or a==BLUE or a==YELLOW:
        if a==RED and b==BLUE:
            c="purple"
            print("Final Color: ",c)
        elif a==RED and b==YELLOW:
            c="orange"
            print("Final color: ",c)
        elif a==BLUE and b==RED:
            c="purple"
            print("Final Color: ",c)
        elif a==BLUE and b==YELLOW:
            c="green"
            print("Final Color: ",c)
        elif a==YELLOW and b==RED:
            c="orange"
            print("Final Color: ",c)
        elif a==YELLOW and b==BLUE:
            c="green"
            print("Final Color: ",c)
    else:
        print("INVALID")

