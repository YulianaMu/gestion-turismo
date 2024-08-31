paquetes = []
while True:
   print("BIENVENIDO A LA AGENCIA DE VIAJES")
   print("REGISTRARSE (1)")
   print("INICIAR SECION (2)")
   opcion = str(input("INGRESE UNA OPCION: "))

   if opcion == "1":

      print(f"{paquetes}")      
   elif opcion == "2":
        
        print(f"SU LISTA DE CONTACTOS ES: {paquetes}")
       
   else:
    print("INGRESE UNA OPCION CORRECTA")

