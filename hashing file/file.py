
import hashlib

def hash_file(file_name):
    hash = hashlib.blake2s()
    with open(file_name,"rb") as file: # rb = read only & Binary
        # in line 8 ":=" is check file is end or no and add this to hash value and read it and if it's not ending the code is add file fo hash value continue it
        while slice_file:=file.read(1024):
            hash.update(slice_file)
        # while True:
        #   slice_file = file.read(1024)
        #   if not slice_file:
        #       break
    return hash.hexdigest()

file_name = hash_file("hash.py")
print(file_name)

# with out '#########' = 73744f5afde53e0292912b18aab13e62ddb0da62daa95acff4fbc9c92d584502

# with '#########' = 944c9d0f78d9f99f2c707f12a32b034f72934a12bc982eff9a0abd20a2819d73

# with blank2b = 6630a40ff5a22fcfde09aad37f4e203665b8d6909c69fafdb6ec593f34ee6648b618d04a28cc34f0298a31a9f7539407997167ffdf3e9a3e4d03ce94030e2266

# with blank2s = bcddf77e47a85ce6138ac84583efccef64aec413f74d0a1268d03b8fe44ff3ec