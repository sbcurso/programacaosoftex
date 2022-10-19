def calcular (valor1, valor2, op ):
 
    if op ==  "+" :
        resultado = valor1 + valor2
    elif op == "-" :
        resultado = valor1 - valor2
    elif op == "*" :
        resultado = valor1 * valor2
    elif op == "/" :
        resultado = valor1 / valor2

print ( "Esta é a melhor calculadora do mundo." )

opcao = "S"
while opcao == "S" :
    operando1 = input ( "Informe o primeiro operando: " )
    operando2 = input ( "Informe o segundo operando: " )
    operador = input ( "Informe o operador: " )

    a = int (operando1)
    b = int (operando2)

    resposta = calcular ( a, b, operador )
    print ( resposta )

    opcao = input ("Você deseja executar novamente (S ou N)?" )

