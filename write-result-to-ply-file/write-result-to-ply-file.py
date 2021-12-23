from laserchicken import export
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--features', action='store', type=int, required='True', dest='features')


args = arg_parser.parse_args()
features = args.features




export(features, 'my_output.ply')

