def add(a, b):
    return a + b

def sum_three_numbers(a, b, c):
    # CODE SMELL: duplicate logic
    return add(add(a, b), c)
