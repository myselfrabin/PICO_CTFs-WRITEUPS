import hashlib

#input_string = "3000"

with open("md5_hash","w") as f:
    for i in range(1,4001,1):
        # Create an MD5 hash object, update it with the encoded string, and get the hexadecimal digest
        s=str(i)
        md5_hash = hashlib.md5(s.encode('utf-8')).hexdigest()

        print(f"{md5_hash}")
    
        f.write(f"{md5_hash}\n")


