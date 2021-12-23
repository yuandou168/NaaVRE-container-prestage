from laserfarm import GeotiffWriter
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--features', action='store', type=list, required='True', dest='features')

arg_parser.add_argument('--param_webdav_token', action='store', type=, required='True', dest='param_webdav_token')

args = arg_parser.parse_args()
features = args.features

param_webdav_token = args.param_webdav_token

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Sevilla')
conf_remote_path_targets = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/targets')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}

conf_local_tmp = pathlib.Path('/tmp')
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Sevilla')
conf_remote_path_targets = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/targets')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_token': param_webdav_token}

feature = features[0]
remote_path_geotiffs = conf_remote_path_ahn.parent / 'geotiffs'

geotiff_export_input = {
    'setup_local_fs': {'tmp_folder': conf_local_tmp.as_posix()},
    'pullremote': conf_remote_path_targets.as_posix(),
    'parse_point_cloud': {},
    'data_split': {'xSub': 1, 'ySub': 1},
    'create_subregion_geotiffs': {'output_handle': 'geotiff'},
    'pushremote': remote_path_geotiffs.as_posix(),
    'cleanlocalfs': {}   
}

writer = GeotiffWriter(input_dir=feature, bands=feature).config(geotiff_export_input).setup_webdav_client(conf_wd_opts)
writer.run()

