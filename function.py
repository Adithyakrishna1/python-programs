# def sample():
#     x=2
#     print(x)
# sample()

# def hello():
#     a=10
#     b=20
#     x=a+b
#     print(x)
# hello()

# def name(x):
#     print(x)
# name("gokul")

# def x(a,b):
#     y=a+b
#     print(y)
# x(2,3)

# #arbitrary arguments
# def hello(*x): 
#     print(x[2])
# hello("apple","orange","banana","grape",)

# #keyword arguments
# def name(x,y,z):
#     print(x)
# name(x=2,y=4,z=6)

# #arbitrary keyword arguments
# def wow(**x):
#     print(x["a"])
# wow(a=10,b=20,c=30,d=40)

# def helloo(x=12):
#     print(x)
# helloo(10)
# helloo()

# def help(x,y):
#     return x-y
# print(help(5,7))

# def come():
#     pass

a=lambda x,y:x+y
print(a(10,20))

x=lambda a,b,c:a+b+c
print(x(1,2,3))

x=["apple","orange","grape","pineapple","banana"]
y=list(map(lambda z:z.upper(),x))
print(y)

a=[2,4,6,8,10,12,14,16]
b=list(filter(lambda x:x>10,a))
print(b)
