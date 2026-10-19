#9. Algorisme que demani tres nombres i els mostri ordenats (de més a menys);

a = int(input("N1: "))
b = int(input("N2: "))
c = int(input("N3: "))

if a>=b and a>=c:
    if b>c:
        print (a,b,c)
    else:
        print (a,c,b)
elif b>=a and b>=c:
    if a>c:
        print (b,a,c)
    else:
        print (b,c,a)
elif a>=b:
    print (c,a,b)
else:
    print (c,b,a)
print("Fin  del programa")


""" if a > b > c: 
    print (a,b,c)
elif a > c > b:
    .... """