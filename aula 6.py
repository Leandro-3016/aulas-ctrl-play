



lista = [1,2,3,4,4,2,5,6,5,4,6,7,4,3,2,3,8,9,8,6,5,10]
em = set(lista)
print(lista)
outra = []
outra.insert(0, em)
print(f'atualizado{outra}')


ddds = {
    11: "São Paulo",
    21: "Rio de Janeiro",
    31: "Belo Horizonte",
    41: "Curitiba",
    51: "Porto Alegre",
    61: "Brasília",
    71: "Salvador",
    81: "Recife",
    91: "Belém",
    12: "São José dos Campos",
    13: "Santos",
    14: "Bauru",
    15: "Sorocaba",
    16: "Ribeirão Preto",
    17: "São José do Rio Preto",
    19: "Campinas",
    27: "Vitória",
    47: "Joinville",
    48: "Florianópolis",
    85: "Fortaleza"
}

ddd = ''
while ddd not in ddds:
    ddd = int(input("Digite um dd para descobrir qual o estado pertencente:"))
    if ddd not in ddds:
      print("Não está na lista")
else:
    print(ddds[ddd])























