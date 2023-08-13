#%% Modules
import pandas as pd
from pandas.core.indexes.datetimes import date_range
from pandas.io.html import read_html
from pandas.io.pytables import Table
import requests
import bs4
import requests
import os

def symbol_desc(symbol:str=""):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-GB,en;q=0.5',
        'Origin': 'https://cafef.vn',
        'Connection': 'keep-alive',
        'Referer': 'https://cafef.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'TE': 'trailers',
    }

    params = (
        ('symbol', symbol),
    )

    response = requests.get('https://e.cafef.vn/info.ashx', headers=headers, params=params)
    symbol_desc = response.json()['Link']
    symbol_desc = os.path.basename(symbol_desc).replace(".chn","")[4:]
    print(symbol_desc)
    return symbol_desc

def url_from_symbol(symbol:str="",year:int=2021,quarter:str = 0,report_type:str="BS"):
    """
    URL_BS = "https://s.cafef.vn/bao-cao-tai-chinh/NLG/BSheet/2021/2/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-dau-tu-nam-long.chn"
    URL_PL = "https://s.cafef.vn/bao-cao-tai-chinh/NLG/IncSta/2021/2/0/0/bao-cao-tai-chinh-cong-ty-co-phan-dau-tu-nam-long.chn"
    URL_CF = "https://s.cafef.vn/bao-cao-tai-chinh/NLG/CashFlow/2021/2/0/0/bao-cao-tai-chinh-cong-ty-co-phan-dau-tu-nam-long.chn"
    """
    domain = "https://s.cafef.vn/bao-cao-tai-chinh"
    symbol_description = symbol_desc(symbol)
    latest = f"{year}/{quarter}/0/0" # quarter = 0 --> YEARLY
    if report_type == "BS": 
        url_report_1 = "BSheet"
        url_report_2 = "can-doi-ke-toan-"
    elif report_type == "PL":
        url_report_1 = "IncSta"
        url_report_2 = "ket-qua-hoat-dong-kinh-doanh-"
    elif report_type == "CF":
        url_report_1 = "CashFlow"
        url_report_2 = "luu-chuyen-tien-te-gian-tiep-"
    URL = f"{domain}/{symbol}/{url_report_1}/{latest}/{url_report_2}{symbol_description}.chn"
    return URL

def url_to_table(symbol:str="",year:int=2021,quarter:str = 0,report_type:str="BS",current_only:bool=False):
    URL = url_from_symbol(symbol=symbol,year=year,quarter=quarter,report_type=report_type)
    req = requests.get(URL)
    data_table = bs4.BeautifulSoup(req.content,"html.parser")\
        .find("table",attrs={"id":"tableContent"})
    text = data_table.text
    
    if "BSheet" in URL:
        break_line = "\n\n\n\n\r\n                \xa0\xa0\xa0\xa0\r\n                "
        break_line_1 = "\n\n\n\n\n\r\n                "
        break_session = "\r\n            \n"
        break_item = "\n\n\n\n\n\r\n                "
        remove_str = "\n\n\r\n                \xa0\xa0\xa0\xa0\r\n                "
        text = text.replace(break_line,"@bi").replace(break_line_1,"@bi").\
            replace(break_session,"@bs").replace(break_item,"@bi")\
                .replace(remove_str,"")
    elif "IncSta" in URL:
        break_line = "\n\n\n\n\r\n                \xa0\xa0\r\n                "
        break_line_1 = "\n\n\n\n\r\n                \xa0\xa0\xa0\xa0\r\n"
        break_session = "\r\n            \n"
        remove_str = "\n\n\r\n                \xa0\xa0\r\n                "
        text = text.replace(break_line,"@bi").replace(break_line_1,"@bi")\
            .replace(break_session,"@bs")\
            .replace(remove_str,"")
    elif "CashFlow" in URL:
        break_line = "\n\n\n\n\r\n                \r\n "
        break_line_1 = "\r\n            \n\n\n\n\n\n\n\n\r\n                \r\n                "
        break_session = "\r\n            \n"
        remove_str = "\n\n\r\n                \r\n                "
        text = text.replace(break_line,"@bi").replace(break_line_1,"@bi")\
            .replace(break_session,"@bs")\
            .replace(remove_str,"")

    data_dict = {}

    for row in text.split("@bi"):
        key = row.split("@bs")[0]
        value = row.split("@bs")[1].replace(",","").split("\n",3)
        data_dict.update({key:value})

    header = pd.read_html(req.content)[2].values.tolist()[0][1:5]

    data = pd.DataFrame(data_dict).transpose()
    data.columns = header
    data.replace("\n","",inplace=True)

    for col in header:
        data[col] = data[col].str.replace("\n","").replace("",0)
        data[col] = data[col].astype(float)

    if current_only == True:
        data = data[[header[len(header)-1]]]

    print(f"URL to Table done! Report:{report_type} Symbol:{symbol} Year:{year} Quarter:{quarter}")
    return data

print("Module & Function done!")
#%% Process data

url_to_table(symbol="PNJ",year=2018,quarter=0,report_type="BS",current_only=True)

test = url_from_symbol(symbol="PNJ",year=2021,quarter=0,report_type="BS")

BS2021 = url_to_table(URL)
BS2021 = url_to_table(URL_BS)
PL2021 = url_to_table(URL_PL)
BS2021.to_excel("demo.xlsx")

data = url_to_table(symbol="PNJ",year=2015,quarter=4,report_type="BS",\
    current_only=True)
for y in range(2016,2022):
    for q in range(1,5):
        data_quarter = url_to_table(symbol="PNJ",year=y,quarter=q,report_type="BS",current_only=True)
        data = data.merge(data_quarter,how='inner',right_index=True,left_index=True)
# %%
