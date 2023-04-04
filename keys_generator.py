import random
from argparse import ArgumentParser

from utils import generate_prime, gcd, inverse_by_module


def generate_keys(digits_count):
    p = q = 0
    while p == q:
        p = generate_prime(digits_count)
        q = generate_prime(digits_count)
    n = p * q
    m = (p - 1) * (q - 1) // gcd(p - 1, q - 1)

    e = g = 0
    while g != 1:
        e = random.randint(3, m - 1)
        g = gcd(e, m)

    d = inverse_by_module(e, m)
    return d, e, n


def parse_args():
    parser = ArgumentParser(description='RSA keys generator')
    parser.add_argument('-d', '--digits_amount', type=int, default=9, help='Amount of digits for p and q in RSA algo.')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    private_part, public_part, MOD = generate_keys(args.digits_amount)
    print(f'Module(N): {MOD}')
    print(f'Public part(e): {public_part}')
    print(f'Private key(d): {private_part}')

# Module(N): 417512501230088267
# Public part(e): 206259799556923507
# Private key(d): 46869912338529679
