from argparse import ArgumentParser

from utils import pow_mod, int_to_byte


def write_decoded(given_file, encoded_file, private_key, mod):
    with open(encoded_file, "wb") as out_file:
        with open(given_file, "r") as in_file:
            encoded_bytes = in_file.readlines()
            for encoded_byte in encoded_bytes:
                out_file.write(int_to_byte(pow_mod(int(encoded_byte), private_key, mod)))


def parse_args():
    parser = ArgumentParser(description='RSA decoder')
    parser.add_argument('-i', '--input_filename', type=str, help='Encoded file which has to be decrypted.')
    parser.add_argument('-o', '--output_filename', type=str, help='File which will contain the decoded data of the encoded input file.')
    parser.add_argument('-d', '--private_key', type=int, help='Private key')
    parser.add_argument('-N', '--mod', type=int, help='MOD')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    write_decoded(args.input_filename, args.output_filename, args.private_key, args.mod)
    print(f"Decoded data is saved to {args.output_filename}")
