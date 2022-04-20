from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient
import pathlib
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--id', action='store', type=str, required=True, dest='id')


arg_parser.add_argument('--param_webdav_token', action='store', type=str, required='True', dest='param_webdav_token')

args = arg_parser.parse_args()

id = args.id


param_webdav_token = args.param_webdav_token

conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Sevilla')

conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Sevilla')

laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]

import json
filename = "/tmp/laz_files_" + id + ".json"
file_laz_files = open(filename, "w")
file_laz_files.write(json.dumps(laz_files))
file_laz_files.close()
