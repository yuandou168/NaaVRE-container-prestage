import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_list_size', action='store', type=int, required='True', dest='param_list_size')

args = arg_parser.parse_args()

param_list_size = args.param_list_size



sum_factor = 10 + param_list_size

import json
outs = {}
outs['sum_factor'] = sum_factor
print(json.dumps(outs))
