# how to use argparser for command line interface

import sys
import argparse


def main():
    parser = argparse.ArgumentParser()  # from the case of ArgumentParser it is a class., so parser is a class
    parser.add_argument('--x', type=float, default=1.0, help='What is the first number')
    parser.add_argument('--y', type=float, default=1.0, help='What is the second number')
    parser.add_argument('--operation', type=str, default="add", help='What operation?(add,sub,mul,div)')
    args = parser.parse_args()
    print(calculation(args))


def calculation(args):
    if args.operation == "add":
        return args.x + args.y
    elif args.operation == "sub":
        return args.x - args.y
    elif args.operation == "mul":
        return args.x * args.y
    elif args.operation == "div":
        return args.x / args.y

"""
ensures that the code only runs, if it is that py file that is being run.  So if that py file is being imported
for functions/classes in it, the code that is under the name/main  wont run. Without it, the code would run every
time the file was imported and that'd be annoying
"""

if __name__ == '__main__':
    main()
