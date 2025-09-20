
import sqlite3
import hashlib
from colorama import Fore

try:
    # in this try, code try to find every thing in database and if code can't find every thing in the database except part is run
    connection = sqlite3.connect("persons.db")
    cursor = connection.cursor()
    cursor.execute("select * from teacher")

except:
    # in except part code make table for the database
    connection = sqlite3.connect("persons.db")
    cursor = connection.cursor()
    cursor.execute("""create table teacher(
        id integer primary key autoincrement,
        user_name varchar(500),
        user_last_name varchar(500),
        national_code text,
        age int,
        salary int
    );""")

    cursor.execute("""create table student(
        id integer primary key autoincrement,
        user_name varchar(500),
        user_last_name varchar(500),
        national_code text,
        age int,
        user_grade int
    );""")
    cursor.execute("""create table manager(
        id integer primary key autoincrement,
        user_name varchar(500),
        user_last_name varchar(500),
        national_code text,
        age int,
        salary int
    );""")

class human:
    """
    this class is parent class
    in the initial method I make many variables for one normal person in the school
    """
    def __init__(self,name,last_name,national_code,age):
        self.name = name
        self.last_name = last_name
        self.national_code = national_code
        self.age = age

class student_class(human):
    """
    this is student class
    this class is child of human class
    in student_detail method I defined grade variable to get students grade in next functions
    """
    def student_detail(self,grade):
        self.grade = grade

class teacher_class(human):
    """
    this is teacher class
    this class is child of human class
    in teacher_detail method I defined salary variable to get teachers salary in next functions
    """
    def teacher_detail(self,salary):
        self.salary = salary

class manager_class(human):
    """
    this is manager class
    this class is the last child of human class
    in manager_detail method I defined salary variable to get managers salary in next functions
    """
    def manager_detail(self,salary):
        self.salary = salary

def hash_password(password):
    """
    this function is change user password to one hash text with 256 character
    I use this function for hash user national code in next functions
    """
    hex = hashlib.sha256(password.encode()).hexdigest()
    return hex

exit_situation = False

def menu():
    """
    this is menu
    menu function help user to find what do they want to do
    after user choose his/her role in school menu send user to one of thees function in the bottom of the code
    """
    global exit_situation
    while True:
        print(f"1.teacher\n2.student\n3.manager\n4.{Fore.RED}exit{Fore.RESET}")
        user_input = input("select your role: ")
        if user_input in ["1","teacher"]:
            teacher_function()
        elif user_input in ["2","student"]:
            student_function()
        elif user_input in ["3","manager"]:
            manager_function()
        elif user_input in ["4","exit"]:
            exit_situation = True
            break
        else:
            print("you must to write numbers on the top")
            user_input = input("select your role: ")

def teacher_function():
    """
    this is teacher function
    this function is get some information from user like name,last name,national code,... for add them to database
    """
    if exit_situation == False:
        user_name = input("what is your name?: ")
        user_last_name = input("what is your last name?: ")
        user_national_code = input("enter your national code: ")
        while True:
            if len(user_national_code) != 10:
                print("your code must have 10 numbers")
                user_national_code = input("enter your national code: ")
            else:
                break
        user_age = input("enter your age: ")
        user_salary = input("how much is your salary?: ")
        teacher = teacher_class(user_name,user_last_name,hash_password(user_national_code),user_age)
        teacher.teacher_detail(user_salary)
        cursor.execute(f"insert into teacher (user_name,user_last_name,national_code,age,salary) values('{teacher.name}','{teacher.last_name}','{teacher.national_code}','{teacher.age}','{teacher.salary}')")
        connection.commit()
        return

def student_function():
    """
    this is student function
    this function is get some information from user like name,last name,national code,... for add them to database
    """
    if exit_situation == False:
        user_name = input("what is your name?: ")
        user_last_name = input("what is your last name?: ")
        user_national_code = input("enter your national code: ")
        while True:
            if len(user_national_code) != 10:
                print("your code must have 10 numbers")
                user_national_code = input("enter your national code: ")
            else:
                break
        user_age = input("enter your age: ")
        user_grade = input("witch grade are you in?: ")
        student = student_class(user_name,user_last_name,hash_password(user_national_code),user_age)
        student.student_detail(user_grade)
        cursor.execute(f"insert into student (user_name,user_last_name,national_code,age,user_grade) values('{student.name}','{student.last_name}','{student.national_code}','{student.age}','{student.grade}')")
        connection.commit()
        return

def manager_function():
    """
    this is manager function
    this function is get some information from user like name,last name,national code,... for add them to database
    """
    if exit_situation == False:
        user_name = input("what is your name?: ")
        user_last_name = input("what is your last name?: ")
        user_national_code = input("enter your national code: ")
        while True:
            if len(user_national_code) != 10:
                print("your code must have 10 numbers")
                user_national_code = input("enter your national code: ")
            else:
                break
        user_age = input("enter your age: ")
        user_salary = input("how much is your salary?: ")
        manager = manager_class(user_name,user_last_name,hash_password(user_national_code),user_age)
        manager.manager_detail(user_salary)
        cursor.execute(f"insert into manager (user_name,user_last_name,national_code,age,salary) values('{manager.name}','{manager.last_name}','{manager.national_code}','{manager.age}','{manager.salary}')")
        connection.commit()
        return

# after try: or except: in line 6 & 13 line 184 run
# this line is like engine of the code to start every thing
menu()