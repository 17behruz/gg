import math
x = 1
y = 2

numerator = y**2 + 12 * x * y - 3 * x**2
denominator = 18 * y - 1
result = math.exp(x) - (numerator / denominator)
print("Результат:", result)
