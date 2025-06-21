x=[1,2,3,4,5,6]
print(x)
print(type(x))
print(len(x))
print(3 in x)
print(7 in x)
print(9 not in x)
print(4 not in x)
for i in x:
    print(i)
print(x[1])
print(x[0:5])
print(x[3:])
print(x[:3])
print(x[-1:])
print(x[:-4])
print(x[-4:-1])
x[2]=20
print(x)
x.append(7) #adding new number to the list
print(x)
x.insert(3,8)
print(x)
y=[5,6,7,8,9]
print(y)
x.extend(y) #adding a list to another list
print(x)
x.remove(8) 
print(x)
x.pop(2)
print(x)
x.pop()
print(x)
del x[5]
print(x)
a=["apple","orange","grape","banana"]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
x=a.copy()
print(x)
y=list(x)
print(y)
x=a+y
print(x)
print(x.count("apple"))
x.clear()
print(x)
del a
print(a)
