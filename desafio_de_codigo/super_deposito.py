saldo = 0

valor = float(input("valor: "))

if valor > 0:
    saldo = saldo + valor
    print(f"Deposito realizado com sucesso!\nSaldo atual: R$ {saldo:.2f}")
elif valor < 0:
    print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")