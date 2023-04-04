from argparse import ArgumentParser

from utils import pow_mod, bytes_to_int


def write_encrypted(given_file, encrypted_file, public_key, mod):
    with open(encrypted_file, "w") as out_file:
        with open(given_file, "rb") as in_file:
            while byte := in_file.read(1):
                out_file.write(str(pow_mod(bytes_to_int(byte), public_key, mod)))
                out_file.write('\n')


def parse_args():
    parser = ArgumentParser(description='RSA encryptor')
    parser.add_argument('-i', '--input_filename', type=str, help='File which has to be encrypted.')
    parser.add_argument('-o', '--output_filename', type=str, help='File which will contain the encrypted data of the input file.')
    parser.add_argument('-e', '--public_key', type=int, help='Public key')
    parser.add_argument('-N', '--mod', type=int, help='MOD')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    write_encrypted(args.input_filename, args.output_filename, args.public_key, args.mod)
    print(f"Encrypted data is saved to {args.output_filename}")
