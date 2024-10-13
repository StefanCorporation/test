def a():
    yield 1
    yield 2
    yield 3


for i in a():
    print(i)

for j in a():
    print(j)