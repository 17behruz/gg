import math

def calculate_task2(x):
    a = 0.25
    return math.exp((a / x) + 4) + math.sqrt(math.log(math.sin(x)) / math.cos(a * x)) + (math.sin(2*x) + 5*x)**3
