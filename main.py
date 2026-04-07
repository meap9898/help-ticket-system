import os
import sys

def get_path(filename):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, filename)
while True:
    print("*" * 51)
    print("*************Help Ticket pre-screening*************")
    print("***********When you submit a help ticket***********")
    print("*************Follow the instructions***************")
    print("******and attach screenshots to the ticket*********")
    print("*****************pick your problem*****************")
    print("*" * 51)
    print("1: Apps dont work \n2: Internet's not working \n3: Sound not working")
    x = input("enter your problem or \"q\" to exit: ")
    if x == "1":
        with open(get_path('appsnoworkie.txt'),'r') as mydata:
            print(mydata.read())
    elif x == "2":
        with open(get_path('internetbroke.txt'),'r') as mydata:
            print(mydata.read())
    elif x == "3":
        with open(get_path('no sound.txt'),'r') as mydata:
            print(mydata.read())
    elif x == "q":
        break
    else:
        print("you picked something out of scope")