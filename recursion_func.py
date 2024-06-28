# Recursion function : A function which is returning the same function again and again.

def fact(n):
    if n == 1:
        return 1
    
    else:
        return n*fact(n-1)
    
print(fact(7))