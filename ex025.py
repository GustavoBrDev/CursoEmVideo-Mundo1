nome = str(input('Digite seu nome completo: ')).strip().upper()
silva = 'SILVA' in nome
if silva == True:
    print('Seu nome \033[32mtem\033[m \033[36mSilva\033[m')
elif silva == False:
    print('Seu nome \033[31mnão\033[m tem \033[36mSilva\033[m')
