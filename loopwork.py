#sum of first 10 natural numbers using for loop
#factorial of a number
#sum of even numbers in the range of 1-20
#check whether a number is prime number or not
#sum of square of first 10 natural numbers
#fibanocci series
#calculate the average of three numbers



sum=0
for i in range(1,11):
    sum+=i
print(sum)

n=5
r=1
for i in range(1,n+1):
    r*=i
print(r)

x=0
for i in range(1,21):
    if i%2==0:
        x+=i
print(x)

x=0
for i in range(1,11):
    x+=i**2
print(x)

a=(int(input("enter a number:")))
if a==1:
    print("the number is not a prime number")
elif a>1:
    for i in range(2,a):
        if a%2==0:
         print("the number is not a prime ")
         break
        else:
            print("the number is a prime number")

n=10
a,b=0,1
count=0
print(a,end='')
for i in range(1,n):
    print(b,end='')
    c=a+b
    a=b
    b=c



 
