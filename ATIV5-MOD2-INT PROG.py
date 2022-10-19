def calcular(op1, op2, operacao):
    if operacao == 1:
        return op1 + op2
    if operacao == 2:
        return op1 - op2
    if operacao == 3:
        return op1 * op2
    if operacao == 4:
        return op1 / op2
    
Execute=True
while execute:
    print("Opções válidas:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    oper = int(input("Informe a operação: "))
    if oper >=1 and oper <=4:
        op1 = int(input("Informe o primeiro operando: "))
        op2 = int(input("Informe o segundo operando: "))

        resultado = calcular(op1, op2, oper)
        print(resultado)
    elif oper == 0:
        print("Obrigada, até a próxima.")
        execute = False
else:
    print("Esta opção não existe. Digite outro valor")
