import json
from map_draw import *
from data import *

with open("data.json", "r") as file:
    data = file.read()

    data = json.loads(data)

map = MyMap()
my_data = Data()
my_data.get_data()
updated_time = my_data.get_time()
my_data.parse_data()

# china map
def get_china():
    area = []
    confirmed = []

    for each in data:
        area.append(each["area"])
        confirmed.append(each["curConfirm"])
    map.to_map_china(area, confirmed, updated_time)
    


# provices map
def get_province():

    for each in data:
        city = []
        confirmed = []
        province = each["area"]

        if province == "重庆":

            for each_city in each["subList"]:
                if each_city["city"] == "武隆区":
                    each_city["city"] = "武隆县"
                elif each_city["city"] == "梁平区":
                    each_city["city"] = "梁平县"
                elif each_city["city"] == "秀山县":
                    each_city["city"] = "秀山土家族苗族自治县"
                elif each_city["city"] == "石柱县":
                    each_city["city"] = "石柱土家族自治县"
                elif each_city["city"] == "彭水县":
                    each_city["city"] = "彭水苗族土家族自治县"
                elif each_city["city"] == "酉阳县":
                    each_city["city"] = "酉阳土家族苗族自治县"
                city.append(each_city["city"])
                confirmed.append(each_city["curConfirm"])
            
            map.to_map_city(province, city, confirmed, updated_time)

        elif province == "四川":

            for each_city in each["subList"]:
                if "州" in each_city["city"] and each_city["city"] != "达州" and each_city["city"] != "泸州":
                    if each_city["city"] == "凉山州":
                        each_city["city"] = "凉山彝族自治州"
                    elif each_city["city"] == "阿坝州":
                        each_city["city"] = "阿坝藏族羌族自治州"
                    elif each_city["city"] == "甘孜州":
                        each_city["city"] = "甘孜藏族自治州"
                    city.append(each_city["city"])
                else:
                    city.append(each_city["city"]+"市")
                confirmed.append(each_city["curConfirm"])
            
            map.to_map_city(province, city, confirmed, updated_time)
                
            



get_province()

get_china()