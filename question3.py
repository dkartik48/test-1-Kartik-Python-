a=int(input("Please enter your salary in Germany in euros: "))
b=str(input("Enter the country you want to migrate to: ")).lower().upper()

def convertsalary():
    if b=="canada":
        c=a*1.49
    elif b=="usa":
        c=a*1.10
    elif b=="combodia":
        c=a*4483.85
    elif b=="united kingdom":
        c=a*0.86
    else:
        print("Country you entered is not acceptable  ")
    return c
c=convertsalary()
if b=="canada":
    if c>56000:
        d="rich"
    else:
        d="poor"
elif b=="usa":
    if c>45000:
        d="rich"
    else:
        d="poor"
elif b=="combodia":
    if c>7649856:
        d="rich"
    else:
        d="poor"
elif b=="united kingdom":
    if c>7649856:
        d="rich"
    else:
        d="poor"
else:
    print("Country you entered is not acceptable  ")
    
print("You will be ",d," in ",b,"with a salary of ",c)