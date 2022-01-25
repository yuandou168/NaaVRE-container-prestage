import fnmatch
from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--remote_path_retiled', action='store', type=, required='True', dest='remote_path_retiled')

arg_parser.add_argument('--param_webdav_login', action='store', type=, required='True', dest='param_webdav_login')
arg_parser.add_argument('--param_webdav_password', action='store', type=, required='True', dest='param_webdav_password')

args = arg_parser.parse_args()
remote_path_retiled = args.remote_path_retiled

param_webdav_login = args.param_webdav_login
param_webdav_password = args.param_webdav_password

conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}

conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}

tiles = [t.strip('/') for t in list_remote(get_wdclient(conf_wd_opts), remote_path_retiled.as_posix())
         if fnmatch.fnmatch(t, 'tile_*_*/')]

import json
outs = {}
outs['t'] = t
outs['tiles'] = tiles
print(json.dumps(outs))
