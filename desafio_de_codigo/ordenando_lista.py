ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ordenada = [valor for valor in ativos]
lista_ordenada = ordenada.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ordenada:
    print(ativo)





