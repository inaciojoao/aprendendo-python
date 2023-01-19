import os

palavra_secreta = 'vodka'  #aqui vc escolhe a palavra secreta
letras_acertadas = ""
numero_tentativa = 0
while True:
    entrada_usuario = input('Digite uma letra: ')
    numero_tentativa +=1

    if len(entrada_usuario) > 1:    #esse blobo serve para checar se o usuario digitou apenas uma letra
        print('Digite apenas uma letra. ')
        continue

    print('Bora lá continuar essa bagaça.')

    if entrada_usuario in palavra_secreta:
        letras_acertadas += entrada_usuario

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('PARABÉNS VC ACERTOU A PALAVRA SECRETA!!')
        print('Número total de tentativas: ', numero_tentativa)


