# Gestionar perfil
usuarios = {
    "usuario1": {
        "nombre": "Marlon Molina",
        "residencia": "Cali",
        "correo": "Marlonmm25@gmail.com"
    },
    "usuario2": {
        "nombre": "Pepito Perez",
        "residencia": "Palmira",
        "correo": "Pepito@gmail.com"
    }
}

# Almacenar los paquetes de viajes disponibles
paquetes = {
    "paquete1": {"destino": "París", "precio": 7000},
    "paquete2": {"destino": "Londres", "precio": 8000},
    "paquete3": {"destino": "Nueva York", "precio": 6000}
}

def mostrar_menu():
    print("\nMenu de Gestión de Viajes")
    print("1. Modificar Lugar de Residencia")
    print("2. Mostrar Paquetes Disponibles")
    print("3. Modificar Correo Electrónico")
    print("4. Salir")

def modificar_residencia():
    usuario_id = input("Ingrese su ID de usuario (ej. usuario1): ")
    if usuario_id in usuarios:
        nueva_residencia = input("Ingrese su nuevo lugar de residencia: ")
        usuarios[usuario_id]["residencia"] = nueva_residencia
        print("Lugar de residencia modificado con éxito.")
    else:
        print("ID de usuario no encontrado.")

def mostrar_paquetes():
    print("\nPaquetes Disponibles:")
    for paquete_id, info in paquetes.items():
        print(f"ID del Paquete: {paquete_id}, Destino: {info['destino']}, Precio: ${info['precio']}")

def modificar_correo():
    usuario_id = input("Ingrese su ID de usuario (ej. usuario1): ")
    if usuario_id in usuarios:
        nuevo_correo = input("Ingrese su nuevo correo electrónico: ")
        usuarios[usuario_id]["correo"] = nuevo_correo
        print("Correo electrónico modificado con éxito.")
    else:
        print("ID de usuario no encontrado.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            modificar_residencia()
        elif opcion == '2':
            mostrar_paquetes()
        elif opcion == '3':
            modificar_correo()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
