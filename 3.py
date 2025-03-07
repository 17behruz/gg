import math
A = 3
B = 4
r = math.sqrt(A**2 + B**2)
theta = math.atan2(B, A)
print(f"Комплексное число в тригонометрической форме: {r} * (cos({theta}) + i*sin({theta}))")
