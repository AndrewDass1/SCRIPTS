import random

def testing_check_multiplication():
    a = random.randint(1, 2)
    b = random.randint(1, 2)
    c = random.randint(1, 4)

    print("Variable a:", a)
    print("Variable b:", b)
    print("a * b:", a * b)
    print("Variable c:", c)

    assert a * b == c
