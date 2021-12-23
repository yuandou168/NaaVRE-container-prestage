from laserchicken import load



point_cloud = load('testdata/AHN3.las')

import json
outs = {}
outs['point_cloud'] = point_cloud
print(json.dumps(outs))
