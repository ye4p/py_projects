def main(min, max):
    for x in range(min, max):
        print(x, " is a number x")
        n=x
        while n!=1:
            if n %2==0:
                n=n/2
            else:
                n=n*3+1
        print(f"Number {x} got to zero")
    return True
main(2, 100000000)