import time
import hashlib
with open('message1.txt', 'r') as message:
    msg = message.read()
    t1 = time.clock()
    hash_md5 = hashlib.md5(msg.encode()).hexdigest()
    t2 = time.clock()
    tm1 = t2 - t1
    tm11 = tm1
    t1 = time.clock()
    hash_sha1 = hashlib.sha1(msg.encode()).hexdigest()
    t2 = time.clock()
    tm2 = t2 - t1
    tm12 = tm2
    print("File1:\nTime:\nMD5:",tm1,"SHA1:",tm2)
    print("Size (bits):\nMD5:",len(hash_md5)*4,"SHA1:",len(hash_sha1)*4)
    print("MD5 Hash:",hash_md5)
    print("SHA1 Hash:",hash_sha1,"\n")
with open('message2.txt', 'r') as message:
    msg = message.read()
    t1 = time.clock()
    hash_md5 = hashlib.md5(msg.encode()).hexdigest()
    t2 = time.clock()
    tm1 = t2 - t1
    tm21 = tm1
    t1 = time.clock()
    hash_sha1 = hashlib.sha1(msg.encode()).hexdigest()
    t2 = time.clock()
    tm2 = t2 - t1
    tm22 = tm2
    print("File2:\nTime:\nMD5:",tm1,"SHA1",tm2)
    print("Size (bits):\nMD5:",len(hash_md5)*4,"SHA1:",len(hash_sha1)*4)
    print("MD5 Hash:",hash_md5)
    print("SHA1 Hash:",hash_sha1,"\n")
with open('message3.txt', 'r') as message:
    msg = message.read()
    t1 = time.clock()
    hash_md5 = hashlib.md5(msg.encode()).hexdigest()
    t2 = time.clock()
    tm1 = t2 - t1
    tm31 = tm1
    t1 = time.clock()
    hash_sha1 = hashlib.sha1(msg.encode()).hexdigest()
    t2 = time.clock()
    tm2 = t2 - t1
    tm32 = tm2
    print("File3:\nTime:\nMD5:",tm1,"SHA1",tm2)
    print("Size (bits):\nMD5:",len(hash_md5)*4,"SHA1:",len(hash_sha1)*4)
    print("MD5 Hash:",hash_md5)
    print("SHA1 Hash:",hash_sha1)
