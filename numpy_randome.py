from numpy import random

x = random.randint(100)

print(x)
print("----------------------------")
y=random.randint(100, size=(10))
print(y)
print("----------------------------")
z = random.randint(100, size=(3, 5))

print(z)
print("----------------------------")
a = random.rand(5)
print(a)
print("----------------------------")
b = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(b)