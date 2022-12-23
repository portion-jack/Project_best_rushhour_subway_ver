"""
진입 역사 기준 열차 혼잡도

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

results = list()
hours = [7,8,9,17,18,19,20]
dows = ['MON', 'TUE', 'WED', 'THU', 'FRI']
for hour in hours:
    for dow in dows:
        url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/626?dow={dow}&hh={str(hour).zfill(2)}"
        headers = {
            "accept": "application/json",
            "appkey": app_key()
        }

        response = requests.get(url, headers=headers)

        res_dict=eval(response.text)
        using_data = list()
        for trains in res_dict['contents']['stat']:
            count = 0
            for train in trains['data']:
                if train['congestionTrain'] == 0:
                    count += 1
            if count == 0:
                using_data.append(trains)
        df_main = pd.concat(using_data)
        df_main['subwayLine'] =res_dict['contents']['subwayLine']
        df_main['stationName'] =res_dict['contents']['stationName']
        results.append(df_main)
ans=pd.concat(results)