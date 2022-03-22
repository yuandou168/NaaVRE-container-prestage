from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient
import fnmatch
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--remote_path_retiled', action='store' , type= , required='True', dest='remote_path_retiled')

arg_parser.add_argument('--param_hostname', action='store', type=, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=, required='True', dest='param_password')

args = arg_parser.parse_args()
remote_path_retiled = args.remote_path_retiled

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}

tiles = [t.strip('/') for t in list_remote(get_wdclient(conf_wd_opts), remote_path_retiled.as_posix())
         if fnmatch.fnmatch(t, 'tile_*_*/')]

print(tiles)
