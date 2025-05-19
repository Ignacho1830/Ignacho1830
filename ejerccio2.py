def calcular_objetivo_ml(peso_kg, nivel_actividad):
    """Calcula el objetivo diario de consumo de agua en mililitros."""
    base_ml = peso_kg * 35  # 35 ml por kg

    if nivel_actividad == "bajo":
        return base_ml * 0.9  # -10%
    elif nivel_actividad == "alto":
        return base_ml * 1.1  # +10%
    else:
        return base_ml  # actividad media, sin ajuste


def estado_hidratacion(consumo_ml, objetivo_ml):
    """Devuelve un mensaje según el porcentaje de cumplimiento del objetivo."""
    porcentaje = (consumo_ml / objetivo_ml) * 100
    diferencia = abs(porcentaje - 100)

    if porcentaje >= 100:
        if porcentaje == 100:
            return "¡Has alcanzado tu objetivo de hidratación!"
        else:
            return f"¡Has excedido tu objetivo en un {diferencia:.1f}%!"
    else:
        return f"Te falta un {diferencia:.1f}% para alcanzar tu objetivo."


# Programa principal
print("=== Control de Consumo de Agua ===")
peso = float(input("Ingrese su peso en kg: "))
actividad = input("Nivel de actividad (bajo, medio o alto): ").lower()
consumo = float(input("Cantidad de agua consumida hoy (en ml): "))

objetivo = calcular_objetivo_ml(peso, actividad)
mensaje = estado_hidratacion(consumo, objetivo)

print("\n=== Resultados ===")
print(f"Objetivo diario recomendado: {objetivo:.1f} ml")
print(f"Estado de hidratación: {mensaje}")
