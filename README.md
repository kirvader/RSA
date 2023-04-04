# Usage of RSA digital signature

There are 3 tools: keys generator, decoder and encoder. Example is given at the end of the doc.

```
RSA keys generator

options:
  -h, --help            show this help message and exit
  -d DIGITS_AMOUNT, --digits_amount DIGITS_AMOUNT
                        Amount of digits for p and q in RSA algo.
```

```
RSA encoder

options:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input_filename INPUT_FILENAME
                        File which has to be encoded.
  -o OUTPUT_FILENAME, --output_filename OUTPUT_FILENAME
                        File which will contain the encoded data of the input file.
  -e PUBLIC_KEY, --public_key PUBLIC_KEY
                        Public key
  -N MOD, --mod MOD     MOD
```

```
RSA decoder

options:
  -h, --help            show this help message and exit
  -i INPUT_FILENAME, --input_filename INPUT_FILENAME
                        Encoded file which has to be decrypted.
  -o OUTPUT_FILENAME, --output_filename OUTPUT_FILENAME
                        File which will contain the decoded data of the encoded input file.
  -d PRIVATE_KEY, --private_key PRIVATE_KEY
                        Private key
  -N MOD, --mod MOD     MOD
```

# Example of usage

### Keys generating
```cmd
python keys_generator.py -d 9
```
Output example:
```
Module(N): 395411861266357709
Public part(e): 187346351850403369
Private key(d): 12485841584289487
```

### Encoding
```
python encoder.py -i temp/example.txt -o temp/encrypted_example.txt -e 187346351850403369 -N 395411861266357709
```

Output example:
```
Encoded data is saved to temp/encrypted_example.txt
```

### Decoding
```
python decoder.py -i temp/encoded_example.txt -o temp/decoded_example.txt -d 12485841584289487 -N 395411861266357709
```

Output example:
```
Decoded data is saved to temp/decoded_example.txt
```