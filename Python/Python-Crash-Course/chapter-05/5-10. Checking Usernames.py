current_users = ["AFX","Joa","Xqc","Charles","Koplo"]
new_users = ["AFX","Jinx","Rrt","Charles","lolo"]
for value in new_users:
    if value in current_users:
       print(f"El nombre de usuario '{value}' ya está en uso. Por favor, ingresá uno diferente.")
    else:
        print(f"El nombre de usuario '{value}' está disponible.")