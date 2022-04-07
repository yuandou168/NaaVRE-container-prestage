import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_chunk_size', action='store', type=int, required='True', dest='param_chunk_size')
arg_parser.add_argument('--param_text_corpus', action='store', type=str, required='True', dest='param_text_corpus')

args = arg_parser.parse_args()

param_chunk_size = args.param_chunk_size
param_text_corpus = args.param_text_corpus



chunks = [param_text_corpus[i:i+param_chunk_size] for i in range(0, len(param_text_corpus), param_chunk_size)]

file_chunks = open("/tmp/chunks.json", "w")
file_chunks.write(chunks)
file_chunks.close()
