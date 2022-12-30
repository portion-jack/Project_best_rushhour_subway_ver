# 최고의 출근시간 (지하철 ver)

## TOOLS

```
API to Insight
making pipeline
```

-> 데이터 뭐가 있는지 없는지 자동체크 기능 추가 필요

### imgs

<img width="1721" alt="Screen Shot 2022-12-26 at 18 40 48" src="https://user-images.githubusercontent.com/112222918/209533276-72878243-6807-436d-bba5-4b4439c9c468.png">

<img width="1717" alt="Screen Shot 2022-12-26 at 18 37 25" src="https://user-images.githubusercontent.com/112222918/209533054-c13e5eea-de4e-4767-b80f-cbefd710ac9b.png">

<img width="1607" alt="Screen Shot 2022-12-26 at 18 38 23" src="https://user-images.githubusercontent.com/112222918/209533095-1c940310-9d08-4842-aaa0-0c575fd1aab5.png">



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
