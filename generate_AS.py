from random import randint, shuffle


def solver(array):
    return sorted(array, key=abs)



for _ in range(20):
    t = list(range(-99, 100))
    shuffle(t)
    t = t[:randint(1, 20)]
    ans = solver(t)
    print('{{\n"input": {0},\n"answer": {1}\n}},\n'.format(t, ans))
