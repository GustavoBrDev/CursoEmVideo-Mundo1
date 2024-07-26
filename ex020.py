from random import shuffle
a1 = input('Qual o nome do \033[31mprimeiro\033[m aluno? ')
a2 = input('Qual o nome do \033[32msegundo\033[m aluno? ')
a3 = input('Qual o nome do \033[33mterceiro\033[m aluno? ')
a4 = input('Qual o nome do \033[34mquarto\033[m aluno? ')
alunos = [a1,a2,a3,a4]
shuffle(alunos) #Embaralha a ordem
print(f'''A ordem de apresentação será: 
{alunos}''')