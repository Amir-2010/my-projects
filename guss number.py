
import random
import pyttsx3 as pysound
engine=pysound.init()

def menu():
    """
    this is the menu of the program
    """
    global user_input
    print("select game level")
    print("1.easy\n2.medium\n3.hard\n4.extera hard\n5.exit")
    engine.say("enter your choice")
    engine.runAndWait()
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
            engine.say("your choice isn't in the menu")
            engine.runAndWait()
            print("your choice isn't in the menu")
            engine.say("enter your choice")
            engine.runAndWait()
            user_input=input("enter your choice: ")

def easy():
    """
    this is the easy mode function of the game
    """
    pc_number=random.randint(1,10)
    heart=5
    global user_input
    while heart>=1:
        if user_input not in ["5","exit"]:
            engine.say(f"you have {heart} chabce")
            engine.runAndWait()
            print(f"you have a {heart} chance")
            engine.say("enter a number bethween 1 to 10")
            engine.runAndWait()
            user_input1=int(input("enter a number bethween 1 to 10: "))
            if user_input1 == pc_number:
                print("you win")
                break
            elif user_input1 < pc_number:
                engine.say("the number is bigger thab you think")
                engine.runAndWait()
                print("the number is bigger than you think")
                heart-=1
            elif user_input1 > pc_number:
                engine.say("the number is smaller than you think")
                engine.runAndWait()
                print("the number is smaller than you think")
                heart-=1
        else:
            break
    engine.say(f"computer choice is {pc_number}")
    engine.runAndWait()
    print(f"computer choice is {pc_number}")
    menu()

def meadium():
    """
    this is the medium function of the game
    """
    pc_number=random.randint(1,20)
    global user_input
    heart=5
    while heart>=1:
        if user_input not in ["5","exit"]:
            engine.say(f"you have {heart} chabce")
            engine.runAndWait()
            print(f"you have a {heart} chance")
            engine.say("enter a number bethween 1 to 20")
            engine.runAndWait()
            user_input1=int(input("enter a number bethween 1 to 20: "))
            if user_input1 == pc_number:
                print("you win")
                break
            elif user_input1 < pc_number:
                engine.say("the number is bigger thab you think")
                engine.runAndWait()
                print("the number is bigger than you think")
                heart-=1
            elif user_input1 > pc_number:
                engine.say("the number is smaller than you think")
                engine.runAndWait()
                print("the number is smaller than you think")
                heart-=1
        else:
            break
    engine.say(f"computer choice is {pc_number}")
    engine.runAndWait()
    print(f"computer choice is {pc_number}")
    menu()

def hard():
    """
    this function is for the hard mode of this game
    """
    pc_number=random.randint(1,30)
    global user_input
    heart=5
    while heart>=1:
             if user_input not in ["5","exit"]:
            engine.say(f"you have {heart} chabce")
            engine.runAndWait()
            print(f"you have a {heart} chance")
            engine.say("enter a number bethween 1 to 30")
            engine.runAndWait()
            user_input1=int(input("enter a number bethween 1 to 30: "))
            if user_input1 == pc_number:
                print("you win")
                break
            elif user_input1 < pc_number:
                engine.say("the number is bigger thab you think")
                engine.runAndWait()
                print("the number is bigger than you think")
                heart-=1
            elif user_input1 > pc_number:
                engine.say("the number is smaller than you think")
                engine.runAndWait()
                print("the number is smaller than you think")
                heart-=1
        else:
            break
    engine.say(f"computer choice is {pc_number}")
    engine.runAndWait()
    print(f"computer choice is {pc_number}")
    menu()

def extera_hard():
    """
    this is the last function of the levels
    this is the extera hard function
    """
    pc_number=random.randint(1,40)
    global user_input
    heart=5
    while heart>=1:
              if user_input not in ["5","exit"]:
            engine.say(f"you have {heart} chabce")
            engine.runAndWait()
            print(f"you have a {heart} chance")
            engine.say("enter a number bethween 1 to 40")
            engine.runAndWait()
            user_input1=int(input("enter a number bethween 1 to 40: "))
            if user_input1 == pc_number:
                print("you win")
                break
            elif user_input1 < pc_number:
                engine.say("the number is bigger thab you think")
                engine.runAndWait()
                print("the number is bigger than you think")
                heart-=1
            elif user_input1 > pc_number:
                engine.say("the number is smaller than you think")
                engine.runAndWait()
                print("the number is smaller than you think")
                heart-=1
        else:
            break
    engine.say(f"computer choice is {pc_number}")
    engine.runAndWait()
    print(f"computer choice is {pc_number}")
    menu()

menu()
