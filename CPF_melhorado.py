cpf_usuario = '' # coloco entre aspas para virar uma string e poder fatiar/ coloque um cpf gerado aleatoriamente por um gerador online
nove_digitos = cpf_usuario[:9]
contador_regressivo = 10

resultado_primeiro_digito = 0 #variavel para salvar as multiplicações
for digito in nove_digitos:
    resultado_primeiro_digito += int(digito) * contador_regressivo  #aqui multiplica cada numero do cpf por 10 e ja soma os resultados
    contador_regressivo -= 1
primeiro_digito = (resultado_primeiro_digito * 10) % 11 
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0


# claculando o segundo digito do cpf

cpf = cpf_usuario
dez_digitos = cpf[:10]
contador_regressivo = 11

resultado_segundo_digito = 0

for digito in dez_digitos:
    resultado_segundo_digito += int(digito) * contador_regressivo
    contador_regressivo -= 1
segundo_digito = (resultado_segundo_digito * 10 ) % 11
segundo_digito = segundo_digito if segundo_digito <= 9 else 0



# validando o cpf

cpf_calculado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_usuario == cpf_calculado:
    print(f'O CPF {cpf_calculado} é válido.')
else:
    print('CPF inválido.')
