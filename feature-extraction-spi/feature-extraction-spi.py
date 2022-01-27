from laserfarm import DataProcessing
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--tiles', action='store', type=list, required='True', dest='tiles')

arg_parser.add_argument('--param_hostname', action='store', type=str, required='True', dest='param_hostname')
arg_parser.add_argument('--param_login', action='store', type=str, required='True', dest='param_login')
arg_parser.add_argument('--param_password', action='store', type=str, required='True', dest='param_password')

args = arg_parser.parse_args()
tiles = args.tiles

param_hostname = args.param_hostname
param_login = args.param_login
param_password = args.param_password

conf_remote_path_targets = pathlib.Path('/webdav/targets')
conf_local_tmp = pathlib.Path('/tmp')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')

conf_remote_path_targets = pathlib.Path('/webdav/targets')
conf_local_tmp = pathlib.Path('/tmp')
conf_wd_opts = { 'webdav_hostname': param_hostname, 'webdav_login': param_login, 'webdav_password': param_password}
conf_remote_path_retiled = pathlib.Path('/webdav/retiled/')

t = tiles[2]

tile_mesh_size = 10.
features = ['perc_95_normalized_height']

grid_feature = {
    'min_x': -113107.81,
    'max_x': 398892.19,
    'min_y': 214783.87,
    'max_y': 726783.87,
    'n_tiles_side': 512
}

feature_extraction_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_retiled.as_posix(),
    'load': {'attributes': ['raw_classification']},
    'normalize': 1,
    'apply_filter': {
        'filter_type': 'select_equal', 
        'attribute': 'raw_classification',
        'value': [1, 6]#ground surface (2), water (9), buildings (6), artificial objects (26), vegetation (?), and unclassified (1)
    },
    'generate_targets': {
        'tile_mesh_size' : tile_mesh_size,
        'validate' : True,
        **grid_feature
    },
    'extract_features': {
        'feature_names': features,
        'volume_type': 'cell',
        'volume_size': tile_mesh_size
    },
    'export_targets': {
        'attributes': features,
        'multi_band_files': False
    },
    'pushremote': conf_remote_path_targets.as_posix(),
}
idx = (t.split('_')[1:])
processing = DataProcessing(t, tile_index=idx).config(feature_extraction_input).setup_webdav_client(conf_wd_opts)
processing.run()

print(features)
