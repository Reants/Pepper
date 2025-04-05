def emotion_clasificator(facial, voz, palabras):
    # Pesos de cada algoritmo
    pesos = {0: 0, 1: 0, 2: 0}  # Diccionario para acumular votos

    # Asignar votos ponderados
    pesos[facial] += 0.45
    pesos[voz] += 0.35
    pesos[palabras] += 0.20

    # Seleccionar la emoción con el mayor peso
    emocion_detectada = max(pesos, key=pesos.get)

    return emocion_detectada

while True:
    Fer=int(input("Por favor ingrese el primer dato:"))
    Ver=int(input("\nPor favor ingrese el segundo dato dato:"))
    Wr=int(input("\nPor favor ingrese el tercer dato:"))
    emocion = emotion_clasificator(Fer, Ver, Wr)
    print("\nSu resultado es:",emocion)
    x=input("\nDesea continuar? S o N")
    if x == "S": continue
    else: break
