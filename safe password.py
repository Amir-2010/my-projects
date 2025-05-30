
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

our_password=security(10)
print(our_password)
