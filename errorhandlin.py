
try:
    print(x)
except NameError:
    print("check the variable")
except:
    print("check the code")
finally:
    print("program completed")

try:
    print("hello")
except:
    print("something went wrong")
else:
    print("no error")
finally:
    print("program completed")
x=-5
if x<0:
    raise Exception("negative number")
 



    

