from laserfarm import Retiler
import pathlib
import pathlib
import pathlib
import argparse
arg_parser = argparse.ArgumentParser()
from os.path import exists
import json
inputs_path = '/tmp/inputs.json'
inputs_exists = exists(inputs_path)

if inputs_exists:
    with open(inputs_path) as json_file:
        inputs = json.load(json_file)

if inputs_exists:
    if 'laz_files' in inputs:
        laz_files = inputs['laz_files']
    elif isinstance(inputs,list):
        laz_files = inputs
else:
    arg_parser.add_argument('--laz_files', action='store' , required='True', dest='laz_files')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

args = arg_parser.parse_args()
if not inputs_exists:
    laz_files = args.laz_files

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')
conf_local_tmp = pathlib.Path('/tmp')

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')
conf_local_tmp = pathlib.Path('/tmp')

remote_path_retiled = str(conf_remote_path_retiled)

grid_retile = {
    'min_x': -113107.81,
    'max_x': 398892.19,
    'min_y': 214783.87,
    'max_y': 726783.87,
    'n_tiles_side': 512
}


retiling_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_ahn.as_posix(),
    'set_grid': grid_retile,
    'split_and_redistribute': {},
    'validate': {},
    'pushremote': conf_remote_path_retiled.as_posix(),
    'cleanlocalfs': {}
}

file = laz_files
retiler = Retiler(file).config(retiling_input).setup_webdav_client(conf_wd_opts)
retiler_output = retiler.run()

import json
with open('/tmp/outputs.json', 'w') as f:
    json.dump(remote_path_retiled, f)

