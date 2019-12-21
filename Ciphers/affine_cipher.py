def multiInverse(a, m) :
   a = a % m
   for x in range(1, m) :
       if ((a * x) % m == 1) :
           return x
   return 1
alpha = 'abcdefghijklmnopqrstuvwxyz'

k1 = int(input("Enter key for multiplication: "))
k2 = int(input("Enter key for addition: "))
k1i = multiInverse(k1, 26)
msg = input("Enter the message: ")
enc = ""

for i in msg :
   if i == " " :
       enc = enc + i
   enc = enc + alpha[(alpha.find(i)*k1+k2)%26]
print("Encrypted text: " + enc.upper())
dec = ""
for i in enc :
   if i == " " :
       dec = dec + i
   dec = dec + alpha[((alpha.find(i)-k2)*k1i)%26]
print("Decrypted text: " + dec)

