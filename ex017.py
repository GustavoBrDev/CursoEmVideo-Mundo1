from math import hypot
x = float(input('Comprimento do cateto oposto: '))
y = float(input('Comprimento do cateto adjacente: '))
print(f'A hipotenusa vai medir \033[1;42m{hypot(x,y):.2f}\033[m')
print(f'Modo matematico: \033[1;43m{(x**2+y**2)**(1/2):.2f}\033[m') #a² = b² + c²