# 최고의 출근시간 (지하철 ver)

## TOOLS

```
--data--
apache_spark
pandas 
seaborn
```

#### REPO structure

```
.
├── main_pipeline.ipynb # pipeline by ipynb
├── pipe_line_py.py # pipeline by py
├── README.md
│
├── ## main_codes ##
│   ├── show_congest_sectional_graph.py # 칸별 혼잡도 데이터 전처리 및 그래프 생성
│   ├── show_congest_graph.py # 역별 혼잡도 데이터 전처리 및 그래프 생성
│   └── read_data.py # 칸별, 역별 혼잡도 데이터 읽어오기
│
├── 1. codes_get_data 
│   ├── get_congest.py # 역별 혼잡도 데이터 불러오기 api 불러와서 csv로 저장
│   └── get_congest_subway.py # 칸별 혼잡도 데이터 불러오기 api 불러와서 csv로 저장
│
├── 2. prerprocessing
│   ├── preprocessing_main.py # 역별 혼잡도 전처리 코드
│   └── preprocessing_congest.py # 칸별 혼잡도 전처리 코드
│
├── data
│   └── StationCode_mapper.csv # 역명에 대한 역명 코드 매퍼
│
├── private
│   ├── _private_.py # api secrete key
│   └── private.md
│
├── ppt
│   ├── Presentation1.pptx # 발표 자료
│   └── ~$Presentation1.pptx
└── utils
    └── utils.py 

7 directories, 18 files

```
