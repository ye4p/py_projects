x=int(input("Enter value of initial number: "))

while x!=1:
    if x %2==0:
        x=x/2
    else:
        x=x*3+1
    print("x value is: ",x)
print('X is 1!')