# Potencia.py - Algoritmo para calcular la potencia de un número
def calcular_potencia(base, exponente):
    return base**exponente


if __name__ == "__main__":
    print("--- Cálculo de Potencia ---")
    try:
        base = float(input("Ingrese la base: "))
        exponente = float(input("Ingrese el exponente: "))
        resultado = calcular_potencia(base, exponente)
        print(f"El resultado de {base} elevado a {exponente} es: {resultado}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")