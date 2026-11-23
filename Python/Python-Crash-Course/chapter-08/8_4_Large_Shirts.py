def make_shirt(size="large", text="I love Python"):
    """Muestra el tamaño y el mensaje de una remera."""
    print(
        f"\nEl tamaño de la remera es {size} "
        f"y el mensaje impreso es '{text}'."
    )


# 1. Remera large con el mensaje por defecto (no pasamos nada)
make_shirt()

# 2. Remera medium con el mensaje por defecto (sobrescribimos solo size)
make_shirt(size="medium")

# 3. Remera de cualquier tamaño con un mensaje distinto (sobrescribimos ambos)
make_shirt(size="small", text="Data Science")