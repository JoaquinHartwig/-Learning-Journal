def city_country(name,country):
    formatted_location = f"{name.title()},{country.title()}"
    return formatted_location
ubicacion = city_country("Santiago","Chile")
print(ubicacion)

ubicacion = city_country("Caballito","Argentina")
print(ubicacion)

paubicacionis = city_country("San Jose","Argentina")
print(ubicacion)