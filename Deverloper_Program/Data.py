import os
class Data:
    provinces = [
    "กรุงเทพมหานคร", "กระบี่", "กาญจนบุรี", "กาฬสินธุ์", "กำแพงเพชร", "ขอนแก่น", "จันทบุรี", "ฉะเชิงเทรา", 
    "ชลบุรี", "ชัยนาท", "ชัยภูมิ", "ชุมพร", "เชียงราย", "เชียงใหม่", "ตรัง", "ตราด", "ตาก", "นครนายก", 
    "นครปฐม", "นครพนม", "นครราชสีมา", "นครศรีธรรมราช", "นครสวรรค์", "นนทบุรี", "นราธิวาส", "น่าน", 
    "บึงกาฬ", "บุรีรัมย์", "ปทุมธานี", "ประจวบคีรีขันธ์", "ปราจีนบุรี", "ปัตตานี", "พระนครศรีอยุธยา", 
    "พะเยา", "พังงา", "พัทลุง", "พิจิตร", "พิษณุโลก", "เพชรบุรี", "เพชรบูรณ์", "แพร่", "ภูเก็ต", 
    "มหาสารคาม", "มุกดาหาร", "แม่ฮ่องสอน", "ยโสธร", "ยะลา", "ร้อยเอ็ด", "ระนอง", "ระยอง", "ราชบุรี", 
    "ลพบุรี", "ลำปาง", "ลำพูน", "เลย", "ศรีสะเกษ", "สกลนคร", "สงขลา", "สตูล", "สมุทรปราการ", 
    "สมุทรสงคราม", "สมุทรสาคร", "สระแก้ว", "สระบุรี", "สิงห์บุรี", "สุโขทัย", "สุพรรณบุรี", "สุราษฎร์ธานี", 
    "สุรินทร์", "หนองคาย", "หนองบัวลำภู", "อ่างทอง", "อำนาจเจริญ", "อุดรธานี", "อุตรดิตถ์", 
    "อุทัยธานี", "อุบลราชธานี", "บึงกาฬ"
    ]

    token_user_lazada = "e7ad5dcedc004a94a8fa563b6268107a";

    path_file = os.getcwd();
    setting_insert = open(path_file+'\setting.txt',mode='r',encoding='utf-8');
    def setting(setting_insert):
        data = setting_insert.readlines()
        data_setting = []
        for i in range(len(data)):
            data_setting.append(data[i].replace('\n','').split('=')[1]);
        return data_setting;
    setting = setting(setting_insert)
    url_main = setting[0]
    key_api_sender_main = setting[1]
    url_detail = setting[2]
    key_api_sender_detail = setting[3]
    token_data = setting[4]
    is_api = True
    if(setting[5] == "False"):
        is_api = False


    first = True
    selected_option = 'อุปกรณ์-อิเล็กทรอนิกส์';
    count_product = 0;
    product_total = 0;
    is_product = 0;
    api_conf = 0;
    group = "Test"
    is_run = False
    mode = "lazada"
    parth_image = path_file+"\image\\"
    url = "https://adsense.lazada.co.th/index.htm#!/offer/product_offer"
    image_to_find = parth_image+"type.png"
    

    select_product_lazada = parth_image+"select_all.png"
    get_link_lazada = parth_image+"getlink_.png"
    export_link_lazad = parth_image+"export_.png"
    product_image_lazada = parth_image+"product_image.png"
    product_image1_lazada = parth_image+"product_image2.png"
 
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
    select_product_shopee2 = parth_image+"select_shopee2.png"
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
        "ลิงก์ข้อเสนอ":"affiliate_link"
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
        "ตั๋วและบัตรกำนัน"
    ]
    parth_error = path_file+"\error\\"
    parth_error_lazada = parth_error+"error_lazada.json"




