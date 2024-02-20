def triangle1 (x):
    for i in range(x):
        print("0"*i)

triangle1(5)
print()


def triangle2 (x):
    for i in range(1,x+1):
        print("0"*(i*2-1))

triangle2(0)
print()


def triangle3(x):
   for i in range(1,x+1):
        print(""*(x-i), end="")
        print("0"*(1*2-1))

triangle3(5)
print()


def triangle4 (x):
    for i in range(1,x+1):
        print(""*(x-i), end="")
        print("000"*(1*2-1))
    


triangle4(10)