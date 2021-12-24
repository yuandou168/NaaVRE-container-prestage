from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient
import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_webdav_login', action='store', type=str, required='True', dest='param_webdav_login')
arg_parser.add_argument('--param_webdav_password', action='store', type=str, required='True', dest='param_webdav_password')

args = arg_parser.parse_args()

param_webdav_login = args.param_webdav_login
param_webdav_password = args.param_webdav_password

conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Spain_test')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}

conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Spain_test')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}

laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]

print(laz_files)
