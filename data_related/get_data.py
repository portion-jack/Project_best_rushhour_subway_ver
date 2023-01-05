import pandas as pd

import json
import requests
from private._private_ import app_key

mapper=pd.read_csv('raw_data/StationCode_mapper.csv',index_col=0)

# 1.1 baseline
def get_congest(st_code,dow,hh):
    """
    dow = dayofweek
    hh = hours
    """
    url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/{st_code}?dow={dow}&hh={hh}"

    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response_1 = requests.get(url, headers=headers)

    with open(f'raw_data/01_{st_code}_{dow}_{hh}.json', 'w') as outfile:
        json.dump(eval(response_1.text), outfile, indent=4)

# 1.2 baseline
def get_congest_sectional(st_code,dow,hh):
    """
    dow = dayofweek
    hh = hours
    """
    url = f"https://apis.openapi.sk.com/puzzle/congestion-car/stat/stations/{st_code}?dow={dow}&hh={hh}"

    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response_2 = requests.get(url, headers=headers)

    with open(f'raw_data/02_{st_code}_{dow}_{hh}.json', 'w') as outfile:
        json.dump(eval(response_2.text), outfile, indent=4)

# 1.3 baseline
def get_dropoff(st_code,dow,hh):
    """
    dow = dayofweek
    hh = hours
    """
    url = f"https://apis.openapi.sk.com/puzzle/get-off-car/stat/stations/{st_code}?dow={dow}&hh={hh}"

    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response_3 = requests.get(url, headers=headers)

    with open(f'raw_data/03_{st_code}_{dow}_{hh}.json', 'w') as outfile:
        json.dump(eval(response_3.text), outfile, indent=4)


# get 3 types of data
def get_data(st_code,dow,hh):
    # get_data info
    stationname, subwayline=mapper[mapper['stationCode']==st_code].loc[:,['stationName','subwayLine']].values[0]
    get_congest(st_code,dow,hh)
    get_congest_sectional(st_code,dow,hh)
    get_dropoff(st_code,dow,hh)
    print(f'{stationname}_{subwayline}_{dow}_{hh} 데이터 추출 완료')
    return None