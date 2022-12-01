import requests
from lxml import etree
import re
import json


class Data():
    url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"

    def get_data(self):
        response = requests.get(self.url)
        with open("html.txt", "w", encoding="utf-8") as file:
            file.write(response.text)

    def get_time(self):
        with open("html.txt", "r", encoding="utf-8") as file:
            text = file.read()
        time = re.findall('"mapLastUpdatedTime":"(.*?)"', text)[0]
        return time
    
    def parse_data(self):
        with open("html.txt", "r", encoding="utf-8") as file:
            text = file.read()
        html = etree.HTML(text)
        result = html.xpath('//script[@type="application/json"]/text()')
        result = json.loads(result[0])
        result = result["component"][0]["caseList"]
        result = json.dumps(result)

        with open("data.json", "w", encoding="utf-8") as file:
            file.write(result)
            print("done")
