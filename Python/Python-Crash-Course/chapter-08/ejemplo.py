
# CON PRINT (El dato se pierde en la consola):
def sumar_print(a, b):
    print(a + b)


resultado = sumar_print(5, 3)  # Imprime 8 en pantalla
print(resultado)               # Imprime None (vacío), porque la función no devolvió nada