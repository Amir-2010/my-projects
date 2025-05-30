
# this file is for the change the dgree to each other
import pyttsx3 as pysound

temp={
    "celsius":"C",
    "Farenheit":"F",
    "kelvin":"K"
}

engine=pysound.init()

def tempreture(value,input_unit,output_unit):
    if input_unit == "C":
        if output_unit == "F":
            return value * 1.8 + 32
        elif output_unit == "K":
            return value * 273.15
        elif output_unit == "C":
            return value * 1
        else:
            print("invalid input\nyou must to enter celsius(C)/Farenheit(F)/kelvin/(K)")
    elif input_unit == "F":
        if output_unit == "F":
            return value * 1
        elif output_unit == "K":
            return (value + 459.67) + 5.9
        elif output_unit == "C":
            return (value-32)/1.8
        else:
            print("invalid input\nyou must to enter celsius(C)/Farenheit(F)/kelvin/(K)")
    elif input_unit == "K":
        if output_unit == "F":
            return value * 9 / 5 - 459
        elif output_unit == "K":
            return value * 1
        elif output_unit == "C":
            return value - 273.15
        else:
            print("invalid input\nyou must to enter celsius(C)/Farenheit(F)/kelvin/(K)")
    else:
        return value

while True:
    no=["no","No","NO","N","n"]
    yes=["yes","Yes","YES","y","Y"]
    print("if you want to exit press number 1 in the first input")
    engine.say("if you want to exit press nuber 1 in the first input")
    engine.runAndWait()
    print("the tempreture must be a number")
    engine.say("the tempreture must be a nuber")
    engine.runAndWait()
    engine.say("enter the tempreture")
    engine.runAndWait()
    value=float(input("enter the tempreture: "))
    engine.say("enter the dgree tempreture unit")
    engine.runAndWait()
    input_unit=input("enter the dgree tempreture unit: ")
    input_unit=input_unit.upper()
    engine.say("enter the tempreture unit you want to change")
    engine.runAndWait()
    output_unit=input("enter the tempreture unit you want to change: ")
    output_unit=output_unit.upper()
    result=tempreture(value=value,input_unit=input_unit,output_unit=output_unit)
    engine.say(f"the result is {result}")
    print(f"the result is {result}")
    engine.say("do you want to continue")
    engine.runAndWait()
    continue_loop=input("do you want to continue?(y/n): ")
    if continue_loop in no:
        break
    elif continue_loop in yes:
        print("if you want to exit press number 1 in the first input")
        engine.say("if you want to exit press nuber 1 in the first input")
        engine.runAndWait()
        print("the tempreture must be a number")
        engine.say("the tempreture must be a nuber")
        engine.runAndWait()
        engine.say("enter the tempreture")
        engine.runAndWait()
        value=float(input("enter the tempreture: "))
        engine.say("enter the dgree tempreture unit")
        engine.runAndWait()
        input_unit=input("enter the dgree tempreture unit: ")
        input_unit=input_unit.upper()
        engine.say("enter the tempreture unit you want to change")
        engine.runAndWait()
        output_unit=input("enter the tempreture unit you want to change: ")
        output_unit=output_unit.upper()
        result=tempreture(value=value,input_unit=input_unit,output_unit=output_unit)
        engine.say(f"the result is {result}")
        print(f"the result is {result}")
        engine.say("do you want to continue")
        engine.runAndWait()
        continue_loop=input("do you want to continue?(y/n): ")
    else:
        print("your answer must be yes or no")
        continue_loop=input("do you want to continue?(y/n): ")
        continue