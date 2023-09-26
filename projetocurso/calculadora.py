

#Calculadora científica

#importar as funções matemáticas
import math

#função para somar
def somar(x, y):
   return x + y

#função para subtrair
def subtrair(x, y):
   return x - y

#função para multiplicar
def multiplicar(x, y):
   return x * y

#função para dividir
def dividir(x, y):
   return x / y

#função para calcular o resto da divisão
def resto(x, y):
   return x % y

#função para calcular o logaritmo
def logaritmo(x):
   return math.log(x)

#função para calcular a potência
def potencia(x, y):
   return math.pow(x, y)

#função para calcular o n-ésimo número de Fibonacci
def fibonacci(x):
   if x<=0:
       print("Por favor, insira um número inteiro positivo")
   elif x==1:
       return 0
   elif x==2:
       return 1
   else:
       return fibonacci(x-1)+fibonacci(x-2)

#função para calcular a raiz quadrada
def raiz_quadrada(x):
   return math.sqrt(x)

#menu
print("Selecione a operação a ser realizada:")
print("1.Somar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")
print("5.Resto da divisão")
print("6.Logaritmo")
print("7.Potência")
print("8.Fibonacci")
print("9.Raiz quadrada")

#pegar a opção do usuário
escolha = input("Digite a opção (1/2/3/4/5/6/7/8/9):")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if escolha == '1':
   print(num1,"+",num2,"=", somar(num1,num2))

elif escolha == '2':
   print(num1,"-",num2,"=", subtrair(num1,num2))

elif escolha == '3':
   print(num1,"*",num2,"=", multiplicar(num1,num2))

elif escolha == '4':
   print(num1,"/",num2,"=", dividir(num1,num2))

elif escolha == '5':
   print(num1,"%",num2,"=", resto(num1,num2))

elif escolha == '6':
   print("log(",num1,")=", logaritmo(num1))

elif escolha == '7':
   print(num1,"**",num2,"=", potencia(num1,num2))

elif escolha == '8':
   print("O",num1,"-ésimo número de Fibonacci é:", fibonacci(num1))

elif escolha == '9':
   print("A raiz quadrada de",num1,"=", raiz_quadrada(num1))

else:
   print("Opção inválida")  #mensagem de erro 

#fim da calculadora