#Este espacio se ha diseñado para registrar nuevos crearUsuario

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

# Llamar a la función para crear un usuario
crear_usuario()
