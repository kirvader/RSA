import random


def gcd(a, b):
    if a * b == 0:
        return max(a, b)
    if a > b:
        return gcd(b, a % b)
    return gcd(a, b % a)


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_prime(digits):
    while True:
        num = random.randint(10 ** (digits - 1), (10 ** digits) - 1)
        if is_prime(num):
            return num


def inverse_by_module(d, mod):
    gcd_value, x, y = extended_gcd(d, mod)
    if gcd_value != 1:
        return None
    return ((x % mod) + mod) % mod


def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd_value, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_value, x, y


def pow_mod(base, exponent, mod):
    if exponent == 0:
        return 1
    result = pow_mod(base, exponent // 2, mod)
    result = (result * result) % mod
    if exponent % 2 == 1:
        return (result * base) % mod
    return result

def bytes_to_int(data: bytes):
    return int.from_bytes(data, "big")

def int_to_byte(data: int):
    return data.to_bytes(1, "big")