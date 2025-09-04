
import pyqrcode
import os
import colorama as c
import sqlite3
import random

exit = False

try:
    connection = sqlite3.connect("chess.db")
    cursor = connection.cursor()
    cursor.execute("select * from chess_urls")
except:
    sight_n = ["chess.com", "lichess", "wintrchess", "chessigma", "chessable", "chessreps"]
    sight_l = ["https://www.chess.com", "https://lichess.org", "https://wintrchess.com", "https://www.chessigma.com","https://www.chessable.com", "https://www.chessreps.com"]
    sight_m = ["play", "play", "analys", "analys", "learn", "learn"]
    connection = sqlite3.connect("chess.db")
    cursor = connection.cursor()
    cursor.execute("""
        create table chess_urls(
            sight_name varchar(500),
            sight_link varchar(500),
            sight_mode varchar(500)
        );
    """)
    for x,y,z in zip(sight_n, sight_l, sight_m):
        cursor.execute(f"insert into chess_urls (sight_name , sight_link , sight_mode) values('{x}','{y}','{z}')")
        connection.commit()
finally:
    def menu():
        """
        This is menu of project
        this function help you to choose which kind of sight you want and after that this function connect you to another function
        """
        global user_input
        global exit
        bye_list = ["Have a nice day👋🏻", "Goodbye🥲", "See you soon😊", "Enjoy your day😊"]
        print(f"1.play\n2.free analys\n3.learn\n4.{c.Fore.RED}exit{c.Fore.RESET}")
        user_input = input("Which kind of sight you want?: ")
        while exit == False:
            if user_input in ["1" , "play"]:
                play()
            elif user_input in ["2" , "free analys"]:
                analys()
            elif user_input in ["3" , "learn"]:
                learn()
            elif user_input in ["4" , "exit"]:
                print(f"{c.Fore.CYAN}{random.choice(bye_list)}{c.Fore.RESET}")
                exit = True
                break
            else:
                print(f"{c.Fore.RED}You must to write numbers on the top only{c.Fore.RESET}")
                menu()

    def play():
        """
        this function is search all sight names where there moods are play in the database
        then you can choose one of them to get QR code
        after that function make one QR code then write the path of QR code in your system
        if you check that path in the system or search it on files in system you can see one QR code on system
        """
        global exit
        if exit == False:
            connection = sqlite3.connect("chess.db")
            cursor = connection.cursor()
            cursor.execute("select sight_name from chess_urls where sight_mode = 'play'")
            result = cursor.fetchall() # fetchone only found one item but if you choose fetchall it search for all items
            number = 1
            names = []
            for i in result:
                print(f"{c.Fore.BLUE}{number}.{i[0]}{c.Fore.RESET}")
                names.append(i[0])
                number+=1
            print(f"{c.Fore.GREEN}write the number only{c.Fore.RESET}")
            user_choice = input("which app do you want to choose?: ")
            try:
                if int(user_choice) <= len(names) and user_choice != "0":
                    user_choice = int(user_choice)
                    cursor.execute(f"select sight_link from chess_urls where sight_name = '{names[user_choice-1]}'")
                    result=cursor.fetchone()
                    url = pyqrcode.create(result[0])
                    url.png(f"{names[user_choice-1]} QR code.png")
                    path = os.path.abspath(f"{names[user_choice-1]} QR code.png")
                    print(f"check {path} in your system and scan {names[user_choice-1]} QRcode.png")
                else:
                    print(f"{c.Fore.YELLOW}you must to write numbers on the top{c.Fore.RESET}")
                    play()
            except ValueError:
                print("you must to write numbers only")
            menu()

    def analys():
        """
        this function is like play function
        first it search all sight names where there moods are analys in the database
        then you can choose one of them to get that QR code
        after all that function make that QR code you want
        finally it show you tha path of QR code in your system and if you search path in your files you can see the QR code
        """
        global exit
        if exit == False:
            connection = sqlite3.connect("chess.db")
            cursor = connection.cursor()
            cursor.execute("select sight_name from chess_urls where sight_mode = 'analys'")
            result = cursor.fetchall()
            names = []
            number = 1
            for i in result:
                print(f"{c.Fore.BLUE}{number}.{i[0]}{c.Fore.RESET}")
                names.append(i[0])
                number+=1
            user_choice = input("which app do you want to choose?: ")
            try:
                if int(user_choice) <= len(names):
                    user_choice = int(user_choice)
                    cursor.execute(f"select sight_link from chess_urls where sight_name = '{names[user_choice-1]}'")
                    result = cursor.fetchone()
                    QRcode = pyqrcode.create(result[0])
                    QRcode.png(f"{names[user_choice-1]} QR code.png")
                    path = os.path.abspath(f"{names[user_choice-1]} QR code.png")
                    print(f"check {path} in your system and scan {names[user_choice-1]} QRcode.png")
                else:
                    print(f"{c.Fore.YELLOW}you must to write numbers on the top{c.Fore.RESET}")
                    analys()
            except ValueError:
                print("you must to enter numbers only")
            menu()

    def learn():
        """
        this function is like last 2 function
        first is search all sight names where there moods are learn in database
        then you can choose one of them to get thant QR code
        after that function make that QR code
        and finally it show the QR code path in your system
        """
        global exit
        connection = sqlite3.connect("chess.db")
        cursor = connection.cursor()
        if exit == False:
            cursor.execute("select sight_name from chess_urls where sight_mode = 'learn'")
            result = cursor.fetchall()
            names = []
            numbers = 1
            for i in result:
                names.append(i[0])
                print(f"{c.Fore.BLUE}{numbers}.{i[0]}{c.Fore.RESET}")
                numbers+=1
            user_choice = input("which app do you want to choose?: ")
            try:
                user_choice = int(user_choice)
                if int(user_choice) <= len(names):
                    cursor.execute(f"select sight_link from chess_urls where sight_name = '{names[user_choice-1]}'")
                    result = cursor.fetchone()
                    QRcode = pyqrcode.create(result)
                    QRcode.png(f"{names[user_choice-1]} QRcode.png")
                else:
                    print(f"{c.Fore.YELLOW}you must to write numbers on the top{c.Fore.RESET}")
            except ValueError:
                print("you must to enter numbers only")
            menu()

    menu()