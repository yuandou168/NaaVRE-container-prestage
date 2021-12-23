from laserchicken.filter import select_polygon
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--norm_point_cloud', action='store', type=int, required='True', dest='norm_point_cloud')


args = arg_parser.parse_args()
norm_point_cloud = args.norm_point_cloud




polygon = "POLYGON(( 131963.984125 549718.375000," + \
                   " 132000.000125 549718.375000," + \
                   " 132000.000125 549797.063000," + \
                   " 131963.984125 549797.063000," + \
                   " 131963.984125 549718.375000))"
filtered_point_cloud = select_polygon(norm_point_cloud, polygon)

import json
outs = {}
outs['filtered_point_cloud'] = filtered_point_cloud
print(json.dumps(outs))
