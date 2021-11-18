import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_chunk_size', action='store', type=int, required='True', dest='param_chunk_size')

args = arg_parser.parse_args()
text_corpus = None
with open('/tmp/text_corpus.txt', 'r') as file_text_corpus:
    text_corpus = file_text_corpus.read().rstrip()

param_chunk_size = args.param_chunk_size



chunks = [text_corpus[i:i+param_chunk_size] for i in range(0, len(text_corpus), param_chunk_size)]

import json
outs = {}
with open('/tmp/chunks.txt', 'w') as file_chunks:
    file_chunks.write(chunks)
print(json.dumps(outs))
