#------reservaciones-------
reservaciones = {"1reservacion"{"lugar":"san andres","cantidad": 5 ,"transporte": "avion","tiempo": "7 dias"},
                 "2reservacion"{"lugar":"cartagena","cantidad": 4 , "transporte": "autobus","tiempo": "5 dias"}
                 }


print(reservaciones)
print("QUE ACCION DESEA REALIZAR?")
print("MODIFICAR RESERVACION (1)")
print("CONFIRMAR RESERVACION (2)")
print("ELIMINAR RESERVACION (3)")
respuesta = input ("ESCRIBA UNA OPCION: ")
while True:
    if respuesta == "1":
        print("MODIFICAR RESERVACION")
        print(reservaciones)
        opcion = print("SELECIONE LA RESERVACION A MODIFIRCAR: ")

    elif respuesta == "2":
        print("CPNFIRMAR RESERVACION") 
    elif respuesta == "3":
        print("ELIMINAR RESERVACION") 
    else:
        print("INGRESE UNA OPCION VALIDAD")        