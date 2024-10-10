import math

def expression(A, B, C, D):
    numerator = 1 + C * math.exp(D / (A * B))
    denominator = 4 * math.pi * D
    result = math.sqrt(A * B * numerator / denominator)
    return result

A = 10
B = -0.5
C = 1.1
D = -1

result = expression(A, B, C, D)

print(result)