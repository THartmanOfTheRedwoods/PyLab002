import math
name = "Tucker"
age = 25
height = 5.6
favorite_color = "Purple"

print(name)
print(age)
print(height)
print(favorite_color)

print(name, age, height, favorite_color)
print(f"{name}, {age}, {height}, {favorite_color}")

print(f"""
Name: {name}
Age: {age}
Height: {height}
Favorite Color: {favorite_color}
""")

radius = 5
circle_area = math.pi * (radius ** 2)
words = "The area is {:.1f}"
print(words.format(circle_area))

print(math.sqrt(age))
print(math.cos(height))
print(math.sin(height))

calc1 = age + 5
calc2 = height - 4
calc3 = age * height
calc4 = height / 2
calc5 = age // 3
calc6 = age % 2

print(f"""
{calc1}
{calc2}
{calc3}
{calc4}
{calc5}
{calc6}
""")

tempf = input("What is the temperature in fahrenheit where you are?")
tempf = float(tempf)
tempc = (tempf - 32) * 5/9
words2 = "It is {:.1f}° in Celsius"
print(words2.format(tempc))