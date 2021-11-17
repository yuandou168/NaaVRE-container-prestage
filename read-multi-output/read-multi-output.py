import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--o1', action='store', type='', required='True', dest='o1')
arg_parser.add_argument('--o2', action='store', type='', required='True', dest='o2')
arg_parser.add_argument('--o3', action='store', type='', required='True', dest='o3')


args = arg_parser.parse_args()
o1 = args.o1
o2 = args.o2
o3 = args.o3




print(o1, o2, o3)

