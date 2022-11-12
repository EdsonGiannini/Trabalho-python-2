def soma_imposto(taxa_imposto, custo):
    return  custo + (custo * (taxa_imposto/100))
taxa_imposto = int(input("Informe a porcentagem da taxa de imposto: "))
custo = int(input("Informe o valor do produto: "))
print(soma_imposto(taxa_imposto, custo))
