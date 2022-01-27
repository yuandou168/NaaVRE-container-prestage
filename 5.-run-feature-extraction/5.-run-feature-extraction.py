from laserfarm.remote_utils import list_remote
from laserfarm import DataProcessing
import fnmatch
from laserfarm.remote_utils import get_wdclient
import argparse
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--feature_extraction_input', action='store', type=str, required='True', dest='feature_extraction_input')
arg_parser.add_argument('--last_modified', action='store', type=str, required='True', dest='last_modified')
arg_parser.add_argument('--last_run', action='store', type=str, required='True', dest='last_run')
arg_parser.add_argument('--t', action='store', type=, required='True', dest='t')

arg_parser.add_argument('--param_webdav_login', action='store', type=, required='True', dest='param_webdav_login')
arg_parser.add_argument('--param_webdav_password', action='store', type=, required='True', dest='param_webdav_password')

args = arg_parser.parse_args()
feature_extraction_input = args.feature_extraction_input
last_modified = args.last_modified
last_run = args.last_run
t = args.t

param_webdav_login = args.param_webdav_login
param_webdav_password = args.param_webdav_password

conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/retiled')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}

conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/retiled')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}
tiles = [t.strip('/') for t in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_retiled.as_posix())
         if fnmatch.fnmatch(t, 'tile_*_*/') and last_modified(conf_wd_opts, conf_remote_path_retiled/t) > last_run]


idx = [[int(el) for el in tile.split('_')[1:]] for tile in tiles]

processing = DataProcessing(t, tile_index=idx[0]).config(feature_extraction_input).setup_webdav_client(conf_wd_opts)
processing.run()

import json
outs = {}
outs['idx'] = idx
outs['tiles'] = tiles
print(json.dumps(outs))
