from laserfarm import Retiler
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--laz_files', action='store', type=, required='True', dest='laz_files')


args = arg_parser.parse_args()
laz_files = args.laz_files


conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')
conf_wd_opts = { 'webdav_hostname': webdav_hostname, 'webdav_login': webdav_login, 'webdav_password': webdav_password}

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')
conf_wd_opts = { 'webdav_hostname': webdav_hostname, 'webdav_login': webdav_login, 'webdav_password': webdav_password}

remote_path_retiled = conf_remote_path_retiled

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

import json
outs = {}
outs['remote_path_retiled'] = remote_path_retiled
print(json.dumps(outs))
