import time
import pandas as pd
import os
from Info import Info as log
from Data import Data 
import json
from Api import Api as api
class Read_file:
    def Read_Excel():
        try:
            time.sleep(5)
            read_excel = pd.read_excel(Data.name_file); # Path Excel
            num_rows, num_columns = read_excel.shape
            print(num_rows)
            for i in range(num_rows):
                price = 0;
                data_send = {
                    "item_id":None, #String
                    "product_name":None,#String
                    "sale_price":None, #Float
                    "discounted_price":None, #Float
                    "discounted_percentage":None, #String
                    "picture_url":None, #String
                    "product_url":None, #String
                    "maximum_commission_rate":None, #String
                    "commission":None, #Float
                    "Seller Id":None, #String
                    "promo_link":None, #String
                    "promo_short_link":None, #String
                    "address":None, #String
                    "review":0, #int
                    "group":None, #String
                    "market":"Lazada" #String
                }
                status_main = 0;
                status_detail = 0;
                # data_api;
                for j in range(len(Data.header_data)):
                    data_input = str(read_excel[Data.header_data[j]][i])
                    data_send[Data.header_data[j]] = data_input;
                    # if(j==0):
                    #     data_api = api.api_detail(data_input);
                        
                    #     if(True): #status data_api 200
                    #         data_send["group"] = Data.group
                    #         data_send["review"] = data_api["data"]["review_info"]["average_score"]
                    #         data_send["address"] = data_api["data"]["delivery_info"]["area_from"]
                    #     else:
                    #         print(log.Info("Error"))
                    #         return
                        
                    if(j==3):
                        price = float(data_input);  
                    if(j==4):
                        pass
                        discount_rate = data_send["discounted_percentage"].replace("-", "").replace("%", "") 
                        data_send["discounted_percentage"] = float(discount_rate);
                    if(j==7):
                        data_send["maximum commission_rate"] = float(data_input.replace("%", ""));
                        data_send["commission"] = data_send["maximum commission_rate"]/100*price;
                        print(log.Info("info"),"[",i+1,": commission ] ",data_send["commission"]);
                    print(log.Info("info"),"[",i+1,": "+Data.header_data[j]+" ] ",data_send[Data.header_data[j]]);
                # status_main = api.send_api_main(json.dumps(data_send))
                # if(status_main!=200):
                #     print(log.Info("Error"),status_main)
                #     return 
                # status_detail = api.send_api_detail(json.dumps(data_api));
                # if(status_detail!=200):
                #     print(log.Info("Error"),status_detail)
                #     return 
                Data.api_conf +=1;
                    
                # sender_api(json.dumps(data_send));
            
            print(log.Info("info"),"Remove ",Data.name_file)
            os.remove(Data.name_file)
        except FileNotFoundError as e:
            print(log.Info("info"),"Remove ",Data.name_file)
            os.remove(Data.name_file)
            print(log.Info("error"),e)
        