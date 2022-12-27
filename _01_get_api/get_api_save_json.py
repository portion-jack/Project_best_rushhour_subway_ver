import json
import requests
from private._private_ import app_key

# input_params
sc = '133'
dow = 'MON'
hh = '08'

# 1.1 baseline
def get_data_1(sc,dow,hh):
    """
    sc = stationline
    dow = dayofweek
    hh = hours
    """
    url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/{sc}?dow={dow}&hh={hh}"

    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response_1 = requests.get(url, headers=headers)

    with open(f'raw_data/01_{sc}_{dow}_{hh}.json', 'w') as outfile:
        json.dump(eval(response_1.text), outfile, indent=4)

# 1.2 baseline
def get_data_2(sc,dow,hh):
    """
    sc = stationline
    dow = dayofweek
    hh = hours
    """
    url = f"https://apis.openapi.sk.com/puzzle/congestion-car/stat/stations/{sc}?dow={dow}&hh={hh}"

    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response_2 = requests.get(url, headers=headers)

    with open(f'raw_data/02_{sc}_{dow}_{hh}.json', 'w') as outfile:
        json.dump(eval(response_2.text), outfile, indent=4)

# 1.3 baseline
def get_data_3(sc,dow,hh):
    """
    sc = stationline
    dow = dayofweek
    hh = hours
    """
    url = f"https://apis.openapi.sk.com/puzzle/get-off-car/stat/stations/{sc}?dow={dow}&hh={hh}"

    headers = {
        "accept": "application/json",
        "appkey": app_key()
    }

    response_3 = requests.get(url, headers=headers)

    with open(f'raw_data/03_{sc}_{dow}_{hh}.json', 'w') as outfile:
        json.dump(eval(response_3.text), outfile, indent=4)