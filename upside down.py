
# colors:
# \033[30m --> black
# \033[31m --> red
# \033[32m --> green
# \033[33m --> yellow
# \033[34m --> blue
# \033[35m --> purple
# \033[36m --> turquoise
# \033[37m --> white
# for background use 40 instead of 30 in the code like "\033[40m"

import pyttsx3

number= 0
leave1 = 0
leave2 = 0
leave3 = 0
leave4 = 0
leave5 = 0
leave6 = 0
leave7 = 0
leave8 = 0
engine = pyttsx3.init()

def menu():
    """
    this is menu of the code
    in this function user choose the color of the terminal for run the code
    """
    global number
    reset_color="\033[0m"
    while True:
        if number == 0:
            print("\033[36mhello!!!\033[0m\n\033[36mselect your favorite color from this list\033[0m\n1.\033[46;30mblack\33[0m\n2.\033[31mred\033[0m\n3.\033[32mgrean\033[0m\n4.\033[33myellow\033[0m\n5.\033[34mblue\033[0m\n6.\033[35mpurple\033[0m\n7.\033[36mturquoise\033[0m\n8.\033[37mwhite\033[0m")
            user_color = input(f"\033[36mWhich color is your favorite \033[4;32mto run the code{reset_color}\033[36m in that color?:{reset_color} ")
            if user_color in ["1","black"]:
                number+=1
                black()
            elif user_color in ["2","red"]:
                number+=1
                red()
            elif user_color in ["3","green"]:
                number+=1
                green()
            elif user_color in ["4","yellow"]:
                number+=1
                yellow()
            elif user_color in ["5","blue"]:
                number+=1
                blue()
            elif user_color in ["6","purple"]:
                number+=1
                purple()
            elif user_color in ["7","turquoise"]:
                number += 1
                turquoise()
            elif user_color in ["8","white"]:
                number += 1
                white()
            else:
                print("\033[4;31myou must to enter number on the top!!!\033[0m")
        else:
            break

def black():
    """
    this function is for color black
    all of the prints and inputs are black here but when user want to answer the color change to default color
    """
    global engine

    black_color="\033[46;30m"
    reset_color="\033[0m"

    def name():
        global user_name
        global leave1
        if leave1 == 0:
            engine.say("enter your name:")
            engine.runAndWait()
            user_name = input(f"{black_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{black_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave1
        upside_down_name = user_name[::-1]
        print(f"{black_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave1 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{black_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{black_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave1 += 1
                name()
            else:
                print(f"{black_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()
    name()

def red():
    """
    this function is for color red
    all of the prints and inputs are red here but when user want to answer the color change to default color
    """
    global engine

    red_color="\033[31m"
    reset_color="\033[0m"

    def name():
        global user_name
        global leave2
        if leave2 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{red_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{red_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave2
        upside_down_name = user_name[::-1]
        print(f"{red_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave2 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{red_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{red_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave2 += 1
                name()
            else:
                print(f"{red_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()
    name()

def green():
    """
    this function is for color green
    all of the prints and inputs are green here but when user want to answer the color change to default color
    """
    global engine

    green_color = "\033[32m"
    reset_color = "\033[0m"

    def name():
        global user_name
        global leave3
        if leave3 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{green_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{green_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave3
        upside_down_name = user_name[::-1]
        print(f"{green_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave3 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{green_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{green_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave3 += 1
                name()
            else:
                print(f"{green_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()

    name()

def yellow():
    """
    this function is for color yellow
    all of the prints and inputs are yellow here but when user want to answer the color change to default color
    """
    global engine

    yellow_color = "\033[33m"
    reset_color = "\033[0m"

    def name():
        global user_name
        global leave4
        if leave4 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{yellow_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{yellow_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave4
        upside_down_name = user_name[::-1]
        print(f"{yellow_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave4 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{yellow_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{yellow_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave4 += 1
                name()
            else:
                print(f"{yellow_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()

    name()

def blue():
    """
    this function is for color blue
    all of the prints and inputs are blue here but when user want to answer the color change to default color
    """
    global engine

    blue_color = "\033[34m"
    reset_color = "\033[0m"

    def name():
        global user_name
        global leave5
        if leave5 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{blue_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{blue_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave5
        upside_down_name = user_name[::-1]
        print(f"{blue_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave5 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{blue_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{blue_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave5 += 1
                name()
            else:
                print(f"{blue_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()

    name()

def purple():
    """
    this function is for color purple
    all of the prints and inputs are purple here but when user want to answer the color change to default color
    """
    global engine

    purple_color = "\033[35m"
    reset_color = "\033[0m"

    def name():
        global user_name
        global leave6
        if leave6 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{purple_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{purple_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave6
        upside_down_name = user_name[::-1]
        print(f"{purple_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave6 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{purple_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{purple_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave6 += 1
                name()
            else:
                print(f"{purple_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()

    name()

def turquoise():
    """
    this function is for color turquoise
    all of the prints and inputs are turquoise here but when user want to answer the color change to default color
    """
    global engine

    cyan_color = "\033[36m"
    reset_color = "\033[0m"

    def name():
        global user_name
        global leave7
        if leave7 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{cyan_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{cyan_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave7
        upside_down_name = user_name[::-1]
        print(f"{cyan_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave7 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{cyan_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{cyan_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave7 += 1
                name()
            else:
                print(f"{cyan_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()

    name()

def white():
    """
    this function is for color white
    all of the prints and inputs are white here but when user want to answer the color change to default color
    """
    global engine

    white_color = "\033[37m"
    reset_color = "\033[0m"

    def name():
        global user_name
        global leave8
        if leave8 == 0:
            engine.say("enter your name: ")
            engine.runAndWait()
            user_name = input(f"{white_color}enter your name (in english please):{reset_color} ").lower()
            upside_down()
        else:
            print(f"{white_color}goodbye{reset_color}")
            engine.say("goodbye")
            engine.runAndWait()

    def upside_down():
        global user_name
        global leave8
        upside_down_name = user_name[::-1]
        print(f"{white_color}{upside_down_name}{reset_color}")
        engine.say(f"upside down of your name is {upside_down_name}")
        engine.runAndWait()
        while leave8 == 0:
            engine.say("do you want to try again")
            engine.runAndWait()
            try_again = input(f"{white_color}do you want to try again?:{reset_color} ")
            if try_again in ["yes", "Yes", "YES", "y", "Y"]:
                print(f"{white_color}ok let's do it{reset_color}")
                engine.say("ok let's do it")
                engine.runAndWait()
                name()
            elif try_again in ["No", "no", "NO", "n", "N"]:
                leave8 += 1
                name()
            else:
                print(f"{white_color}you must to answer with yes or no{reset_color}")
                engine.say("you must to answer with yes or no")
                engine.runAndWait()

    name()
    
menu()