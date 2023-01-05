# 최고의 출근시간 (지하철 ver)

## Tools

```
Data
    - SK open API
    - Json
    - csv

Tools
    - Database
    - sqlight
    - pandas
    - numpy
    - matplotlib
    - seaborn

Skills
    - using API
    - make data pipeline
    - draw datetime related plot
    - using pivot table
```

## What I learned

```
1. insert json in db is not general
2. awesome way to deal list value in DataFrame
    - df.explode, df['col'].apply(pd.Series)

```


### Images

<img width="1721" alt="Screen Shot 2022-12-26 at 18 40 48" src="https://user-images.githubusercontent.com/112222918/209533276-72878243-6807-436d-bba5-4b4439c9c468.png">

<img width="1717" alt="Screen Shot 2022-12-26 at 18 37 25" src="https://user-images.githubusercontent.com/112222918/209533054-c13e5eea-de4e-4767-b80f-cbefd710ac9b.png">

<img width="1607" alt="Screen Shot 2022-12-26 at 18 38 23" src="https://user-images.githubusercontent.com/112222918/209533095-1c940310-9d08-4842-aaa0-0c575fd1aab5.png">

### Process

```
Input
- 출발 지하철 역
- 출발 지하철 노선 (except 경의중앙선, 분당선)
- 가는 방향 (상행선/하행선)

Process
1. find next station

2. check and get current_station and next_station data
    - input 출발 (지하철 역 & 지하철 노선) 데이터가 있는지 확인
        -> 없다 추출
    - input 출발 (지하철 역 & 지하철 노선)의 다음역 데이터가 있는지 확인
        -> 없다 추출

3. informations
    - 출발역의 혼잡도 시간별 lineplot
    - 출발역의 칸별 시간별 heatmap
    - 출발역의 다음역 칸별 하차율 heatmap
```

### REPO structure

(new)
```
.
├── README.md
├── _main_.ipynb
├── data_CI.ipynb
├── data_get.ipynb
├── data_related
│   ├── check_data.py
│   ├── data_read_optimize.ipynb
│   ├── get_data.py
│   └── preprocess.py
├── database_connection.ipynb
├── depreciated_main_.ipynb
├── private
│   ├── _private_.py
│   └── private.md
├── problems.md
└── 지하철혼잡도활용_최적화.pdf

2 directories, 14 files

```


(depreciated)
```
.
├── _main_.ipynb            # ** main file ** 
│
├── _01_get_api             # 1. get_data_by api
│   └── get_api_save_json.py
│
├── _02_preprocessing       # 2. preprocess json data to dataframe
│   └── preprocessing.py
│
├── _03_data_pipeline       # 3. check_data -> get data -> preprocess data (pipeline)
│   └── data_pipeline.py
│
├── _04_data_eda            # 4. read_data by condition
│   └── read_data.py
│
├── _05_plots               # 5. show information related to data
│   └── draw_plots.py
│
│── raw_data                # json_files
│
│── preprocessed_data       # csv_files
│
├── metro_graph
│   └── metro_graph.json
├── ppt
│   ├── ASAC_김정우.pptx
│   └── 지하철혼잡도활용_최적화.pdf
├── private
│   ├── _private_.py
│   └── private.md
└── 지하철혼잡도활용_최적화.pdf

```


## Really nice learn

```
df.explode('column_name')
-> append row if data_frame value is list type
```
