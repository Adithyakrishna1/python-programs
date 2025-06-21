print('hello')
x="hello"
print(x)
print(type(x))
a="""hello,
nice to meet you.
how are u?"""
print(a)
a="hello, world!"
print(a[1])
b="hello, world!"
print(b[2:5])
b="hello, world!"
print(b[-5:-2])
b="hello, world!"
print(len(b))
b="hello, world!"
print(b.strip()) #removes whitespace
a="Hello,World!"
print(a.lower())
a="Hello,World!"
print(a.upper())
a="Hello,World!"
print(a.replace("H","J"))
a="Hello,World!"
print(a.split(","))
txt="Rain in Spain"
x="ain" in txt
print(x)
x="ain" not in txt
print(x)
a="Hello"
b="World"
x=a+b
print(x)
a="Hello"
b="World"
x=a+" "+b
print(x)
age=20
txt="My name is Adithyakrishna, I am {}"
print(txt.format(age))   #method to insert numbers into strings
#example
quantity= 3
itemno= 205
price=50
myorder="I want to pay {2} dollers for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))
