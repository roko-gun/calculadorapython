def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division entre 0 no permitida"
    
def potencia(a, b):
    return a ** b
    
print("=== Calculadora Basica===")
print("Operaciones disponibles: +, -, *, /")

# pedimos los datos al usuario 
num1 = float(input('ingrese el primer numero:'))
operador = input("ingrese la operacion (+, -, *, /): ")
num2 = float(input('Ingrese el segundo numero:'))

if operador == "+":
    resultado = sumar(num1, num2)
elif operador == "-":
    resultado = restar(num1, num2)
elif operador == "*":
    resultado = multiplicar(num1, num2)
elif operador == "/":
    resultado = dividir(num1, num2)
elif operador == "**":
    resultado = potencia(num1, num2)
else:
    resultado = "Operacion No valida"

print ("Resultado:", resultado)

