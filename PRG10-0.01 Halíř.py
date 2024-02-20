def p (p, d):
    d-=1
    x=1
    print(x, "-", p)
    for i in range(d):
        p*=2
        x+=1
        print(x,"-", p)




print (p(0.01, 30 ))