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
    first = True
    selected_option = 'อุปกรณ์-อิเล็กทรอนิกส์';
    count_product = 0;
    product_total = 0;
    is_product = 0;
    api_conf = 0;
    group = "Test"
    is_run = False
    is_api = True
    mode = "lazada"
    parth_image = "./image/"
    url = "https://adsense.lazada.co.th/index.htm#!/offer/product_offer"
    image_to_find = parth_image+"type.png"
    

    select_product_lazada = parth_image+"select_all.png"
    get_link_lazada = parth_image+"getlink_.png"
    export_link_lazad = parth_image+"export_.png"
    product_image_lazada = parth_image+"product_image.png"
    product_image1_lazada = parth_image+"product_image2.png"
    path_file = os.getcwd();
    folder_down = path_file+"\download"
    name_file_lazada = path_file+"\download\data_promo_list.xlsx";
    space_lazada = parth_image+"space.png"
    icon_lazada =  parth_image+"icon_lazada.png"
    header_data = [
        "item_id",
        "product_name",
        "sale_price",
        "picture_url",
        "product_url",
        "maximum commission_rate",
        "promo_short_link"
    ]
    options_lazada = [
        'อุปกรณ์-อิเล็กทรอนิกส์',
        'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
        'ทีวีและเครื่องใช้ในบ้าน',
        'สุขภาพและความงาม',
        'ทารกและของเล่น',
        'ของชำและสัตว์เลี้ยง',
        'บ้านและไลฟ์สไตล์',
        'แฟชั่นและเครื่องประดับผู้หญิง',
        'แฟชั่นและเครื่องประดับผู้ชาย',
        'กีฬาและการเดินทาง',
        'ยานยนต์และรถจักรยานยนต์',
    ]
    select_product_shopee = parth_image+"select_shopee.png"
    get_link_shopee = parth_image+"get_link_shopee.png"
    take_link_shopee = parth_image+"take_link_shopee.png"
    change_page_shopee = parth_image+"change_page_shopee.png"
    cant_shopee = parth_image+"cant_shopee.png"
    cant2_shopee = parth_image+"cant2_shopee.png"
    space_shopee = parth_image+"space_shopee.png"
    name_file2 = path_file+"\download\\";
    icon_shopee =  parth_image+"icon_shopee.png"
    header_csv = [
        "รหัสสินค้า",
        "ชื่อสินค้า",
        "ราคา",
        "ขาย",
        "อัตราค่าคอมมิชชัน",
        "คอมมิชชัน",
        "ลิงก์สินค้า",
        "ลิงก์ข้อเสนอ"
    ]

    head_key = {
        "รหัสสินค้า":"item_id",
        "ชื่อสินค้า":"product_name",
        "ราคา": "sale_price",
        "ขาย":"sold",
        "อัตราค่าคอมมิชชัน":"commission_rate",
        "คอมมิชชัน":"commission",
        "ลิงก์สินค้า":"product_url",
        "ลิงก์ข้อเสนอ":"promo_link"
    }
    options_shopee = [
        'อุปกรณ์-อิเล็กทรอนิกส์',
        'อุปกรณ์เสริม-อิเล็กทรอนิกส์',
        'ทีวีและเครื่องใช้ในบ้าน',
        'สุขภาพและความงาม',
        'ทารกและของเล่น',
        'ของชำและสัตว์เลี้ยง',
        'บ้านและไลฟ์สไตล์',
        'แฟชั่นและเครื่องประดับผู้หญิง',
        'แฟชั่นและเครื่องประดับผู้ชาย',
        'กีฬาและการเดินทาง',
        'ยานยนต์และรถจักรยานยนต์',
    ]




