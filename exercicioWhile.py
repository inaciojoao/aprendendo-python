# CALCULADORA COM WHILE

while True:    # começando com true para fazer as opeções, quando for false o usuario encerra o programa
   
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+ - * /) ')
    
    numero_valido = None  # variavel para poder checar se o usuario digitou numeros válidos

    try:
        numero1_float = float(numero1) #convertendo os numeros para float
        numero2_float = float(numero2) #convertendo os numeros para float
        numero_valido = True  #se caso o numero realmente for válido o programa vai continuar

    except:
        numero_valido = None

    if numero_valido is None:
        print('Um ou ambos números digitados são inválidos, por favor digite novamente.')
        continue #se caso a condição cair aqui o programa irá retornar para a parte de digitar os números

    operadores_permitidos = '+-*/' # somente esses operadores matematicos sao permitidos

    if operador not in operadores_permitidos: # aqui esta sendo checado se o operador digitado pelo usuário é válido
        print('Operador inválido.')
        continue
  
    if len(operador) > 1:   #aqui esta sendo checado se o usuário digitou apenas um operador
        print('Digite somente um operador.')
        continue

    soma = numero1_float + numero2_float
    subtracao = numero1_float - numero2_float
    multiplicacao = numero1_float * numero2_float
    divisao = numero1_float / numero2_float
  
    if operador == '+' :
        print(soma)
    elif operador == '-' :
        print(subtracao)
    elif operador == '*' :
        print(multiplicacao)
    elif operador == '/' :
        print(divisao)
    else:
        print('Não deveria chegar até aqui KKKKKK')
  
    sair = input('Deseja sair? [S]sim [N]não ').lower().startswith('s')  #.lower joga o que o user digitar para   #.startswith pega a primeira letra digitada, no caso é o 's'
    if sair is True:
        print('Programa encerrado.')
        break
    elif sair is False:
        continue                   
