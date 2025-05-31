
import string
import random

def security(length):
    caracters=string.digits + string.ascii_letters + string.punctuation
    security_password="".join(random.choice(caracters) for i in range(length))
    
    # you can write line number 7 like here
    # security = ""
    # for i in range(length):
    #     password=random.choice(caracters)
    #     security_password+=password
    
    return security_password

password_length=int(input("how long is your password lenghth?: "))
our_password=security(password_length)
print(our_password)
