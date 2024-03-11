# viết chương trình tìm 2 số nguyên tố nhỏ hơn hoặc bằng n sao cho tổng và hiệu là 1 số nguyên tố
import math

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range (2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
n = int(input("Nhap n = "))
primes = []
for i in range (n + 1):
    if isPrime(i):
        primes.append(i)

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        sum = primes[i] + primes[j]
        diff = abs(primes[i] - primes[j])
        if isPrime(sum) and isPrime(diff):
            print(f"Hai so co tong va hieu la snt: ({primes[i]}, {primes[j]})")
