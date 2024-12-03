import requests
import json
from Info import Info as log
from Data import Data as dt
class Api:
    def send_api_main(data):
        # main
        url_Api = dt.url_main
        payload = {
            "key":dt.key_api_sender_main,
            "datas":data 
        }
        try:
            response = requests.request("POST",url_Api,data=payload)
            print(log.Info("info")+"Send Main");
            return response.status_code
        except Exception as e:
            return e
        
    def send_api_detail(data):
        # main
        url_Api = dt.url_detail
        payload = {
            "key":dt.key_api_sender_detail,
            "datas":data 
        }
        try:
            response = requests.request("POST",url_Api,data=payload)
            print(log.Info("info")+"Send Detail");
            return response.status_code
        except Exception as e:
            return e

    def api_detail_lazada(value):
        url = "http://api.openchinaapi.com/v1/lazada/products/"+value+"?nation=th"
        payload={}
        headers = {
            'Authorization':dt.token_data
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if(response.status_code == 200):
            data = json.loads(response.text);
            print(log.Info("info")+"Data Detail");
            return data
        else:
            print(log.Info("error"),response.status_code);
            return 0

    def api_detail_shopee(id_product,shop_id):
        url = "http://api.openchinaapi.com/v1/shopee/products/"+id_product+"/?shop_id="+shop_id+"&nation=th"
        payload={}
        print(url);
        headers = {
            'Authorization':dt.token_data
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if(response.status_code == 200):
            data = json.loads(response.text);
            print(log.Info("info")+" APi Detail");
            return data
        else:
            print(log.Info("error"),response.status_code);
            return 0