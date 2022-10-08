print("-----------------------")
print("-------FIBONACCI-------")
print("-----------------------")

a = 0
b = 1
c = a + b
num = 0
while c < 1000:
    num = num + 1
    print("El numero",c,"es el",num,"en a serie fibonacci")
    a = b
    b = c
    c = a + b
