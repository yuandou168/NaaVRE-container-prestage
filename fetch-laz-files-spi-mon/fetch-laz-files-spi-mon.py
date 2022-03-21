import requests
from laserfarm.remote_utils import get_wdclient
from laserfarm.remote_utils import list_remote
import argparse
import pathlib
import time

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

arg_parser.add_argument('--param_grafana_base_url', action='store', type=str, required='True', dest='param_grafana_base_url')
arg_parser.add_argument('--param_grafana_pwd', action='store', type=str, required='True', dest='param_grafana_pwd')
arg_parser.add_argument('--param_grafana_user', action='store', type=str, required='True', dest='param_grafana_user')


args = arg_parser.parse_args()

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

param_grafana_base_url = args.param_grafana_base_url
param_grafana_pwd = args.param_grafana_pwd
param_grafana_user = args.param_grafana_user


def send_annotation(start=None, end=None, message=None, tags=None):
    if not tags:
        tags = []
    tags.append(message)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    data = {
        "time": start,
        "timeEnd": end,
        "created": end,
        "tags": tags,
        "text": message
    }
    resp = requests.post(param_grafana_base_url + '/api/annotations', verify=False,
                         auth=(param_grafana_user, param_grafana_pwd), headers=headers, json=data)
    

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')

start = int(round(time.time() * 1000))
laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]
end = int(round(time.time() * 1000))
send_annotation(start=start,end=end,message="Fetch Laz Files")

import json
outs = {}
outs['laz_files'] = laz_files
# print(json.dumps(outs))
print(json.dumps(laz_files))
