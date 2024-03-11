# tìm các số nguyên tố và tổng các số này trong khoảng (a,b)
import math

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range (2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


a = int(input("Nhap a = "))
b = int(input("Nhap b = "))

sum = 0

for i in range (a, b + 1):
    if isPrime(i):
        sum += i
print(f"Tong cac snt tu ({a}, {b}) =  {sum}")
    
