largura = float(input('Qual é a \033[31mlargura\033[m? '))
comprimento = float(input('Qual é o \033[36mcomprimento\033[m? '))
print(f'A aréa de \033[31m{largura}\033[m x \033[36m{comprimento}\033[m corresponde a \033[32m{largura * comprimento:.2f}m²\033[m')
print(f'Para pintarmos para essa aréa precisaremos de \033[35m{(largura * comprimento) / 2:.2f}\033[m litros de tinta ')
