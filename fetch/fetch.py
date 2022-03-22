from laserfarm.remote_utils import get_wdclient
import requests
from laserfarm.remote_utils import list_remote
import argparse
arg_parser = argparse.ArgumentParser()

arg_parser.add_argument('--conf_remote_path_ahn', action='store' , type= , required='True', dest='conf_remote_path_ahn')
arg_parser.add_argument('--conf_wd_opts', action='store' , type= , required='True', dest='conf_wd_opts')
arg_parser.add_argument('--grafana_base_url', action='store' , type= , required='True', dest='grafana_base_url')
arg_parser.add_argument('--grafana_pwd', action='store' , type= , required='True', dest='grafana_pwd')
arg_parser.add_argument('--theNotebook', action='store' , type= , required='True', dest='theNotebook')


args = arg_parser.parse_args()
conf_remote_path_ahn = args.conf_remote_path_ahn
conf_wd_opts = args.conf_wd_opts
grafana_base_url = args.grafana_base_url
grafana_pwd = args.grafana_pwd
theNotebook = args.theNotebook



    
laz_files = [f for f in list_remote(get_wdclient(conf_wd_opts), conf_remote_path_ahn.as_posix())
             if f.lower().endswith('.laz')]

def send_annotation(start=None,end=None,message=None,tags=None):
    if not tags:
        tags = []
    
    tags.append(theNotebook)
    
    headers = {
        'Accept':'application/json',
        'Content-Type': 'application/json',
    }
    
    data ={
      "dashboardId":1,
    #   "panelId":8,
      "time":start,
      "timeEnd":end,
      "created": end,
      "tags":tags,
      "text": message
    }
    resp = requests.post(grafana_base_url+'/api/annotations',verify=False,auth=('admin', grafana_pwd),headers=headers,json=data)
    
    data ={
      "dashboardId":2,
    #   "panelId":8,
      "time":start,
      "timeEnd":end,
      "created": end,
      "tags":tags,
      "text": message
    }
    resp = requests.post(grafana_base_url+'/api/annotations',verify=False,auth=('admin', grafana_pwd),headers=headers,json=data)

