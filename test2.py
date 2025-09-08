c1=float(input("enter a speed: "))
c2=float(input("enter another speed: "))
c3=float(input("enter another other speed: "))

sum=c1+c2+c3
avg=sum/3
print(avg)

if c1>avg:
    print("c1 is faster than average")
elif c2>avg:
    print("c2 is faster than average")
else:
    print("c3 is faster than average")