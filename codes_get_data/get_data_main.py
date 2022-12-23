import pandas as pd
import requests
from private._private_ import app_key
results = list()
hours = [7,8,9,17,18,19,20]
dows = ['MON', 'TUE', 'WED', 'THU', 'FRI']
sc = 626
for hour in hours:
    for dow in dows:
        url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"
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
                
        df_main = pd.DataFrame(using_data)
        df_main['subwayLine'] =res_dict['contents']['subwayLine']
        df_main['stationName'] =res_dict['contents']['stationName']
        results.append(df_main)
df_1=pd.concat(results)
df_1.to_csv('data/cleaned_공덕_6호선_station_congest.csv')
results = list()
hours = [7,8,9,17,18,19,20]
dows = ['MON', 'TUE', 'WED', 'THU', 'FRI']
sc = 626
for hour in hours:
    for dow in dows:
        url = f"https://apis.openapi.sk.com/puzzle/congestion-car/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"
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
                if sum(train['congestionCar']) == 0:
                    count += 1
            if count == 0:
                using_data.append(trains)

        df_main = pd.DataFrame(using_data)
        df_main['subwayLine'] =res_dict['contents']['subwayLine']
        df_main['stationName'] =res_dict['contents']['stationName']
        results.append(df_main)
df_2=pd.concat(results)
df_2.to_csv('data/cleaned_공덕_6호선_station_congest_sectional.csv')
