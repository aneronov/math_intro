from math import factorial


def probability(k, n, p):
    return ((factorial(n) / (factorial(k) * factorial(n - k))) * (p)**k * (1 - p)**(n - k))


print('вероятность выпадания орла 3 раза при 8 подбрасываний монеты:', probability(3, 8, 1/2))
print('вероятность выпадания орла 8 раза при 10 подбрасываний монеты:', probability(8, 10, 1/2))
print('вероятность выпадания "ЗЕРО" 2 раза при 10 попытках игры в рулетку:', probability(2, 10, 1/37))