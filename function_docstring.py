def max(x,y):
    '''
    Prints the maximum of two numbers.
    The two values must be integers.
    '''

    x=int(x)
    y=int(y)

    if x>y:
        print(x,"is maximum.")
    else:
        print(y, "is maximum.")

max(1,2)
print(max.__doc__)
help(max)