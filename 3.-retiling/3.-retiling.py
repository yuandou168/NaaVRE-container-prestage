from laserfarm import Retiler
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--laz_files', action='store', type=list, required='True', dest='laz_files')

arg_parser.add_argument('--param_webdav_login', action='store', type=str, required='True', dest='param_webdav_login')
arg_parser.add_argument('--param_webdav_password', action='store', type=str, required='True', dest='param_webdav_password')

args = arg_parser.parse_args()
laz_files = args.laz_files

param_webdav_login = args.param_webdav_login
param_webdav_password = args.param_webdav_password

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/AHN3/Test_las')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}
conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/retiled')

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/AHN3/Test_las')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}
conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/retiled')


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

file = laz_files[0]

retiler = Retiler(file).config(retiling_input).setup_webdav_client(conf_wd_opts)
retiler.run()

