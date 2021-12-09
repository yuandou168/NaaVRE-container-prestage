import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--k', action='store', type=int, required='True', dest='k')
arg_parser.add_argument('--s', action='store', type=, required='True', dest='s')


args = arg_parser.parse_args()
k = args.k
s = args.s



 
for i in range(1000000):
 
    # even index elements are positive
    if i % 2 == 0:
        s += 4/k
    else:
 
        # odd index elements are negative
        s -= 4/k
 
    # denominator is odd
    k += 2
     
print(s)

