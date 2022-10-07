N=int(input("ingresa el numero:"))

n1=N
if N>0:
    suma=0
    while N>0:
        suma = suma + N%10
        N = N//10
    print("la suma de",n1,"es",suma)

else:
    print("Ingresa un dato positivo")