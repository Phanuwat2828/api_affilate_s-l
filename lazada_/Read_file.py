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
            for i in range(num_rows):
                price = 0;
                data_send = {
                    "item_id":None, #String
                    "product_name":None,#String
                    "sale_price":None, #Float
                    "picture_url":None, #String
                    "product_url":None, #String
                    "commission_rate":None, #String
                    "commission":None, #Float
                    "affiliate_link":None, #String
                    "address":None, #String
                    "sold":0, #int
                    "review":None, #int
                    "group":None, #String
                    "market":"lazada" #String
                }
                status_main = 0;
                status_detail = 0;
                for j in range(len(Data.header_data)):
                    data_input = str(read_excel[Data.header_data[j]][i])
                    data_send[Data.header_data[j]] = data_input;
                    if(Data.header_data[j]=="item_id"):
                        data_send["item_id"] = data_input;
                        if(Data.is_api):
                            data_api = api.api_detail_shopee(data_input);
                            status_detail = data_api['code']
                            if(status_detail == 200): #status data_api 200
                                data_send["group"] = Data.selected_option
                                data_send["review"] = data_api["data"]["review_info"]["average_score"]
                                data_send["address"] = data_api["data"]["delivery_info"]["area_from"]
                            else:
                                print(log.Info("Error"),status_detail)
                                return
                    if(Data.header_data[j]=="product_name"):
                        data_send["product_name"] = data_input;
                    if(Data.header_data[j]=="sale_price"):
                        data_send["sale_price"] = data_input;
                        price = float(data_input);  
                    if(Data.header_data[j]=="picture_url"):
                        data_send["picture_url"] = data_input;
                    if(Data.header_data[j]=="product_url"):
                        data_send["product_url"] = data_input;
                    if(Data.header_data[j]=="promo_short_link"):
                        data_send["affiliate_link"] = data_input;
                    # if(j==4):
                    #     pass
                    #     discount_rate = data_send["discounted_percentage"].replace("-", "").replace("%", "") 
                    #     data_send["discounted_percentage"] = float(discount_rate);
                    if(Data.header_data[j]=="maximum commission_rate"):
                        data_send["commission_rate"] = float(data_input.replace("%", ""));
                        data_send["commission"] = data_send["commission_rate"]/100*price;
                        print(log.Info("info"),"[",i+1,": commission ] ",data_send["commission"]);
                        print(log.Info("info"),"[",i+1,": group ] ",data_send["group"]);
                        print(log.Info("info"),"[",i+1,": review ] ",data_send["review"]);
                        print(log.Info("info"),"[",i+1,": address ] ",data_send["address"]);
                    # print(log.Info("info"),"[",i+1,": "+Data.header_data[j]+" ] ",data_send[Data.header_data[j]]);
                print(log.Info("info")+"Read product [",i+1,"]")
                if(Data.is_api):
                    status_main = api.send_api_main(json.dumps(data_send))
                    if(status_main!=200):
                        print(log.Info("Error"),status_main)
                        return 
                    status_detail = api.send_api_detail(json.dumps(data_api['data']));
                    if(status_detail!=200):
                        print(log.Info("Error"),status_detail)
                        return 
                Data.api_conf +=1;
                # sender_api(json.dumps(data_send));
            print(log.Info("info"),"Remove File",Data.name_file)
            os.remove(Data.name_file)
        except FileNotFoundError as e:
            print(log.Info("info"),"Remove File",Data.name_file)
            os.remove(Data.name_file)
            print(log.Info("error"),e)

    def process_split(value):
        product_id = value.split('/')[4]  
        print(log.Info("info")+"split ",value);
        return product_id

    def file_shopee():
        path_file = os.getcwd();
        folder_path = path_file+"\download"
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            if files:
                for file in files:
                    return file
            else:
                print(log.Info("info")+"No files found in the folder.")
        else:
            print(log.Info("info")+"Folder does not exist.")

    def Read_csv():
        try:
            Data.name_file2 += Read_file.file_shopee()
            df = pd.read_csv(Data.name_file2)
            num_rows, num_columns = df.shape
            for i in range(num_rows):
                data_send = {
                    "item_id":None, #String
                    "product_name":None,#String
                    "sale_price":None, #Float
                    "sold":None, #String
                    "name_seller":None, #String
                    "product_url":None, #String
                    "commission_rate":None, #String
                    "commission":None, #Float
                    "promo_link":None, #String
                    "place":None, #String
                    "shop_id":None,#String
                    "market":"Shopee" #String
                }
                for j in range(len(Data.header_csv)):
                    data_input = str(df[Data.header_csv[j]][i])
                    data_send[Data.head_key[Data.header_csv[j]]] = data_input;
                    if(j==7):    
                        data_send['shop_id'] = Read_file.process_split(data_input);
                        print(log.Info("info"),i+1," :","รหัสร้านค้า","=",data_send['shop_id']);
                    print(log.Info("info"),i+1," :",Data.header_csv[j],"=",data_send[Data.head_key[Data.header_csv[j]]]);
                # data_detail = api.api_detail_shopee(data_send[ "item_id"],data_send['shop_id']);
                # print( sender_api_main(json.dumps(data_send)))
            print(log.Info("info"),"Remove File",Data.name_file2)
            # os.remove(Data.name_file2)
        except FileNotFoundError as e:
            print(log.Info("info"),"Remove File",Data.name_file2)
            # os.remove(Data.name_file2)
            print(log.Info("error"),e)
    

        