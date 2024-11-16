import requests
import json
from Info import Info as log
class Api:
    def send_api_main(data):
        # main
        url_Api = "http://26.49.17.12:8080/0eea90b98ea1129c8f7c16af9bca09820d5564ac93678c9766000941f5444ade"
        payload = {
            "key":"5a3dec84301206e275f7ca7fa119796c8a5be05d100a2d23ba3a4f189876d03a",
            "datas":data 
        }

        try:
            response = requests.request("POST",url_Api,data=payload)
            return response.status_code
        except:
            return {"status":404,"message":"POST API ERROR."}
        
    def send_api_detail(data):
        # main
        url_Api = "http://26.49.17.12:8080/5564ac93678c9766000941f5444ade0eea90b98ea1129c8f7c16af9bca09820d"
        payload = {
            "key":"5a3dec84301206e275f7ca7fa119796c8a5be05d100a2d23ba3a4f189876d03a",
            "datas":data 
        }
        try:
            response = requests.request("POST",url_Api,data=payload)
            return response.status_code
        except:
            return {"status":404,"message":"POST API ERROR."}

    def api_check(value):
        url = "http://api.openchinaapi.com/v1/lazada/products/"+value+"?nation=th"
        payload={}
        headers = {
            'Authorization':'Token '
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if(response.status_code == 200):
            data = json.loads(response.text);
            print(log.Info("info")+"Check Data");
            return data['data']
        else:
            print("Error",response.status_code);