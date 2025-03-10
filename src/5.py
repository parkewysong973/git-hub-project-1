import random

def get_random_code():
    """Generate a random code."""
    code = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
    return code
