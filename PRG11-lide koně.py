def kl (h,k,l,n):
    print(h,"-","Koní =",k,"Lidí =", l)
    for i in range(h):
        k+=4
        l+=2
        print(h,"-","Koní =",k,"Lidí =", l)
        if k+l == n:
            print(k,l, k+l)
            k/=4
            l/=2
            return k,"koní",l,"lidí"

print (kl(22,4,2,72))