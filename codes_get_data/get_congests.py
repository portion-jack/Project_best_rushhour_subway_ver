import pandas as pd
import requests
from private._private_ import app_key

def get_congest(hour,dow,sc):
    url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"
    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response = requests.get(url, headers=headers)

    res_dict=eval(response.text)

    _main_=[i for i in res_dict['contents']['stat'] if pd.DataFrame(i['data'])['congestionTrain'].sum() != 0]
    _main_df=pd.DataFrame(_main_)
    _main_df['subwayLine']=res_dict['contents']['subwayLine']
    _main_df['stationName']=res_dict['contents']['stationName']
    return _main_df

def get_congest_sectional(hour,dow,sc):
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
    return _main_df