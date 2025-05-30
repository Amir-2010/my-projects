
import random
import pyttsx3 as pysound
engine=pysound.init()

def menu():
    global user_input
    print("select game level")
    print("1.easy\n2.medium\n3.hard\n4.extera hard\n5.exit")
    user_input=input("enter your choice: ")
    while True:
        if user_input in ["1","easy"]:
            easy()
        elif user_input in ["2","medium"]:
            meadium()
        elif user_input in ["3","hard"]:
            hard()
        elif user_input in ["4","extera hard"]:
            extera_hard()
        elif user_input in ["5","exit"]:
            break
        else:
            print("your choice isn't in the menu")
            user_input=input("enter your choice: ")

def easy():
    pc_number=random.randint(1,10)
    heart=5
    global user_input
    while heart>=1:
        if user_input not in ["5","exit"]:
            print(f"you have a {heart} chance")
            user_input1=int(input("enter a number bethween 1 and 10: "))
            if user_input1 == pc_number:
                print("you win")
                break
            elif user_input1 < pc_number:
                print("the number is bigger than your number")
                heart-=1
            elif user_input1 > pc_number:
                print("the number is smaller than your number")
                heart-=1
        else:
            break
    print(f"computer choice is {pc_number}")
    menu()

def meadium():
    pc_number=random.randint(1,20)
    global user_input
    heart=5
    while heart>=1:
        if user_input not in ["5","exit"]:
            print(f"you have a {heart} chance")
            user_input2=int(input("enter a number bethween 1 and 20: "))
            if user_input2 == pc_number:
                print("you win")
            elif user_input2 < pc_number:
                print("the number is bigger than your number")
                heart-=1
            elif user_input2 > pc_number:
                print("the number is smaller than your number")
                heart-=1
        else:
            break
    print(f"computer choice is {pc_number}")
    menu()

def hard():
    pc_number=random.randint(1,30)
    global user_input
    heart=5
    while heart>=1:
        if user_input not in ["5","exit"]:
            print(f"you have a {heart} chance")
            user_input3=int(input("enter a number bethween 1 and 30: "))
            if user_input3 == pc_number:
                print("you win")
            elif user_input3 < pc_number:
                print("the number is bigger than your number")
                heart-=1
            elif user_input3 > pc_number:
                print("the number is smaller than your number")
                heart-=1
        else:
            break
    print(f"computer choice is {pc_number}")
    menu()

def extera_hard():
    pc_number=random.randint(1,40)
    global user_input
    heart=5
    while heart>=1:
        if user_input not in ["5","exit"]:
            print(f"you have a {heart} chance")
            user_input4=int(input("enter a number bethween 1 and 40: "))
            if user_input4 == pc_number:
                print("you win")
            elif user_input4 < pc_number:
                print("the number is bigger than your number")
                heart-=1
            elif user_input4 > pc_number:
                print("the number is smaller than your number")
                heart-=1
        else:
            break
    print(f"computer choice is {pc_number}")
    menu()

menu()