from laserchicken import compute_neighborhoods
from laserchicken import build_volume
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--filtered_point_cloud', action='store', type=, required='True', dest='filtered_point_cloud')
arg_parser.add_argument('--norm_point_cloud', action='store', type=, required='True', dest='norm_point_cloud')


args = arg_parser.parse_args()
filtered_point_cloud = args.filtered_point_cloud
norm_point_cloud = args.norm_point_cloud




targets = norm_point_cloud
neighborhoods = compute_neighborhoods(filtered_point_cloud, targets, param_volume)

import json
outs = {}
outs['neighborhoods'] = neighborhoods
outs['targets'] = targets
print(json.dumps(outs))
