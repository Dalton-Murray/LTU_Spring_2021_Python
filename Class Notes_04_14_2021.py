#####################
## Dalton Murray    #
## 04/14/20201      #
## Class notes      #
#####################

def message(times):
    if times > 0:
        print("Hello World!")
        message(times-1)
message(5)

import math
print(math.factorial(1))

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1)*num

print(factorial(3))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(7))

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)
print(gcd(3, 9))