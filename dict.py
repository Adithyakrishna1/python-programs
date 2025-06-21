x={"name":"adithyakrishna","age":21,"gender":"male","place":"peringottukara","district":"thrissur"}
print(x)
print(len(x))
print(type(x))
print(x["name"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
print("name" not in x)
x["district"]="ernalm"
print(x)
x.update({"name":"vishnu"})
print(x)
x["postoffice"]="kizhakkummuri"
print(x)
x.update({"college":"sngc"})
print(x)
x.pop("place")
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
y=x.copy()
print(y)
z=dict(x)
print(z)
x.clear()
print(x)
print(x)
family={"child1":{"name":"gokul","age":21,},"child2":{"name":"surya","age":20},"child3":{"name":"deepak","age":22}}
print(family)
print(family["child2"])
print(family["child2"]["age"])
print(family["child3"]["name"])