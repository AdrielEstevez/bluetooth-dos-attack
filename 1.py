reservas = []

while True:
    print("\n1. Agregar reserva")
    print("2. Cancelar reserva")
    print("3. Mostrar reservas activas")
    print("4. Mostrar reservas por cliente")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        nombre_cliente = input("Nombre del cliente: ")
        cantidad_personas = int(input("Cantidad de personas: "))
        hora_reserva = input("Hora de la reserva: ")
        reserva = {
            'nombre_cliente': nombre_cliente,
            'cantidad_personas': cantidad_personas,
            'hora_reserva': hora_reserva
        }
        reservas.append(reserva)
        print(f"Reserva agregada: {reserva}")

    elif opcion == '2':
        nombre_cliente = input("Nombre del cliente: ")
        hora_reserva = input("Hora de la reserva: ")
        reserva_cancelada = False
        for reserva in reservas:
            if reserva['nombre_cliente'] == nombre_cliente and reserva['hora_reserva'] == hora_reserva:
                reservas.remove(reserva)
                print(f"Reserva cancelada: {reserva}")
                reserva_cancelada = True
                break
        if not reserva_cancelada:
            print("Reserva no encontrada.")

    elif opcion == '3':
        if not reservas:
            print("No hay reservas activas.")
        else:
            print("Reservas activas:")
            for reserva in reservas:
                print(reserva)

    elif opcion == '4':
        nombre_cliente = input("Nombre del cliente: ")
        reservas_cliente = []
        for reserva in reservas:
            if reserva['nombre_cliente'] == nombre_cliente:
                reservas_cliente.append(reserva)
        if not reservas_cliente:
            print(f"No hay reservas para el cliente: {nombre_cliente}")
        else:
            print(f"Reservas para {nombre_cliente}:")
            for reserva in reservas_cliente:
                print(reserva)

    elif opcion == '5':
        break
    else:
        print("Opción no válida.")