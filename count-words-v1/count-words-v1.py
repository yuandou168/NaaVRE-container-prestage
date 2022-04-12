import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')

arg_parser.add_argument('--chunks', action='store' , type=str , required='True', dest='chunks')


args = arg_parser.parse_args()

id = args.id

chunks = args.chunks




count = len(chunks)

import json
filename = "/tmp/count_" + id + ".json"
file_count = open(filename, "w")
file_count.write(json.dumps(count))
file_count.close()
