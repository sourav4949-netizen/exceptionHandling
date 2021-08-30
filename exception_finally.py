try:
    f=open("myfile.txt","w")
    a,b=[int(x) for x in input("enter two integers").split()]
    c=a/b
    f.write("writing %f into file"%c)
except ZeroDivisionError:
    print("division by zero is not allowed")
    print("please enter some non zero number")
else:
    print("the number is divided and successfully written in the text file.")
finally:
    f.close()
    print("File closed")
print("after exception block")