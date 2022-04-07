import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--chunks', action='store' , type=str , required='True', dest='chunks')

arg_parser.add_argument('--param_word', action='store', type=str, required='True', dest='param_word')

args = arg_parser.parse_args()
chunks = args.chunks

param_word = args.param_word



found = param_word in chunks.split()

import json
file_found = open("/tmp/found.json", "w")
file_found.write(json.dumps(found))
file_found.close()
