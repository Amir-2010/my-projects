
import time
import pyttsx3
engine=pyttsx3.init()

def menu():
    global menu_question
    print("1.normal timer\n2.upside down timer\n3.exit")
    menu_question=input("what do you want to do?: ")
    while True:
        if menu_question in ["1","normal timer"]:
            normal()
        elif menu_question in ["2","upside down timer"]:
            upside_down()
        elif menu_question in ["3","exit"]:
            break
        else:
            print("your answer must be a ")
            menu_question=input("what do you want to do?: ")

def normal():
    global menu_question
    while True:
        if menu_question not in ["3","exit"] and menu_question in ["1","normal timer"]:
            normal=int(input("time duration: "))
            for i in range(0,normal,1):
                print(f"remaining {i+1} seconds")
                time.sleep(1)
            print("timer is ended")
            engine.say("timer is ended")
            engine.runAndWait()
            menu()
        else:
            break

def upside_down():
    global menu_question
    while True:
        if menu_question not in ["3","exit"] and menu_question in ["2","upside down timer"]:
            normal=int(input("time duration: "))
            for i in range(normal,0,-1):
                print(f"remaining {i} seconds")
                time.sleep(1)
            print("timer is ended")
            engine.say("timer is ended")
            engine.runAndWait()
            menu()
        else:
            break
        
menu()