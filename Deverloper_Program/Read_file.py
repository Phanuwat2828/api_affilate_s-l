import time
import pandas as pd
import os
from Info import Info as log
from Data import Data 
import json
import re
from Api import Api as api
from dotenv import load_dotenv
from datetime import datetime
load_dotenv()

class Read_file:


    def add_product_to_json(new_product, filename):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)

            if "data" in data:
                data["data"].append(new_product)
            else:
                data["data"] = [new_product]
        except FileNotFoundError:
            data = {"data": [new_product]}
        
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def Read_Excel():
        try:
            time.sleep(10)
            read_excel = pd.read_excel(Data.name_file_lazada); # Path Excel
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
                    "sold":None, #int
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
                            print(data_input)
                            data_api = api.api_detail_lazada(data_input);
                            try:
                                status_detail = data_api['data']['code']
                            except Exception as e:
                                status_detail = 200;
                            print(data_api)
                            k=0; 
                            while(status_detail==200 and k<2):
                                k+=1;
                                if(status_detail == 200): #status data_api 200
                                    data_send["group"] = Data.selected_option
                                    try:
                                        data_send["address"] = data_api["data"]["delivery_info"]["area_from"]
                                        print(data_send["address"])
                                        if(data_send["address"]==None):
                                            data_send["address"] = "ไม่ระบุที่อยู่"
                                        else:
                                            try:
                                                provinces_pattern = "|".join(Data.provinces)
                                                matches = re.findall(provinces_pattern, data_send["address"])
                                                data_send["address"] = matches[0]
                                            except Exception as ex:
                                                print(ex);
                                    except Exception as e:
                                        data_send["address"] = "ไม่ระบุที่อยู่"
                                    try:
                                        data_send["review"] = data_api["data"]["review_info"]["average_score"]
                                    except Exception as e:
                                        data_send["review"] = 0;
                                    try:
                                        data_send["sold"] = data_api["data"]['sold']
                                    except Exception as e:
                                        data_send["sold"] = 0;
                                    print(log.Info("info"),"[",i+1,": address ] ",data_send["address"]);
                                    print(log.Info("info"),"[",i+1,": sold ] ",data_send["sold"]);
                                else:
                                    Read_file.add_product_to_json(data_send,Data.parth_error_lazada)
                                    print(log.Info("error"),status_detail)
                                    break
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
                    if(Data.header_data[j]=="maximum commission_rate"):
                        data_send["commission_rate"] = float(data_input.replace("%", ""));
                        data_send["commission"] = data_send["commission_rate"]/100*price;
                        print(log.Info("info"),"[",i+1,": commission ] ",data_send["commission"]);
                        print(log.Info("info"),"[",i+1,": group ] ",data_send["group"]);
                        print(log.Info("info"),"[",i+1,": review ] ",data_send["review"]);
                    
        
                print(log.Info("info")+"Read product [",i+1,"]")
                if(Data.is_api and status_detail==200):
                    try:
                        status_main = api.send_api_main(json.dumps(data_send))
                        if(status_main!=200):
                            print(log.Info("error"),status_main)
                        status_detail = api.send_api_detail(json.dumps(data_api['data']));
                        if(status_detail!=200):
                            print(log.Info("error"),status_detail)
                        if(status_detail==200 and status_main==200):
                            Data.api_conf +=1;
                    except Exception as e:
                        print(log.Info("error"),e);
                else:
                    print(log.Info("error"),"ไม่มีข้อมูลจาก API ไม่สามารถส่งได้ Data Detail NONE")
           
                # sender_api(json.dumps(data_send));
            print(log.Info("info"),"Remove File",Data.name_file_lazada)
            os.remove(Data.name_file_lazada)
        except FileNotFoundError as e:
            print(log.Info("info"),"Remove File",Data.name_file_lazada)
            os.remove(Data.name_file_lazada)
            print(log.Info("error"),e)

    def process_split(value):
        product_id = value.split('/')[4]  
        print(log.Info("info")+" split ",value);
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
                return "404"
                print(log.Info("info")+"No files found in the folder.")
        else:
            return "404"
            print(log.Info("info")+"Folder does not exist.")

    def convert_to_integer(s):
        if 'พัน' in s:
            return int(float(s.replace('พัน', '')) * 1000);
        elif 'ล้าน' in s:
            return int(float(s.replace('ล้าน', '')) * 1000000);
        else:
            return int(s)

    def format_1(price_text):
        price_without_symbol = price_text.replace("฿", "")
        price_without_symbol = price_without_symbol.replace(",", "")
        return float(price_without_symbol)
    
    def format_2(price_text):
        price_without_symbol = price_text.replace("%", "")
        return float(price_without_symbol)

    def Read_csv():
        try:
            time.sleep(5)
            df = pd.read_csv(Data.name_file2+Read_file.file_shopee())
            num_rows, num_columns = df.shape
            is_ = Data.is_product
            # Data.product_total<Data.is_product and
            for i in range(num_rows):
                data_send = {
                    "item_id":None, #String
                    "product_name":None,#String
                    "sale_price":None, #Float
                    "sold":None, #int
                    "product_url":None, #String
                    "commission_rate":None, #String
                    "commission":None, #Float
                    "promo_link":None, #String
                    "address":None, #String
                    "review":None, #Int
                    "market":"shopee", #String
                    "affiliate_link":None, #String
                    "picture_url":None, #String 
                    "group":Data.selected_option #String
                }
                for j in range(len(Data.header_csv)):
                    data_input = str(df[Data.header_csv[j]][i]);
                    if(Data.header_csv[j]=="ลิงก์สินค้า"):    
                        shop_id = Read_file.process_split(data_input);
                        data_send[Data.head_key[Data.header_csv[j]]] = data_input;
                        if(Data.is_api):
                            k=0;
                            status_detail = 0;
                            while(status_detail!=200 and k<2):
                                data_detail = api.api_detail_shopee(data_send[ "item_id"],shop_id);
                                print(data_detail);
                                try:
                                    status_detail = data_detail['data']['code']
                                except Exception as e:
                                    status_detail = 200;
                                print(log.Info("info"),"status_Detail",status_detail)
                                if(status_detail == 200):
                                    try:
                                        data_send["review"] = int(data_detail["data"]["review_info"]["rating_star"])
                                    except Exception as e:
                                        data_send["review"] = 0;
                                    try:
                                        data_send["address"] = data_detail["data"]["shop_info"]["shop_location"]
                                        print(log.Info("test"),data_send["address"]);
                                        if(data_send["address"]=="Overseas"):
                                            data_send["address"] = "ต่างประเทศ"
                                        else:
                                            try:
                                                provinces_pattern = "|".join(Data.provinces)
                                                matches = re.findall(provinces_pattern, data_send["address"])
                                                data_send["address"] = matches[0]
                                                print(log.Info("test"),data_send["address"]);
                                            except Exception as ex:
                                                data_send["address"] = "ไม่ระบุที่อยู่"
                                                print(log.Info("test"),ex);
                                    except Exception as e:
                                        data_send["address"] = "ไม่ระบุที่อยู่"
                                    try:
                                        data_send["picture_url"] = data_detail["data"]["main_imgs"][0]
                                    except Exception as e:
                                        data_send["picture_url"] = ""
                                    print(log.Info("info"),i+1," :","review","=",data_send["review"]);
                                    print(log.Info("info"),i+1," :","address","=",data_send["address"]);
                                    print(log.Info("info"),i+1," :","picture_url","=",data_send["picture_url"]);
                                k+=1;
                                time.sleep(2)
                    elif(Data.header_csv[j]=="ราคา"):
                        data_send[Data.head_key[Data.header_csv[j]]] = Read_file.format_1(data_input)
                    elif(Data.header_csv[j]=="ขาย"):
                        data_send[Data.head_key[Data.header_csv[j]]] = Read_file.convert_to_integer(data_input)
                    elif(Data.header_csv[j]=="อัตราค่าคอมมิชชัน"):
                        data_send[Data.head_key[Data.header_csv[j]]] = Read_file.format_2(data_input)
                    elif(Data.header_csv[j]=="คอมมิชชัน"):
                        data_send[Data.head_key[Data.header_csv[j]]] = Read_file.format_1(data_input)
                    elif(Data.header_csv[j]=="ลิงก์ข้อเสนอ"):
                        data_send["affiliate_link"] = data_input
                    else:
                        data_send[Data.head_key[Data.header_csv[j]]] = data_input;
                    print(log.Info("info"),i+1," :",Data.header_csv[j],"=",data_send[Data.head_key[Data.header_csv[j]]]);
                if(Data.is_api and status_detail==200):
                    try:
                        status_main = api.send_api_main(json.dumps(data_send))
                        if(status_main!=200):
                            print(log.Info("Error"),status_main)
                        status_detail = api.send_api_detail(json.dumps(data_detail['data']));
                        if(status_detail!=200):
                            print(log.Info("Error"),status_detail)
                        if status_main==200 and status_detail==200 :
                            Data.api_conf+=1;
                    except Exception as e:
                        print(log.Info("error")+e);
                else:
                    print(log.Info("error"),"ไม่มีข้อมูลจาก API ไม่สามารถส่งได้ Data Detail NONE")
                
                time.sleep(2)
                Data.product_total+=1;
                # data_detail = api.api_detail_shopee(data_send[ "item_id"],shop_id);
                # print( sender_api_main(json.dumps(data_send)))
            print(log.Info("info"),"Remove File",Data.name_file2+Read_file.file_shopee())
            os.remove(Data.name_file2+Read_file.file_shopee())
        except FileNotFoundError as e:
            print(log.Info("info"),"Remove File",Data.name_file2+Read_file.file_shopee())
            os.remove(Data.name_file2+Read_file.file_shopee())
            print(log.Info("error"),e)
    
    def ReadExcelLazada():
        df = pd.DataFrame();
        time.sleep(5)
        df = pd.read_excel(Data.name_file_lazada)
        
        df.columns = df.columns.str.replace(" ", "_")
        columns = [
            "item_id", "product_name", "sale_price", "discounted_price",
            "picture_url", "product_url", "brand", "maximum_commission_rate", "promo_short_link"
        ]
        # ตรวจสอบว่าคอลัมน์ที่ต้องการมีอยู่จริง มิฉะนั้นจะเกิด KeyError
        missing_columns = [col for col in columns if col not in df.columns]
        if missing_columns:
            raise KeyError(f"Missing columns: {missing_columns}")
        
        df = df[columns]

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        new_filename = os.path.join("./success_file/", f"{timestamp}_success.xlsx")
        os.rename(Data.name_file_lazada, new_filename)
        print(log.Info("warning") + "อ่านไฟล์เรียบร้อย");
        return df.to_dict(orient="records")


