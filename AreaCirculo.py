# AreaCirculo.py - Algoritmo para calcular el área de un círculo
import math


def calcular_area_circulo(radio):
    return math.pi * (radio**2)


if __name__ == "__main__":
    print("--- Cálculo del Área de un Círculo ---")
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("El radio no puede ser negativo.")
        else:
            resultado = calcular_area_circulo(radio)
            print(f"El área del círculo es: {resultado:.2f}")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")