from laserfarm import GeotiffWriter
import pathlib
import pathlib
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
    if 'features' in inputs:
        features = inputs['features']
    else:
        features = inputs
else:
    arg_parser.add_argument('--features', action='store' , required='True', dest='features')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

args = arg_parser.parse_args()
if not inputs_exists:
    features = args.features

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_local_tmp = pathlib.Path('/tmp')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_targets = pathlib.Path('/webdav/targets')

conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_local_tmp = pathlib.Path('/tmp')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_targets = pathlib.Path('/webdav/targets')

feature = features
remote_path_geotiffs = conf_remote_path_ahn.parent / 'geotiffs'

geotiff_export_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_targets.as_posix(),
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': remote_path_geotiffs.as_posix(),
    'cleanlocalfs': {}   
}

writer = GeotiffWriter(input_dir=feature, bands=feature).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

