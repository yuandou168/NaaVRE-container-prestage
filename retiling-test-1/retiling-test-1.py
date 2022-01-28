from laserfarm import Retiler
import argparse
import pathlib

arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--laz_files', action='store' , required='True', dest='laz_files')

arg_parser.add_argument('--param_webdav_token', action='store', type=str, required='True', dest='param_webdav_token')

args = arg_parser.parse_args()
laz_files = args.laz_files

param_webdav_token = args.param_webdav_token

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/retiled')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Sevilla')

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/retiled')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Sevilla')

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
outs['remote_path_retiled'] = str(remote_path_retiled)
print(json.dumps(outs))
