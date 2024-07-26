velocidade = float(input('Qual a velocidade atual do seu carro? '))
if velocidade < 80:
    print('Tenha um bom dia. Dirija com segurança!')
elif velocidade == 80:
    print('Você \033[1mquase passou do limite\033[m, \033[1;33mmais cuidado\033[m na hora de dirigir!')
else:
    print('\033[7;31mVocê ultrapassou o limite de 80km/h!\033[m')
    print(f'A sua \033[1mmulta\033[m será de \033[31mR${(velocidade - 80) * 7:.2f}\033[m')
