#  y=open("file1.txt","x")
# z=open("file2.txt","x")

y=open("file1.txt","w")
y.write("welcome to futura labs")

y=open("file1.txt","r")
x=y.read()
a=open("file2.txt","w")
a.write(x)




