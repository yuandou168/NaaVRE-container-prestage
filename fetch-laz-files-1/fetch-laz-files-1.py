from laserfarm.remote_utils import list_remote
from laserfarm.remote_utils import get_wdclient

conf_wd_opts = { 'webdav_hostname': webdav_hostname, 'webdav_login': webdav_login, 'webdav_password': webdav_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')

conf_wd_opts = { 'webdav_hostname': webdav_hostname, 'webdav_login': webdav_login, 'webdav_password': webdav_password}
conf_remote_path_ahn = pathlib.Path('/webdav/ahn')

laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]

print(laz_files)
