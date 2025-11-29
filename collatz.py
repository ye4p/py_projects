def main(min, max):
    maxSteps=0
    maxX=0
    for x in range(min, max):
        print(x, " is a number x")
        n=x
        count=0
        while n!=1:
            count+=1
            if n %2==0:
                n=n/2
            else:
                n=n*3+1
        print(f"Number {x} got to zero in {count} steps")
        if count>maxSteps:
            maxSteps=count
            maxX=x
    print(f"Biggest num of steps: {maxSteps} for x: {maxX}")
main(2, 1000000)