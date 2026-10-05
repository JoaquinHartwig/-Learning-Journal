pizza = ["muzzarela","peperoni", "americana"]
for pizza1 in pizza:
    print(f"I like {pizza1.title()} pizza")
print("I really love pizza")
print("Eat pizza while watch TV")
print("I belong a the Mason logia")
friend_pizzas= pizza[:]
pizza.append("queso")
friend_pizzas.append("salchicha")
print("My favorite pizza are:")
for value in pizza:
    print(f"{value.title()}")
for value2 in friend_pizzas:
    print(f"{value2.title()}")