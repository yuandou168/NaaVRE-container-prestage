from laserchicken.normalize import normalize
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--point_cloud', action='store', type=, required='True', dest='point_cloud')


args = arg_parser.parse_args()
point_cloud = args.point_cloud




norm_point_cloud = normalize(point_cloud)

import json
outs = {}
outs['norm_point_cloud'] = norm_point_cloud
print(json.dumps(outs))
