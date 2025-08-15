nome = input('como você se chama calculador?: ')
print('=' * 50)
print(f"Bem-vindo(a) {nome}! Aqui é a Calculadora Calculável, sim, ISSO MESMO: C-A-L-C-U-L-A-V-E-L.\n")
print("Aqui existem duas regras:")
print("- Seus cálculos não podem ultrapassar 99999;")
print("- Você só pode usar as operações (+, -, *, /).\n")
print("Bom cálculo!\n")
print('=' * 50)
while True:
 num1 = int(input('Digite o valor desejado no calculo: '))
 operador = input('Escolha o operador: (+, -, *, /)')
 num2 = int(input('Digite o valor desejado no calculo: '))
 if operador == '+':
  resultado = num1 + num2
 elif operador == '-':
  resultado = num1 - num2
 elif operador == '*':
  resultado = num1 * num2
 elif operador == '/':
  resultado = num1 / num2
 else:
    print('operador invalido')
    continue
 if resultado < 10000:
    print(f'Resultado: {resultado: .0f}')
 else:
    print('Parece que alguém não leu as regras.')

continuar = input('Deseja fazer outro calculo? (S/N): ')
if continuar.lower != 's':
 print('Até a proxima')
 break
     
