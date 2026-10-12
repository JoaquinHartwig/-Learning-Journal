import math

m = 8

# a) Grupos de a 5
grupos_de_5 = math.comb(m, 5)

# b) Grupos de a 3
grupos_de_3 = math.comb(m, 3)

# c) Grupos de a 4
grupos_de_4 = math.comb(m, 4)

print(f"a) Combinaciones para grupos de 5: {grupos_de_5}")
print(f"b) Combinaciones para grupos de 3: {grupos_de_3}")
print(f"c) Combinaciones para grupos de 4: {grupos_de_4}")