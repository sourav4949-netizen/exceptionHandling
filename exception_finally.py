import logging

logging.basicConfig(filename="mylog.log",level=logging.DEBUG)
try:
    f=open("myfile.txt","w")
    a,b=[int(x) for x in input("enter two integers").split()]
    logging.info("got 2 numbers successfully from users.")
    c=a/b
    f.write("writing %f into file"%c)
except ZeroDivisionError:
    print("division by zero is not allowed")
    print("please enter some non zero number")
    logging.error("Divide by zero encountered while dividing the 2 numbers")
else:
    print("the number is divided and successfully written in the text file.")
finally:
    f.close()
    print("File closed")
print("after exception block")