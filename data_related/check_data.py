import pandas as pd
from glob import glob

mapper=pd.read_csv('raw_data/StationCode_mapper.csv',index_col=0)

# 1. check if raw_data is available
def check_raw_data(st_code):
    path_li = glob(f'raw_data/??_{st_code}*.json')
    if len(path_li)==0:
        print('no raw_data available')
        return False
    else:
        print('congest_data =>', len([i for i in path_li if i.split('/')[1].startswith('01')]))
        print('congest_sectional_paths =>', len([i for i in path_li if i.split('/')[1].startswith('02')]))
        print('drop_off_paths =>', len([i for i in path_li if i.split('/')[1].startswith('03')]))
        return True


# 2. check if Integrated data is available
def check_Integrated_data(st_code):
    st_name, st_line=mapper[mapper['stationCode']==st_code].loc[:,['stationName','subwayLine']].values[0]
    path_li = glob(f'Intergrated_data/??_{st_line}_{st_name}*.csv')
    
    if len(path_li)==0:
        print('no Integrated_data available')
        return False
    
    elif len(path_li) == 3:
        print('Integrated_data available')
        return True
    
    else:
        print(f'problem in {st_name}_{st_line} data')
        return None