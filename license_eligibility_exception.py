class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg=msg
class TooOldException(Exception):
    def __init__(self,msg):
        self.msg=msg
age=int(input("Enter your age"))
if age<18:
    raise TooYoungException("You have to be 18 or older to get a driving license")
if age>90:
    raise TooOldException("You have to be younger than 90")
else:
    print("You are eligible")
