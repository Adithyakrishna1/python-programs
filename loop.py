i=1
while i<=10:
    print(i)
    i+=1

i=1
while i<=20:
    print(i)
    i+=2

i=1
while i<=10:
    print(i)
    if i==5:
        break
    i+=1
i=0
while i<=10:
    i+=1
    if i==5:
        continue
    print(i)
x="apple"
print(x)
print(type(x))
for i in x:
    print(i)

y=(1,2,3,4,5)
print(y)
print(type(y))
for i in y:
    print(i)

z={10,20,30,40,50}
print(z)
print(type(z))
for i in z:
    print(i)

a={"name":"gokul","age":21}
print(a)
for i in a:
    print(i)
for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(11):
    if i==5:
        continue
    print(i)

x=["a","b","c"]         #nestedloop
y=[1,2,3]
for i in x:
    for j in y:
        print(i,j)

for i in x:
    pass








