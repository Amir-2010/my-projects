
import hashlib

text = "hello"
encoded_text = text.encode() # changing string to bite
hash_object = hashlib.sha256(encoded_text) # making one object for hash
hex = hash_object.hexdigest() # change 'text' variable to hexadecimal
print(hex) # hex_output = 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
#########