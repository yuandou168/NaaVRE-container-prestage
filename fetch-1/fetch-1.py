from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--conf_wd_opts', action='store' , type= , required='True', dest='conf_wd_opts')


args = arg_parser.parse_args()
conf_wd_opts = args.conf_wd_opts


conf_remote_path_ahn = pathlib.Path('/webdav/ahn')

conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]

