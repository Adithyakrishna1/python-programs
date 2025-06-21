def welcome(x):
    print(x)
    for i in x:
        print(i)
y=["apple","grape","orange","banana"]
welcome(y)

def num(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
    print(sum)
y=int(input("enter a number"))
num(y)

# pick even numbers form a list
# pick odd numbers form a list
# number list,square list
# factorial of a number using function
# palindrome
# fibonacci using function
# prime number using function

x=[1,2,3,4,5,6,7,8,9,10]
y=list(filter(lambda a:a%2==0,x))
print(y)

z=list(filter(lambda b:b%2==1,x))
print(z)






    
    