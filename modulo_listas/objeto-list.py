# construtor list
# o construtor "list" transforma cada caracter de uma string em elementos separados em uma lista
print(list("python"))
# objeto range cria uma contagem no intervalo espeficifaco
print(list(range(10)))
# matrix em python
matrix = [
    ["a", 1, 2.5],
    ["b", 10, 5],
    [8, "f", 20]
]
# aqui temos uma matrix de formação bidimencional
#formação que pode ser identificada com uma tabela de linhas e colunas
# forma de acessar elementos na listas
print(matrix[0]) # retorno -> ['a', 1, 2.5]
print(matrix[0][1]) # retorno -> 1
print(matrix[-1][1]) # retorno -> "f"
# usando numeros negativos para buscar elementos dentro de uma matrix,
# -1 tras o ultimo elemnto de uma matrix, 
#    1       2       3
# primeira segunda terceira
#    -1       -2       -3
# ultima penultima  antepenultima

# listas com for
# fazendo interação na lista
# usar enumerate para numerar a lista
roupas = ["camisa","calsa","luvas"]
for v in roupas:
    print(v)
# compressao de lista
valores = [1, 2, 20, 11, 7, 8, 12]
pares = []
for v in valores:
    if v % 2 == 0:
        pares.append(v)

# list comprehension
pares = [v for v in valores if v % 2 == 0]
print(pares)
