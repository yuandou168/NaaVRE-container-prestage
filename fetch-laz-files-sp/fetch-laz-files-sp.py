from laserfarm.remote_utils import get_wdclient
from laserfarm.remote_utils import list_remote
import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

args = arg_parser.parse_args()

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')

conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]

print(laz_files)
