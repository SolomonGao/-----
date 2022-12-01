import requests
from lxml import etree
import json
import openpyxl


url = "https://voice.baidu.com/act/newpneumonia/newpneumonia"

response = requests.get(url)

html = etree.HTML(response.text)
result = html.xpath('//script[@type="application/json"]/text()')
result = result[0]
result = json.loads(result)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "China"
ws.append(["provice", "confirmed", "died", "cured", "curConfirm", "confirmedRelative", "diedRelative", "curedRelative", "curConfirmRelative"])

result_CN = result["component"][0]["caseList"]
result_GL = result["component"][0]["globalList"]

for each in result_CN:
    ws.append([each["area"],each["confirmed"],each["died"],each["crued"],each["curConfirm"],
              each["confirmedRelative"],each["diedRelative"],each["curedRelative"],each["curConfirmRelative"]])

for each in result_GL:
    sheet_tile = each["area"]
    ws_out = wb.create_sheet(sheet_tile)
    ws_out.append(["country", "confirmed", "died", "cured", "curConfirm", "confirmedRelative"])
    for country in each["subList"]:
        ws_out.append([country["country"], country["confirmed"], country["died"], country["crued"], country["curConfirm"], country["confirmedRelative"]])

wb.save("./data.xlsx")
