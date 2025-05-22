import mathematic
from package.messages import welcome
from package.operations import multiply

print(welcome("Denis"))

print("Soma:", mathematic.sum(5, 2))
print("Subtração:", mathematic.sub(10, 4))
print("Fatorial:", mathematic.factor(5))
print("Multiplicação:", multiply(3, 7))
