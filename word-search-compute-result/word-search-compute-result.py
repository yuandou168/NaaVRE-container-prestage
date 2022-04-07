import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--found', action='store' , type=int , required='True', dest='found')


args = arg_parser.parse_args()
found = args.found




result = False
for f in found:
    result = result or f

