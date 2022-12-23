import requests
import pandas as pd
from private import _private_

url = "https://apis.openapi.sk.com/puzzle/subway/stations"
headers = {
    "accept": "application/json",
    "appkey": _private_.app_key()
}
response = requests.get(url, headers=headers)

StationCode_dict=eval(response.text)
pd.DataFrame(StationCode_dict['contents']).to_csv('data/StationCode_mapper.csv')