import openpyxl
from wordcloud import WordCloud

# read data
wb = openpyxl.load_workbook("data.xlsx")

# get work sheet
ws = wb["China"]
frequency = dict()
for row in ws.values:
    if row[0] == "provice":
        pass
    else:
        frequency[row[0]] = float(row[1])



frequency_out = dict()
sheet_name = wb.sheetnames
for each in sheet_name:
    if "洲" in each:
        ws = wb[each]
        for row in ws.values:
            if row[0] == "country":
                pass
            else:
                frequency_out[row[0]] = float(row[1])



def geberate_pic(frequency, name):
    wordcloud = WordCloud(font_path="C:\Windows\Fonts\SIMHEI.TTF", 
                    background_color="White",
                    width=1024, height=720)
    wordcloud.generate_from_frequencies(frequency)
    wordcloud.to_file("%s.png", name)