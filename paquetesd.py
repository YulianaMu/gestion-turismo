
paquetes = [
    {   'ID': 1,
        'lugar_destino': 'Cartagena',
        'transporte': 'avión',
        'días': 5,
        'cantidad_personas': 2,
        'servicios_extra': ['excursiones', 'alimentacion'],
        'valor': '2.000.000'
    },
    {
        'ID': 2,
        'lugar_destino': 'San Andres',
        'transporte': 'avion',
        'días': 5,
        'cantidad_personas': 5,
        'servicios_extra': ['excursiones', 'alimentacion'],
        'valor': '5.999.900'

    }   
]



def mostrar_paquetes(paquetes):
    for paquete in paquetes:
        print("")
        print(f"#: {paquete[ID]}")
        print(f"PAQUETE PARA: {paquete['lugar_destino']}")
        print("-" * 30)
        print(f"Lugar de destino: {paquete['lugar_destino']}")
        print(f"Transporte: {paquete['transporte']}")
        print(f"Días: {paquete['días']}")
        print(f"Cantidad de personas: {paquete['cantidad_personas']}")
        print(f"Servicios extra: {', '.join(paquete['servicios_extra'])}")
        print(f"Precio: {paquete['valor']}")

        print("*" * 30)


def bienvenida():
    print("***********************************")
    print("            BIENVENIDO             ")
    print("-----------------------------------")
    print(" ESTOS SON LOS PAQUETES DISPONIBLES")
    print("***********************************")
    mostrar_paquetes(paquetes)



bienvenida()
