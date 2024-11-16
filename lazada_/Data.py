import os
# item_id:{type:String},
# product_name:{type:String},
# sale_price:{type:Number},
# discounted_price:{type:Number},
# discounted_percentage:{type:String},
# picture_url:{type:String},
# product_url:{type:String},
# maximum_commission_rate:{type:String},
# commission:{type:Number},
# Seller_Id:{type:String},
# promo_link:{type:String},
# promo_short_link:{type:String},
# address:{type:String},
# group:{type:String},
# market:{type:String}
class Data:
    count_product = 0;
    product_total = 0;
    is_product = 5000;
    group = "Test"
    is_run = False
    parth_image = "./image/"
    url = "https://adsense.lazada.co.th/index.htm#!/offer/product_offer"
    # ชื่อไฟล์ภาพที่ต้องการค้นหาบนหน้าจอ
    image_to_find = parth_image+"type.png"
    select_product = parth_image+"select_all.png"
    get_link = parth_image+"getlink_.png"
    export_link = parth_image+"export_.png"
    product_image = parth_image+"product_image.png"
    path_file = os.getcwd();
    name_file = path_file+"\download\data_promo_list.xlsx";
    space_ = parth_image+"space.png"
    header_data = [
        "item_id",
        "product_name",
        "sale_price",
        "discounted_price",
        "discounted_percentage",
        "picture_url",
        "product_url",
        "maximum commission_rate",
        "Seller Id",
        "promo_link",
        "promo_short_link"
    ]
