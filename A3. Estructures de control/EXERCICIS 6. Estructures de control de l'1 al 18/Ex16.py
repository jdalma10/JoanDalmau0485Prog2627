a = float(input("Costat A: "))
b = float(input("Costat B: "))
c = float(input("Costat C: "))

if a == b and b == c:
    print ("Es equilater.")
elif a == b or a == c or b == c:
    print("Es isoceles.")
elif a>=b and a>=c:
    if a**2 == (b**2)+(c**2):
        print ("Es triangle rectangle.")
elif b>=a and b>=c:
   if b**2 == (a**2)+(c**2):
           print ("Es triangle rectangle.")
elif c>=b  and c>=a:
    if c**2 == (b**2)+(a**2):
        print ("Es triangle rectangle.")
else:
    print("Es escale.")


# if a == b and b == c:
#     print ("Es equilater.")
# elif a == b or a == c or b == c:
#     print("Es isoceles.")

# elif a!=b !=c:
#     print("Es escale.")
# else:
#     if a>=b and a>=c:
#         hipo = a
#         c1 = b
#         c3 = c
    
#     elif b>=a and b>=c:
#         hipo = b
#         c1 = a
#         c3 = c
#     elif c>=b  and c>=a:
#         hipo = c
#         c1 = a
#         c3 = b

#     if hipo**2 == (c1**2)+(c3**2):
#         print ("Es triangle rectangle.")