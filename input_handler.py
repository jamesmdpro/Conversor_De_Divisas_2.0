def get_user_input():
    tipo_de_cambio = """
    ¿Qué tipo de cambio desea realizar?
    1. Pesos colombianos a dólares
    2. Dólares a pesos colombianos
    3. Pesos mexicanos a dólares
    4. Dólares a pesos mexicanos
    5. Soles peruanos a dólares
    6. Dólares a soles peruanos

    Seleccione una opción: """
    conversion = int(input(tipo_de_cambio))
    if conversion not in [1, 2, 3, 4, 5, 6]:
        print("Opción inválida. Por favor, seleccione una opción válida e intente nuevamente.")
        return None

    if conversion in [1, 3, 5]:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        return {"moneda_origen": "pesos", "cantidad": cantidad, "conversion": conversion}
    else:
        cantidad = float(input("Ingrese la cantidad a convertir: "))
        return {"moneda_origen": "dolares", "cantidad": cantidad, "conversion": conversion}
