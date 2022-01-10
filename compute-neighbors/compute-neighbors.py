from laserchicken import build_volume
from laserchicken import compute_neighborhoods
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--point_cloud', action='store', type=float, required='True', dest='point_cloud')
arg_parser.add_argument('--point_cloud_normalized', action='store', type=float, required='True', dest='point_cloud_normalized')


args = arg_parser.parse_args()
point_cloud = args.point_cloud
point_cloud_normalized = args.point_cloud_normalized




targets = point_cloud
volume = build_volume('sphere', radius=1)
neighborhoods = compute_neighborhoods(point_cloud_normalized, targets, volume)

import json
outs = {}
outs['neighborhoods'] = neighborhoods
outs['targets'] = targets
print(json.dumps(outs))
