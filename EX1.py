def calcula_area(B,b,h):
    return ((B + b) * h)/2

h = int(input("Entre com o valor da altura: "))
B = int(input("Entre com o valor da base maior: "))
b = int(input("Entre com o valor da base menor: "))

area = calcula_area(B,b,h)
print(area)
