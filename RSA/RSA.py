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
c = (p1**e)%(n)
print("c = (p1^e)modn ... (Encryption)")
print("Encrypted digit:",c)

d = ei%pn
print("\nd = inv(e)%phi(n) =",d)
p2 = (c**d)%(n)
print("p1 = (c^d)modn .. (Decryption)")
print("Decrypted digit:",p2)
