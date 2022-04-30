import itertools
from math import factorial
p = itertools.permutations('abcdef', 3)
print('количество вариантов при поиске размещеиния (k=3, n=6) =', (factorial(len('abcdef'))/factorial(len('abcdef')-3)))
print(*p, sep='\n')
print()
print()
print('количество вариантов при поиске сочетания (k=3, n=6) =', (factorial(len('abcdef'))/(factorial(len('abcdef')-3) * factorial(3))))
p = itertools.combinations('abcdef', 3)
print(*p, sep='\n')