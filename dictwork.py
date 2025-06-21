
x={"name":"adithyakrishna","age":21,"gender":"male","place":"peringottukara","district":"thrissur"}
print(x)
print(len(x))
print(type(x))
print(x["name"])
print(x.keys())
print(x.values())
print(x.items())
x["district"]="ernalm"
print(x)
x.update({"name":"gokul"})
print(x)
x["phno"]="9876678590"
print(x)
x.update({"college":"sn college"})
print(x)
x.pop("district")
print(x)
x.popitem()
print(x)
del x["gender"]
print(x)
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
a=x.copy()
print(a)
b=dict(x)
print(x)
x.clear()
print(x)
course={"student1":{"name":"gokul","age":21},"student2":{"name":"deepak","age":22}}
print(course)
print(course["student1"])
print(course["student2"]["age"])
print(course["student1"]["name"])