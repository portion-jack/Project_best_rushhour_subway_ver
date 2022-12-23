"""
하차인원 비율

input
# hour 05 ~ 23
# dow MON ~ SUN

hour = 3
dow = 'MON'
sc = 626
"""
import requests
import numpy as np
import pandas as pd
from utils.utils import without_keys
from private._private_ import app_key

hour = 8
dow = 'MON'
sc = 626

url = f"https://apis.openapi.sk.com/puzzle/get-off-car/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"

headers = {
    "accept": "application/json",
    "appkey": app_key()
}

response = requests.get(url, headers=headers)

res_dict = eval(response.text)

_main_df=pd.DataFrame(res_dict['contents']['stat'])
_main_df['subwayLine']=res_dict['contents']['subwayLine']
_main_df['stationName']=res_dict['contents']['stationName']
print(_main_df)
