tienda = {
    "P01":{"nombre":"afx",
           "precio":2002,
           "categoria":"muebles"},
    "P02":{"nombre":"Lo_de_Lolo",
           "precio":6767,
           "categoria":"brainrots"}
}

for clave, lista in tienda.items():
    print(f"{clave.title()} \n")
    nombre = f"{lista['nombre']}"
    precio = f"{lista['precio']}"
    categoria = f"{lista['categoria']}"
    print(f"\nNombre:{nombre.title()} \nPrecio:{precio.title()} \nCategoria: {categoria.title()}\n")
    descuento= lista.get("descuento","No se encontro descuento") 
    print(descuento)   


