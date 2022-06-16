from itertools import product

ret = []
for i in product([1,2,3],'ab'):
    ret.append(i)
print(ret)

ret = []
for i in product([1,2,3], repeat=2):
    ret.append(i)
print(ret)


def product2(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for n in product2(arr, r-1):
                yield [arr[i]] + n

for i in product2([1,2,3], 3):
    print(i, end="")
