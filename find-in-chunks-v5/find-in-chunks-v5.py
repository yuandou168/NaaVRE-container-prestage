import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--chunks', action='store' , type=str , required='True', dest='chunks')

arg_parser.add_argument('--param_word', action='store', type=str, required='True', dest='param_word')

args = arg_parser.parse_args()

id = args.id

chunks = args.chunks

param_word = args.param_word



found = param_word in chunks.split()

import json
filename = "/tmp/found_" + id + ".json"
file_found = open(filename, "w")
file_found.write(json.dumps(found))
file_found.close()
