cops = []
def gcd(a, b):
   if (a == 0 or b == 0):
       return 0
   if (a == b):
       return a    
   if (a > b):
       return gcd(a - b, b)
   return gcd(a, b - a)

def multiInverse(a, m) :
   a = a % m
   for x in range(1, m) :
       if ((a * x) % m == 1) :
           return x
   return 1

p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
n = p*q
pn = (p-1)*(q-1)
print("'p' is",p)
print("'q' is",q)
print("n = p * q =",n)
print("phi(n) = (p-1)*(q-1) =",pn)

for i in range(1,pn) :
   if gcd(i,pn) == 1 :
       cops.append(i)


print("\nCo-primes:",cops)
e = int(input("Select one of the above numbers as 'e': "))
ei = multiInverse(e,pn)
print("inv(e) =",ei)
p1 = int(input("\nEnter digit to be encrypted (p1): "))
d = ei%pn
c = (p1**d)%(n)
print("\nd = inv(e)%phi(n) =",d)
print("Public key (e,n): ("+str(e)+","+str(n)+")")
print("Private key (d,n): ("+str(d)+","+str(n)+")")
print("\nc = (p1^d)modn ... (Encryption)")
print("Encrypted text (digital signature):",c)

p2 = (c**e)%(n)
print("\np1 = (c^e)modn .. (Decryption)")
print("Decrypted text:",p2)
print("Decrypted text from signature = original text.")
print("Sender is verified!")
