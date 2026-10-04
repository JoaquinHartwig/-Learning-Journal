squares = []
for value in range(1, 6):
    squares.append(value ** 2)

print(squares)  # [1, 4, 9, 16, 25]

squares = [value ** 2 for value in range(1, 6)]

print(squares)  # [1, 4, 9, 16, 25]