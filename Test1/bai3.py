# in ra các cặp số a,b thỏa mãn 0<=a,b<=1000 sao cho UCLN của 2 số là 1 số nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range (2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

for i in range (0, 11):
    for j in range (i+1, 11):
        if isPrime(math.gcd(i, j)):
            print(f"gcd({i}, {j}) = {math.gcd(i, j)} la snt")
        
    