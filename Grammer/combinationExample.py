items = [1, 2, 3, 4, 5]
# 입력값이 주어졌을 때 => 보통 리스트의 형태

from itertools import permutations
        
permuItems = list(permutations(items, 2))
print(permuItems)
# [(1, 2), (1, 3), (1, 4), (1, 5), 
#  (2, 1), (2, 3), (2, 4), (2, 5), 
#  (3, 1), (3, 2), (3, 4), (3, 5), 
#  (4, 1), (4, 2), (4, 3), (4, 5), 
#  (5, 1), (5, 2), (5, 3), (5, 4)]

from itertools import combinations

combiItemsBy2 = list(combinations(items, 2))
print(combiItemsBy2)
# [(1, 2), (1, 3), (1, 4), (1, 5), 
#  (2, 3), (2, 4), (2, 5), 
#  (3, 4), (3, 5), 
#  (4, 5)]

combiItemsBy3 = list(combinations(items, 3))
print(combiItemsBy3)
# [(1, 2, 3), (1, 2, 4), (1, 2, 5), 
#  (1, 3, 4), (1, 3, 5), (1, 4, 5), 
#  (2, 3, 4), (2, 3, 5), (2, 4, 5), 
#  (3, 4, 5)]

# 여러개의 리스트에서 조합을 뽑아내야 하는 경우
from itertools import product

items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]
productList = list(product(*items))

print(productList)
# [('a', '1', '!'), ('a', '1', '@'), ('a', '1', '#'), 
#  ('a', '2', '!'), ('a', '2', '@'), ('a', '2', '#'), 
#  ('a', '3', '!'), ('a', '3', '@'), ('a', '3', '#'), 
#  ('a', '4', '!'), ('a', '4', '@'), ('a', '4', '#'), ~~ 