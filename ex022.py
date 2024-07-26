#Esse é bom

frase = str(input('Digite seu nome completo: ')).strip()

print('\nAnalisando seu nome...')
letras = len(frase)-frase.count(' ')
print(f'Seu nome em MAISÚSCULO: \033[31m{frase.upper()}!!!\033[m')
print(f'Seu nome em miniscúlo: \033[36m{frase.lower()}\033[m')
print(f'Seu nome possui \033[32m{letras}\033[m letras(s)')
print(f'Seu primeiro nome é \033[33m{frase.split()[0]}\033[m e ele possui \033[35m{len(frase.split()[0])}\033[m letras(s) ')