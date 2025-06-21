



sum=0
for i in range(1,11):
    sum+=i
print(sum)

x=0
for i in range(1,11):
    x+=i**2
print(x)

x=int(input("enter a number"))
r=1
for i in range(1,x+1):
    r*=i
print(r)

#fibonacci
a=0    
b=1
print(a)
print(b)
for i in range(0,10):
    print(a+b)
    c=a
    a=b
    b=c+b