from laserfarm.remote_utils import get_wdclient
import fnmatch
from laserfarm.remote_utils import list_remote
import pathlib
import argparse
import json
from json import JSONDecodeError
arg_parser = argparse.ArgumentParser()
from os.path import exists
inputs_path = '/tmp/inputs.json'
inputs_exists = exists(inputs_path)

if inputs_exists:
    with open(inputs_path) as json_file:
        try:
            inputs = json.load(json_file)
        except JSONDecodeError:
            json_file.close()
            f = open(inputs_path, "r")
            inputs = f.readlines()[0].strip()

if inputs:
    if 'laz_files' in inputs:
        laz_files = inputs['laz_files']
    else:
        laz_files = inputs
else:
    arg_parser.add_argument('--remote_path_retiled', action='store' , required='True', dest='remote_path_retiled')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

args = arg_parser.parse_args()
if not inputs_exists:
    remote_path_retiled = args.remote_path_retiled

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
remote_path_retiled

tiles = [t.strip('/') for t in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_retiled.as_posix())
         if fnmatch.fnmatch(t, 'tile_*_*/')]

import json
with open('/tmp/outputs.json', 'w') as f:
    json.dump(tiles, f)

