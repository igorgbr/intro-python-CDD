# adição +
# subtração -
# multiplicação *
# Divistão /

# divisão inteira //
# modúlo %
# potenciação **

# import math

# x = 2 + 2
# x = 2 - 2
# x = 3 * 3
# x = 10 / 2

# x = 10 / 3
# x = 10 % 3
# x = 10 ** 2

# y = 5

# print(math.sqrt(y))


# x = str(input('Qual é o seu nome? '))
# print(f'o nome do usuario é {x}')

# --------------------------------------------------------------------------------------------------

# Crie um programa que calcule a velocidade média passando por INPUT() o Delta S e o Delta T

# lembrando que Delta T é o intervalo de tempo e Delta S a distancia
# exemplo: V = 60 Km / 2h | vm = 30km/h
# Lembe-se a divisão deve ser exata!


vf = int(input('Velocidade Final: '))
vi = int(input('Velocidade Inicial: '))
deltaS = vf - vi


tf = int(input('Tempo Final: '))
ti = int(input('Tempo Inicial: '))
deltaT = tf - ti

print(f'Velocidade Média: {deltaS // deltaT} Km/h')
