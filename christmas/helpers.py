import random

def random_alpha_numeric(n):
    return ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(int(n)))