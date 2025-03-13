import random

def get_random_number(n):
    return random.randint(0, n)

if __name__ == "__main__":
    num = get_random_number(10)
    print(num)
