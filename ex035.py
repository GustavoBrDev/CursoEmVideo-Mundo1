from time import sleep

print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
reta1 = float(input('Qual o comprimento do primeiro segmento: '))
reta2 = float(input('Qual o comprimento do segundo segmento: '))
reta3 = float(input('Qual o comprimento do terceiro segmento: '))
print('\nAnalisando')
sleep(2)
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2: #Uma reta não pode ser maior do que a soma dos demais
    print('As retas informadas acima \033[1;32mPODEM formar\033[m um \033[35mtriangulo\033[m')
else:
    print('As retas informadas acima \033[1;31mNÃO PODEM\033[m formar um \033[35mtriangulo\033[m')
