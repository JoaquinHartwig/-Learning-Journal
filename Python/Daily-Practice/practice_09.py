autos = {
    "auto1":{"marca":"vw",
             "modelo":"gol",
             "año":2003,
             "disponibilidad":False},

     "auto2":{"marca":"fiat",
              "modelo":"uno",
              "año":1993,
              "disponibilidad":False},

     "auto3":{"marca":"vw",
              "modelo":"CrossFox",
              "año":2021,
              "disponibilidad":False}         
}

#Recorré la lista con un bucle for.

#Si el auto es del año 2020 o posterior, cambiá 'disponible' a True.

#Imprimí únicamente los autos que estén disponibles mostrando la marca, el modelo y el año.

for auto, detalles in autos.items():
    if detalles["año"] >= 2020:
     detalles["disponibilidad"] = True
     print(f"{auto}")
    if detalles["disponibilidad"]:
        marca = detalles["marca"].upper()
        modelo = detalles["modelo"].title()
        año = detalles["año"]

        print(
            f"Auto disponible ({auto}): {marca} {modelo} - Año: {año}"
        )
 