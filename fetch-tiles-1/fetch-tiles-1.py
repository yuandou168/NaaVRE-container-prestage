from laserfarm.remote_utils import list_remote
import fnmatch
from laserfarm.remote_utils import get_wdclient
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--remote_path_retiled', action='store', type=, required='True', dest='remote_path_retiled')


args = arg_parser.parse_args()
remote_path_retiled = args.remote_path_retiled


conf_wd_opts = { 'webdav_hostname': webdav_hostname, 'webdav_login': webdav_login, 'webdav_password': webdav_password}

conf_wd_opts = { 'webdav_hostname': webdav_hostname, 'webdav_login': webdav_login, 'webdav_password': webdav_password}

tiles = [t.strip('/') for t in list_remote(get_wdclient(conf_wd_opts), remote_path_retiled.as_posix())
         if fnmatch.fnmatch(t, 'tile_*_*/')]

print(tiles)
