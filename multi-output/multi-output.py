


o1 = 42
o2 = "String String"
o3 = 'Other test string'

import json
outs = {}
outs['o1'] = o1
outs['o2'] = o2
outs['o3'] = o3
print(json.dumps(outs))
