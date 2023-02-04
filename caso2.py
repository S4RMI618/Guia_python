
# List for storing identification numbers
identifications = []

# Total number of ballots available
tickets_available = 20

while tickets_available > 0:
  # Request identification number
  id_number = input("Por favor ingrese su número de identificación: ")

  # Check if the ID number is already in the list
  if id_number in identifications:
    print("Lo siento, ya se ha vendido una boleta con este número de identificación.")
  else:
    # Add ID number to the list
    identifications.append(id_number)

    # Request total of ballots for buy
    tickets_bought = int(input("Cuántas boletas desea comprar (máximo 4)? "))

    # Check if the total of ballots is available
    if tickets_bought > 4:
      print("Lo siento, solo se pueden comprar 4 boletas por persona.")
    elif tickets_bought > tickets_available:
      print("Lo siento, no hay suficientes boletas disponibles.")
    else:
      # Update the number of ballots available
      tickets_available -= tickets_bought
      print(f"Venta exitosa! Boletas disponibles: {tickets_available}")

      # Check if all the ballots have been sold
      if tickets_available == 0:
        print("Lo siento, no hay boletas disponibles.")
        break