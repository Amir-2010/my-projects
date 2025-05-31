
def menu():
    global menu_question
    global numbers
    print("1.add \n2.subtract \n3.multiply \n4.divide \n5.exit")
    menu_question=input("what do you want to do?: ").strip()
    while True:
        if menu_question in ["1","add"]:
            add()
        elif menu_question in ["2","subtract"]:
            subtract()
        elif menu_question in ["3","multiply"]:
            multiply()
        elif menu_question in ["4","divide"]:
            divide()
        elif menu_question in ["5","exit"]:
            break
        else:
            print("your choice must be numbers on the top")
            menu()

def add():
    """
    this function do add numbers
    """
    numbers=input("enter your numbers,(separate the numbers with space): ")
    numbers=list(map(float,numbers.split())) # split is for separate your value
    global menu_question
    if menu_question not in ["5","exit"]:
        print(sum(numbers))
        menu()

def subtract():
    """
    this function do subtract numbers
    """
    numbers=input("enter your numbers,(separate the numbers with space): ")
    numbers=list(map(float,numbers.split())) # split is for separate your value
    global menu_question
    if menu_question not in ["5","exit"]:
        result=numbers[0]
        for i in numbers[1:]:
            result-=i
        print(result)
        menu()

def multiply():
    """
    this function to multiply numbers
    """
    global menu_question
    numbers=input("enter your numbers,(separate the numbers with space): ")
    numbers=list(map(float,numbers.split())) # split is for separate your value
    if menu_question not in ["5","exit"]:
        result=1
        for i in numbers:
            result *= i
        print(result)
        menu()

def divide():
    """
    this function do divition numbsers
    """
    numbers=input("enter your numbers,(separate the numbers with space): ")
    numbers=list(map(float,numbers.split())) # split is for separate your value
    global menu_question
    if menu_question not in ["5","exit"]:
        if 0 in numbers[1:]:
            return "Error!!"
        else:
            result=numbers[0]
            for i in numbers[1:]:
                result /= i
            print(result)
            menu()

menu()
