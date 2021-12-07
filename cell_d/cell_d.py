import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--a', action='store', type=int, required='True', dest='a')
arg_parser.add_argument('--c', action='store', type=, required='True', dest='c')


args = arg_parser.parse_args()
a = args.a
c = args.c




d = a + c

