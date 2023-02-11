"""
Encrypts UTF-8 Documents and strings with a randomly generated key.

Follows one time pad logic. Hoping to expand this to all data types at some point!

"""
#Decryptor, requires a key and input
import functions
import argparse
import base64
from os import system

def main():
    system('clear')

    parser = argparse.ArgumentParser(description='Encrypts data and provides a key for decryption.')

    input = parser.add_mutually_exclusive_group(required=True)
    input.add_argument('-m', '--message', action='store', help='input a message in command line')
    input.add_argument('-if', '--infile', action='store', help='read input message from file')

    logging = parser.add_mutually_exclusive_group()
    logging.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    #parser.add_argument('-s', '--seed', type=int, action='store', help='Seed value for random number generation. Int only', default=False)
    parser.add_argument('-okf', '--keypath', action='store', help='Output key file')
    parser.add_argument('-of', '--outfile', action='store', help='Output file name')

    args = parser.parse_args()

    #if args.seed:
        #print('--- WARNING ---\nKey generation with the seed value is NOT cryptographically secure. Use no seed value for cryptographically secure data.')

    if args.message:
        data = args.message
    elif args.infile:
        if args.verbose:
            print(f'Attempting to read data from file:\n{args.infile}')
        data = functions.read_file(args.infile)
        if args.verbose:
            print(f'Data read successfully from file:\n{args.infile}')
    if args.verbose:
        print(f'--- Encoding in base64 ---')
    try:
        data = bytes(data, encoding='utf-8')
        data = base64.b64encode(data)
        data = str(data)[2:-1]
    except:
        print('Base64 conversion failed')
        functions.exit_program()

    if args.verbose:
        print(f'--- Generating key size {len(data)} ---')
    if args.seed:
        if args.verbose:
            print(f'--- Key seed {args.seed} ---')
        _key = functions.less_random_key(len(data))
    else:
        _key = functions.random_key(len(data))
    if args.verbose:
        print(f'--- Generated key ---')
    if args.keypath:
        if args.verbose:
            print(f'Writing key to file:\n{args.keypath}')
        functions.write_file(_key, args.keypath)
        if args.verbose:
            print(f'Succesfully written key to file:\n{args.keypath}')
    else:
        print(f'Generated Key:\n{_key}')

    if args.verbose:
        print('--- Attempting to encrypt data ---')
    encrypted = functions.encrypt(_key, data)
    if args.verbose:
        print('--- Encryption successful ---')

    if args.outfile:
        if args.verbose:
            print(f'Writing data to file:\n{args.outfile}')
        functions.write_file(data=encrypted, filepath=args.outfile)
        print(f'Successfully written data to file:\n{args.outfile}')
    else:
        print(f'--- Encrypted message ---:\n{encrypted}\n--- End of Encrypted Message ---')



if __name__ == "__main__":

    main()
