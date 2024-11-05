x = input("num 1 ")
y= input("num 2  ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print("an exception has occoured :", e)
    z = None
except TypeError as e:
    print("type error")
print("division is",z)