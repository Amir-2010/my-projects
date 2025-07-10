
import hashlib

def hash_password(password):
    encoded= password.encode()
    hash_obj= hashlib.sha3_256(encoded)
    hashed = hash_obj.hexdigest()
    return hashed

user_password="68f1927d51ddd7b49c381c7c7d006b813565e3b95f09136cdfc96f529a352a4e"

user_input = input("enter your password: ")
hash=hash_password(user_input)
if hash_password(user_input) == user_password:
    print("It's correct")
    print("welcome")
else:
    print("It's wrong")