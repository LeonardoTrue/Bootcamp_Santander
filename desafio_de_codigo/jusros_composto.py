valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

#TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
def calculando_juros(valor_inicial,taxa_juros,periodo):
    # calculando juros
    montante = valor_inicial * ((1+taxa_juros) ** periodo) # calculando primeiro raiz quadrada de taxa com periodo
    juros = montante - valor_inicial # tirando valor do juros

    print(f"Valor final do investimento: R$ {montante:.2f}")
    print(f"{juros:.2f}")

calculando_juros(valor_inicial,taxa_juros,periodo)