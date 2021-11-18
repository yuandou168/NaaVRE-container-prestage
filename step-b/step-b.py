import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_list_size', action='store', type=int, required='True', dest='param_list_size')

args = arg_parser.parse_args()

param_list_size = args.param_list_size



numbers = [el for el in range(0, param_list_size)]

import json
outs = {}
outs['numbers'] = numbers
print(json.dumps(outs))
