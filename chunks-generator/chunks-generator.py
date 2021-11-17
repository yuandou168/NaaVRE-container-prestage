import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--text_corpus', action='store', type='str', required='True', dest='text_corpus')

arg_parser.add_argument('--param_chunk_size', action='store', type='int', required='True', dest='param_chunk_size')

args = arg_parser.parse_args()
text_corpus = args.text_corpus

param_chunk_size = args.param_chunk_size



chunks = [text_corpus[i:i+param_chunk_size] for i in range(0, len(text_corpus), param_chunk_size)]

import json
outs = {}
outs['chunks'] = chunks
print(json.dumps(outs))
