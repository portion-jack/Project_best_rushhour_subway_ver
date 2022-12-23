"""
진입 역사 기준 칸 혼잡도

input
# hour 05 ~ 23
# dow MON ~ SUN

hour = 3
dow = 'MON'
sc = 626
"""
import requests
import pandas as pd
from utils.utils import without_keys
from private._private_ import app_key

hour = 8
dow = 'MON'
sc = 626

url = f"https://apis.openapi.sk.com/puzzle/congestion-car/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"

headers = {
    "accept": "application/json",
    "appkey": app_key()
}

response = requests.get(url, headers=headers)
res_dict=eval(response.text)
_main_df=pd.DataFrame([i for i in res_dict['contents']['stat'] if sum(pd.DataFrame(i['data'])['congestionCar'].values.sum()) !=0])

_main_df['subwayLine']=res_dict['contents']['subwayLine']
_main_df['stationName']=res_dict['contents']['stationName']
print(_main_df)
