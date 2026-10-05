
#Codigo Versionado

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

# Imprime la lista completa como un bloque: ['pizza', 'falafel', ...]
print("My favorite foods are:")
for value in my_foods:
    print(f"{value.title()}")

print("\nMy friend's favorite foods are:")
for value2 in friend_foods:
   print(f"{value2.title()}")