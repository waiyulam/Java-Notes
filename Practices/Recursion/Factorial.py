
#!/bin/python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

u_input = int(input("Input a number to compute the factorial:  "))
print(factorial(u_input))