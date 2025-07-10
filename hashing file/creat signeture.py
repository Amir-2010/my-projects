
import hashlib

def create_signature(data, secret_key):
    combined = data + secret_key
    encoded = combined.encode()
    hash_object=hashlib.sha256(encoded)
    hash_signature=hash_object.hexdigest()
    return hash_signature


data = "1237 @ Amir @ 1237"
secret_key = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

my_signature = create_signature(data,secret_key)
print(my_signature)