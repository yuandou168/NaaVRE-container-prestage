import getpass
import datetime
import pathlib



conf_remote_path_root = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/')
conf_remote_path_ahn = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/Spain/Spain_test')
conf_remote_path_retiled = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/retiled')
conf_remote_path_targets = pathlib.Path('/pnfs/grid.sara.nl/data/projects.nl/eecolidar/02_UvA/YShi/targets')
conf_local_tmp = pathlib.Path('/tmp')

last_run = datetime.datetime.strptime(input('Date last run (YYYY-MM-DD): '), '%Y-%m-%d')
conf_wd_opts = {'webdav_hostname': 'https://webdav.grid.surfsara.nl:2880', 'webdav_login': param_webdav_login, 'webdav_password': param_webdav_password}

import json
outs = {}
outs['last_run'] = last_run
print(json.dumps(outs))
