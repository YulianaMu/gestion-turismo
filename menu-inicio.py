
import paquetesd

op=0

   

print("BIENVENIDO AL MENU DE INICIO")
print("********************************************")
print("------------ MENU DE INICIO  ---------------")
print("********************************************")
print("**      1. Gestionar perfil               **")
print("**      2. Gestion de reservas            **")
print("**      3. Crear paquete                  **")
print("**      4. Ver paquetes disponiles        **")
print("**      5. Ver mis reservas               **")
print("**      0. Salir                          **")
print("*******************************************")
op=int(input("elija una opcion"))

if(op > 0 and op < 7):
    match op:
        case  1:
            print("BIENVENIDO A TU PERFIL")
        case  2:
            print("BIENVENIDO A LA GESTION DE TUS RESERVAS")
        case  3:
            print("BIENVENIDO, AHORA PUEDES CREAR TU PAQUETE PREFERIDO")
        case  4:
            print("BIENVENIDO, ESTOS SON LOS PAQUETES DISPONIBLES")
            paquetesd.bienvenida()
        case  5:
            print("BIENVENIDO A TUS RESERVAS")
        case  0:
            print("NO HA ELEJIDO NINGUNA OPCION")

    
    

