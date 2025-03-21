from django.test import TestCase

# Create your tests here.


# 8! = 8 * 7!
# 7! = 7 * 6!

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

# print(factorial(7))

n = 8
lista_factorial = [] # (6!, 720), (5!, 120), (4!, 24)
for i in range(n, -1, -1):
    lista_factorial.append((i, factorial(i)))

print(lista_factorial)