from laserchicken import compute_features
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--filtered_point_cloud', action='store', type=, required='True', dest='filtered_point_cloud')
arg_parser.add_argument('--neighborhoods', action='store', type=, required='True', dest='neighborhoods')
arg_parser.add_argument('--targets', action='store', type=, required='True', dest='targets')

arg_parser.add_argument('--param_volume', action='store', type=, required='True', dest='param_volume')

args = arg_parser.parse_args()
filtered_point_cloud = args.filtered_point_cloud
neighborhoods = args.neighborhoods
targets = args.targets

param_volume = args.param_volume



features = compute_features(filtered_point_cloud, neighborhoods, targets, ['std_z','mean_z','slope'], param_volume)

import json
outs = {}
outs['features'] = features
print(json.dumps(outs))
