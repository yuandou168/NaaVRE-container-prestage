import requests
import argparse
arg_parser = argparse.ArgumentParser()


arg_parser.add_argument('--param_grafana_base_url', action='store', type=str, required='True', dest='param_grafana_base_url')
arg_parser.add_argument('--param_grafana_pwd', action='store', type=str, required='True', dest='param_grafana_pwd')

args = arg_parser.parse_args()

param_grafana_base_url = args.param_grafana_base_url
param_grafana_pwd = args.param_grafana_pwd



    
def send_annotation(start=None,end=None,message=None,tags=None):
    if not tags:
        tags = []
    # tags.append(theNotebook)
    tags.append(message)
    
    headers = {
        'Accept':'application/json',
        'Content-Type': 'application/json',
    }
    # for dashboardId in range(30):
    data ={
      # "dashboardId":dashboardId,
    #   "panelId":8,
      "time":start,
      "timeEnd":end,
      "created": end,
      "tags":tags,
      "text": message
    }
    resp = requests.post(param_grafana_base_url+'/api/annotations',verify=False,auth=('admin', param_grafana_pwd),headers=headers,json=data)
    
    # data ={
    #   "dashboardId":8,
    # #   "panelId":8,
    #   "time":start,
    #   "timeEnd":end,
    #   "created": end,
    #   "tags":tags,
    #   "text": message
    # }
    # resp = requests.post(param_grafana_base_url+'/api/annotations',verify=False,auth=('admin', param_grafana_pwd),headers=headers,json=data)

