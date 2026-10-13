usuarios = {"berta":"C",
            "lolo":["Python","R"],
            "valen":["C++","JavaScript","C#"],
            "valeria":"C++"}

for nombre, lenguaje in usuarios.items():
    print(f"\n{nombre.title()}:")
    if isinstance(lenguaje,list):
        for lengua in lenguaje:
            print(f"\t-{lengua}")
    else:
        print(f"\t-{lenguaje}")