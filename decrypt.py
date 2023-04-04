from argparse import ArgumentParser

from utils import pow_mod, int_to_byte


def write_decrypted(given_file, encrypted_file, private_key, mod):
    with open(encrypted_file, "wb") as out_file:
        with open(given_file, "r") as in_file:
            encrypted_bytes = in_file.readlines()
            for encrypted_byte in encrypted_bytes:
                out_file.write(int_to_byte(pow_mod(int(encrypted_byte), private_key, mod)))


def parse_args():
    parser = ArgumentParser(description='RSA encryptor')
    parser.add_argument('-i', '--input_filename', type=str, help='Encrypted file which has to be decrypted.')
    parser.add_argument('-o', '--output_filename', type=str, help='File which will contain the decrypted data of the encrypted input file.')
    parser.add_argument('-d', '--private_key', type=int, help='Private key')
    parser.add_argument('-N', '--mod', type=int, help='MOD')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    write_decrypted(args.input_filename, args.output_filename, args.private_key, args.mod)
    print(f"Decrypted data is saved to {args.output_filename}")
