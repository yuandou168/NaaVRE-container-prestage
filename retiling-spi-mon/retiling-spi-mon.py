from laserfarm import Retiler
import argparse
import pathlib
import time
import requests

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--laz_files', action='store', type=str, required='True', dest='laz_files')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')


arg_parser.add_argument('--param_grafana_base_url', action='store', type=str, required='True', dest='param_grafana_base_url')
arg_parser.add_argument('--param_grafana_pwd', action='store', type=str, required='True', dest='param_grafana_pwd')
arg_parser.add_argument('--param_grafana_user', action='store', type=str, required='True', dest='param_grafana_user')

args = arg_parser.parse_args()
laz_files = args.laz_files

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password


param_grafana_base_url = args.param_grafana_base_url
param_grafana_pwd = args.param_grafana_pwd
param_grafana_user = args.param_grafana_user

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')

remote_path_retiled = conf_remote_path_retiled


def send_annotation(start=None,end=None,message=None,tags=None):
    if not tags:
        tags = []
    tags.append(message)
    
    headers = {
        'Accept':'application/json',
        'Content-Type': 'application/json',
    }
    data ={
      "time":start,
      "timeEnd":end,
      "created": end,
      "tags":tags,
      "text": message
    }
    resp = requests.post(param_grafana_base_url+'/api/annotations',verify=False,auth=(param_grafana_user, param_grafana_pwd),headers=headers,json=data)

start = int(round(time.time() * 1000))

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
retiler.run()

end = int(round(time.time() * 1000))
tags = [str(file)]
send_annotation(start=start,end=end,message="Retiling",tags = tags)


import json
outs = {}
outs['remote_path_retiled'] = str(remote_path_retiled)
print(json.dumps(outs))
