#Decryptor, requires a key and input
import functions
import argparse
import base64
from os import system


def main():

    system('clear')

    parser = argparse.ArgumentParser(description='decrypts text encrypted be encryptor.py')

    input = parser.add_mutually_exclusive_group(required=True)
    input.add_argument('-in', '--input', action='store', help='input data in command line')
    input.add_argument('-if', '--infile', action='store', help='read input data from file')

    logging = parser.add_mutually_exclusive_group()
    logging.add_argument('-v', '--verbose', action='store_true', help='Verbose output')

    _key = parser.add_mutually_exclusive_group(required=True)
    _key.add_argument('-ikf', '--inkeyfile', action='store', help='Input keyfile path')
    _key.add_argument('-k', '--key', action='store', help='Input key data')

    parser.add_argument('-fo', '--messagefile', action='store', help='Output message file name', default=False)

    args = parser.parse_args()

    if args.input:
        data = args.input
    elif args.infile:
        if args.verbose:
            print(f'Attempting to read data from file:\n{args.infile}')
        data = functions.read_file(args.infile)
        if args.verbose:
            print(f'Data read successfully from file:\n{args.infile}')
    if args.key:
        _key = args.key
    elif args.inkeyfile:
        if args.verbose:
            print(f'Attempting to read key from file:\n{args.inkeyfile}')
        _key = functions.read_file(args.inkeyfile)
        if args.verbose:
            print(f'Key read successfully from file:\n{args.inkeyfile}')

    if args.verbose:
        print(f'--- Attempting to decrypt data ---')
    decrypted = functions.decrypt(_key, data)
    if args.verbose:
        print(f'--- Decrypt successful ---')

    if args.messagefile:
        if args.verbose:
            print(f'Writing decrypted data to file:\n{args.messagefile}')
        functions.write_file(data=decrypted, filepath=args.messagefile)
        print(f'Successfully written decrypted data to file:\n{args.messagefile}')
    else:
        print(f'--- Decoded message ---\n{decrypted}\n--- End of Decoded Message ---')


if __name__ == "__main__":
    main()
