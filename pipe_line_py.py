import os
import matplotlib.pyplot as plt
plt.rc('font',family='AppleGothic')
plt.rc('axes',unicode_minus=False)
plt.rc('date.autoformatter',minute="%H:%M")

import warnings
warnings.filterwarnings(action='ignore')

import pandas as pd
import seaborn as sns

from codes_get_data.get_congest_func import get_congest

from main_codes.read_data import read_congest,read_congest_section
from main_codes.show_congest_graph import relative_graph_morning,relative_graph_dinner
from main_codes.show_congest_sectional_graph import get_sectional_df_morning, get_sectional_df_dinner, show_sectional_graph


# stationcode mapper

codemapper=pd.read_csv('data/StationCode_mapper.csv',index_col=0)

stationname = input('찾고자 하는 지하철역 :')
stationline = input('찾고자 하는 지하철역의 호선:')

# check data

if len(codemapper[(codemapper['subwayLine']==stationline) & (codemapper['stationName']==stationname)]) != 0:
    print('추출 가능한 데이터 입니다.')
else:
    print('추출 불가한 데이터 입니다.')
    raise ValueError
"""
get_congest()
# path => data/final_data/xx역_xx호선_congest.csv
# path => data/final_data/xx역_xx호선_congest_section.csv
"""

# get data
if len([i for i in os.listdir('data/final_data/') if i.startswith('_'.join([stationname,stationline]))]) == 0:
    print('아직 존재하지 않는 데이터 입니다.')
    print('추출을 시작합니다.')
    df_target_congest,df_target_congest_sectional=get_congest(station_name=stationname,station_line=stationline)
else:
    print('이미 존재 하는 데이터 입니다.')
df_congest=read_congest()

# show graph

relative_graph_morning(df_congest,stationname,stationline)
relative_graph_dinner(df_congest,stationname,stationline)
show_sectional_graph(stationname,stationline)