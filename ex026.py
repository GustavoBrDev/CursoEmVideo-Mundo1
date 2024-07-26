frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.count('A') + 1  # Conta a quantidade (+1 --> Inicia em 0)
b = frase.find('A')  # Procura pela esquerda (padrao)
c = frase.rfind('A') + 1  # Procura pela direita (pelo fim)
print('-' * 15)
print('Analisando...')
if a == 0:
    print('Não há nenhuma letra \033[1;43mA\033[m na frase')
else:
    print(f'A letra \033[1;43mA\033[m aparece \033[1;32m{a}\033[m vezes na frase')
if b == -1:
    print('A letra \033[1;43mA\033[m \033[1;31mnão aparece\033[m na frase')
else:
    print(f'A priveira aparição da letra \033[1;43mA\033[m é na posição \033[4;34m{b}\033[m e a ultima vez é na posição \033[4;35m{c}\033[m')

print('Analise completa!')
print('-' * 15)
