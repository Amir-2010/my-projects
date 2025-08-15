
exit_variable = False

while exit_variable == False:
    #this loop is continiue while user don't whant to continiue
    try:
        user_number = float(input("enter one decimal number: "))
        low_number = int(user_number)
        high_number = int(user_number) + 1
        if user_number-low_number < high_number-user_number:
            print(f"the nearest number to {user_number} is {low_number}")
        elif user_number-low_number > user_number-high_number:
            print(f"the nearest number to {user_number} is {high_number}")
        try_again = input("do you want to try again: ")
        while True:
            if try_again in ["yes","Yes","YES","y","Y"]:
                print("ok")
                break
            elif try_again in ["no","No","NO","N","n"]:
                print("goodbye👋🏻")
                exit_variable = True
                break
            else:
                print("you must to answer with yes or no")
                try_again = input("do you want to try again: ")
    except ValueError:

        print("you must to enter number \033[31mnot letter\033[0m😏\ntry again please")
