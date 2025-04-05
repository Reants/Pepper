
import numpy as np

def pertenencia_tristeza(valor):
    if valor <= 0.49:
        return 1  # Pertenece completamente a tristeza
    elif valor <= 0.69:
        return (0.69 - valor) / 0.2  # Transición a fallo
    return 0

def pertenencia_alegria(valor):
    if valor >= 0.7:
        return 1  # Pertenece completamente a alegría
    elif valor >= 0.5:
        return (valor - 0.5) / 0.2  # Transición desde fallo
    return 0

def pertenencia_fallo(valor):
    if 0.5 <= valor <= 0.69:
        return 1
    elif 0.49 < valor < 0.5:
        return (valor - 0.49) / 0.01
    elif 0.69 < valor < 0.7:
        return (0.7 - valor) / 0.01
    return 0

def clasificar_emocion(facial, voz, palabras):
    # Aplicar pesos
    facial_peso = 0.45 * facial
    voz_peso = 0.35 * voz
    palabras_peso = 0.20 * palabras
    
    # Sumar ponderaciones
    emocion_total = facial_peso + voz_peso + palabras_peso
    
    # Obtener grados de pertenencia
    t = pertenencia_tristeza(emocion_total)
    a = pertenencia_alegria(emocion_total)
    f = pertenencia_fallo(emocion_total)
    
    # Decidir la emoción final
    if t > a and t > f:
        return "Tristeza"
    elif a > t and a > f:
        return "Alegría"
    else:
        return "Fallo"

# Ejemplo de prueba
facial = 0.4  # Reconocimiento facial indica tristeza
voz = 0.8     # Reconocimiento de voz indica alegría
palabras = 0.6  # Palabras están en una zona incierta

resultado = clasificar_emocion(facial, voz, palabras)
print("Emoción detectada:", resultado)
