import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--numbers', action='store', type=, required='True', dest='numbers')
arg_parser.add_argument('--sum_factor', action='store', type=int, required='True', dest='sum_factor')


args = arg_parser.parse_args()
numbers = args.numbers
sum_factor = args.sum_factor




result = numbers + sum_factor

