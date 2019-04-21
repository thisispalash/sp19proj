"""
    Generates addresses matching your specific requirements
    Time taken largely dependent on the length of the string you want
    > python3 VanityGenerator.py -c Win
"""

import sys
from KeyPair import KeyPair
import argparse

def generate_address(contains=None, caseSensitive=False):

    if not caseSensitive:
        contains = None if contains == None else contains.lower()
    count = 0
    while True:
        KP = KeyPair()
        addr = KP.GetAddress().decode()

        if not caseSensitive:
            addr = addr.lower()
        
        if contains and not addr.startswith(contains):
            # print(addr,contains)
            count+=1
            continue

        print("Address: {}  ,\nKeypair: {}\n".format(addr, KP.WIF))
        print('Addresses searched:',count)
        sys.exit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("substring", type=str,
                        help="finds addresses that contain your desired substring")
    parser.add_argument("-c", "--case", default=0, action='count',
                        help="case sensitivity. Default is false")
    args = parser.parse_args()

    generate_address(contains=args.substring, caseSensitive=(args.case!=0))
