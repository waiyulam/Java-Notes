
#!/bin/python
import sys
def factorial(n):
    F = 1
    if n == 0:
        return F
    print("I am calculating the F({}) ... ".format(n))
    F = n * factorial(n-1)
    print("Done, F({}) is equal to {}".format(n,F))
    return F

u_input = int(input("Input a number to compute the factorial:  "))
print(factorial(u_input))