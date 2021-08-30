try:
    a,b=[int(x) for x in input("enter two integers").split()]
    c=a/b
    print(c)
except ZeroDivisionError:
    print("division by zero is not allowed")
    print("please enter some non zero number")
print("after exception block")