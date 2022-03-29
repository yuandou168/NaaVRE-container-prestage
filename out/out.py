import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--a', action='store' , required='True', dest='a')
arg_parser.add_argument('--b', action='store' , required='True', dest='b')


args = arg_parser.parse_args()
a = args.a
b = args.b




c = a + 1

d = b + a

import json
outs = {}
outs['c'] = c
outs['d'] = d
print(json.dumps(outs))
