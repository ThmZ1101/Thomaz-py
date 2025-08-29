import math

def calculadora():
    """
    Calcula o seno, cosseno e tangente de um ângulo em graus.
    """
    try:
        angulo = float(input("Digite o valor do ângulo em graus: "))

        anguloR = math.radians(angulo)

        seno = math.sin(anguloR)
        cosseno = math.cos(anguloR)
        tangente = math.tan(anguloR)

        print(f"\nResultados para o ângulo de {angulo} graus:")
        print(f"Seno: {seno:.4f}")
        print(f"Cosseno: {cosseno:.4f}")
        print(f"Tangente: {tangente:.4f}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

calculadora()