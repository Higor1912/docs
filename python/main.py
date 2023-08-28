#x = 10           # tipo: inteiro
#y = 3.14         # tipo: float
#nome = "Maria"   # tipo: string
#lista = [1, 2, 3] # tipo: lista
#/////////////////////////////////
nome = input("digite seu nome:")
funcao = input("digite sua funcao")
idade = input("digite sua idade:")

idade = int(idade)

print ("qual é o seu nome:", nome)
print("qual é a sua funcao:", funcao)
print("digite sua idade:", idade)

x = input("digite um numero: ")
y = input("digite um numero: ")

x = float(x)
y = float(y)

operacao = input("Digite 's' para soma ou 'd' para divisão: ")

if operacao == 's':
    resultado = x + y
    print("A soma dos números é:", resultado)
elif operacao == 'd':
    resultado = x / y
    print("A divisão dos números é:", resultado)
else:
    print("Operação inválida. Por favor, digite 's' para soma ou 'd' para divisão.")
