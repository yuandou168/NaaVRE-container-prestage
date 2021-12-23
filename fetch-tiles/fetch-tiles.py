from laserfarm.remote_utils import get_wdclient
from laserfarm.remote_utils import list_remote
import fnmatch
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--remote_path_retiled', action='store', type=, required='True', dest='remote_path_retiled')

arg_parser.add_argument('--param_webdav_token', action='store', type=, required='True', dest='param_webdav_token')

args = arg_parser.parse_args()
remote_path_retiled = args.remote_path_retiled

param_webdav_token = args.param_webdav_token

conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}

conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}

tiles = [t.strip('/') for t in list_remote(get_wdclient(conf_wd_opts), remote_path_retiled.as_posix())
         if fnmatch.fnmatch(t, 'tile_*_*/')]

print(tiles)
