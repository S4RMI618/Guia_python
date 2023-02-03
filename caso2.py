# Lista para almacenar los números de identificación
identifications = []

# Cantidad total de boletas disponibles
tickets_available = 20

while tickets_available > 0:
  # Solicitar número de identificación
  id_number = input("Por favor ingrese su número de identificación: ")

  # Verificar si el número de identificación ya existe en la lista
  if id_number in identifications:
    print("Lo siento, ya se ha vendido una boleta con este número de identificación.")
  else:
    # Agregar número de identificación a la lista
    identifications.append(id_number)

    # Solicitar la cantidad de boletas a comprar
    tickets_bought = int(input("Cuántas boletas desea comprar (máximo 4)? "))

    # Verificar que la cantidad de boletas sea válida
    if tickets_bought > 4:
      print("Lo siento, solo se pueden comprar 4 boletas por persona.")
    elif tickets_bought > tickets_available:
      print("Lo siento, no hay suficientes boletas disponibles.")
    else:
      # Actualizar la cantidad de boletas disponibles
      tickets_available -= tickets_bought
      print(f"Venta exitosa! Boletas disponibles: {tickets_available}")

      # Verificar si se han vendido todas las boletas
      if tickets_available == 0:
        print("Lo siento, no hay boletas disponibles.")
        break