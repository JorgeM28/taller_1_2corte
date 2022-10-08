print("----------------------")
print("------CHEUQE----------")
print("----------------------")

CB10K = 0
CB2K = 0
CM100 = 0
num = 0
X=int(input("Ingresa el valor del cheque: "))

while X != 0:
    B10K = X // 10000
    R = X - (B10K*10000)
    B2K = R // 2000
    R = R - (B2K*2000)
    M100 = R // 100
    CB10K = CB10K + B10K
    CB2K = CB2K + B2K
    CM100 = CM100 + M100
    num = num + 1
    print("Para el cheque de valor",X,"se dieron")
    print(B10K,"billetes de 10,000$")
    print(B2K,"billetes de 2,000$")
    print(M100,"monedas de 100$")
    X=int(input("Ingresa el valor del cheque: "))



print("En el dia se ingresaron",num,"cheques")
print("Se gastaron",CB10K,"billetes de 10,000$")
print("Se gastaron",CB2K,"billetes de 2,000$")
print("Se gastaron",CM100,"monedas de 100$")