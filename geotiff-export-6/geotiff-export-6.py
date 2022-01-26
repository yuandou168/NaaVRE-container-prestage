from laserfarm import GeotiffWriter
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--features', action='store', type=, required='True', dest='features')

arg_parser.add_argument('--param_webdav_login', action='store', type=, required='True', dest='param_webdav_login')
arg_parser.add_argument('--param_webdav_password', action='store', type=, required='True', dest='param_webdav_password')

args = arg_parser.parse_args()
features = args.features

param_webdav_login = args.param_webdav_login
param_webdav_password = args.param_webdav_password

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_targets = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/targets')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}
conf_remote_path_geotiffs = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/geotiffs')

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_targets = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/targets')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}
conf_remote_path_geotiffs = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/geotiffs')

feature = features[0]

geotiff_export_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_targets.as_posix(),
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': conf_remote_path_geotiffs.as_posix(),
    'cleanlocalfs': {}   
}

writer = GeotiffWriter(input_dir=feature, bands=feature).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

