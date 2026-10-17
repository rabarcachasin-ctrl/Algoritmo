# SumaDosNumeros.py - Algoritmo para sumar dos números
def sumar(a, b):
    return a + b


if __name__ == "__main__":
    print("--- Suma de Dos Números ---")
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es: {resultado}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")