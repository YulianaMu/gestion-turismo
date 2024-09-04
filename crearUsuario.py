# Este espacio se ha diseñado para registrar nuevos usuarios

print("===============================================")
print("          Creación de nuevo usuario            ")
print("===============================================")

# Diccionario para almacenar los usuarios
crearUsuario = {}

# Función para crear un nuevo usuario
def crear_usuario():
    nombre = input("Ingresa tu nombre de usuario: ")
    
    # Verificar si el nombre ya existe en la base de datos
    if nombre in crearUsuario:
        print("Error: Este nombre de usuario ya está registrado.")
        return
    
    contraseña = input("Ingresa tu contraseña: ")
    
    correo = input("Ingresa tu correo electrónico: ")
    
    # Validar que el correo tenga al menos un arroba
    if "@" not in correo:
        print("Error: El correo electrónico debe contener al menos un '@'.")
        return
    
    # Generar un ID único (ejemplo usando el tamaño actual del diccionario)
    usuario_id = len(crearUsuario) + 1
    
    # Almacenar la información del usuario en el diccionario
    crearUsuario[nombre] = {
        "ID": usuario_id,
        "Contraseña": contraseña,
        "Correo": correo
    }
    
    print(f"Usuario {nombre} registrado con éxito.")


# Bucle para permitir la creación de múltiples usuarios
while True:
    crear_usuario()
    
    continuar = input("¿Deseas crear otro usuario? (sí/no): ").strip().lower()
    
    # Si el usuario escribe "no", el bucle termina
    if continuar == "no":
        break

# Mostrar todos los usuarios registrados
print("\nUsuarios registrados:")
for nombre, datos in crearUsuario.items():
    print(f"Nombre: {nombre}, ID: {datos['ID']}, Correo: {datos['Correo']}")
