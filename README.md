# Hanwha Maintenance Analysis

## 프로젝트 개요
이 프로젝트는 **AI4I 2020 Predictive Maintenance Dataset**을 활용해 설비 고장 패턴을 분석하고, 정비 우선순위와 운영 리스크를 파악하는 것을 목표로 합니다.

한화시스템 지원을 위한 포트폴리오 프로젝트로, **PostgreSQL 기반 SQL 분석**과 **Python(pandas, matplotlib)** 을 활용한 데이터 적재 및 시각화를 수행했습니다.

---

## 프로젝트 목표
- 설비 고장 데이터를 PostgreSQL에 적재하고 SQL로 분석
- 장비 유형, 공구 마모도, 토크 조건에 따른 고장 리스크 파악
- 제한된 정비 자원을 우선 배분할 수 있는 기준 도출
- 분석 결과를 시각화하여 직관적으로 전달

---

## 사용 데이터
- **데이터셋명**: AI4I 2020 Predictive Maintenance Dataset
- **출처**: UCI Machine Learning Repository
- **특징**
  - 설비 운전 상태 및 고장 여부를 포함한 예지정비용 데이터
  - 장비 유형(Type), 온도, 회전 속도, 토크, 공구 마모도, 고장 여부 등의 변수 포함
  - 총 10,000건의 데이터 활용

---

## 사용 기술
- PostgreSQL
- SQL
- Python
- pandas
- SQLAlchemy
- psycopg2-binary
- matplotlib
- python-dotenv
- VSCode
- GitHub

---

## 프로젝트 구조

```text
hanwha_maintenance_project/
├─ data/
│  └─ ai4i2020.csv
├─ output/
│  └─ graphs/
│     ├─ failure_rate_by_tool_wear.png
│     ├─ failure_rate_by_torque.png
│     └─ failure_rate_by_type.png
├─ sql/
│  ├─ 01_create_table.sql
│  ├─ 02_check_data.sql
│  └─ 03_analysis.sql
├─ src/
│  ├─ analysis.py
│  └─ load_data.py
├─ .env.example
├─ .gitignore
└─ README.md
```



### 진행 과정
1. 데이터베이스 및 테이블 생성
PostgreSQL에서 hanwha_maintenance 데이터베이스를 생성하고, 원본 CSV 데이터를 저장할 maintenance_raw 테이블을 설계했습니다.
```
sql/01_create_table.sql
```
테이블 생성 SQL 작성
분석에 활용하기 쉽도록 컬럼명을 정리된 형태로 설계

### 2. 데이터 적재
Python을 활용해 CSV 파일을 읽고, PostgreSQL 테이블 컬럼 구조에 맞게 컬럼명을 변경한 뒤 데이터를 적재했습니다.
```
src/load_data.py
```
CSV 파일 로드
컬럼명 변경
테이블 초기화 후 데이터 적재

### 3. 데이터 적재 검증
SQL을 통해 행 개수, 샘플 데이터, 장비 유형별 건수를 확인하여 데이터가 정상 적재되었는지 점검했습니다.
```
sql/02_check_data.sql
```

### 4. SQL 기반 분석
PostgreSQL에서 SQL 쿼리를 사용해 전체 고장률, 장비 유형별 고장률, 고장 유형별 건수, 공구 마모 구간별 고장률, 토크 구간별 고장률을 분석했습니다.
```
sql/03_analysis.sql
```

### 5. 시각화
SQL 분석 결과를 Python으로 불러와 주요 결과를 그래프로 시각화했습니다.
```
src/analysis.py
```


# 주요 SQL 분석 결과

### 1. 전체 고장률
전체 장비 고장률은 **3.39%**로 나타났습니다.

### 2. 제품 타입별 고장률
L 타입: 3.92%
M 타입: 2.77%
H 타입: 2.09%
L 타입 장비군의 고장률이 가장 높게 나타났습니다.

### 3. 고장 유형별 발생 건수
Heat Dissipation Failure (HDF): 115건
Overstrain Failure (OSF): 98건
Power Failure (PWF): 95건
Tool Wear Failure (TWF): 46건
Random Failure (RNF): 19건

열 관련 고장과 과부하·전력 관련 고장이 주요하게 나타났습니다.

### 4. 공구 마모 구간별 고장률
under_50: 2.21%
50_99: 2.25%
100_149: 2.27%
150_plus: 5.95%

공구 마모 시간이 150분 이상인 구간에서 고장률이 크게 상승했습니다.

### 5. 토크 구간별 고장률
under_20: 14.91%
20_39: 0.59%
40_59: 3.67%
60_plus: 41.84%

토크가 적정 범위를 벗어나는 극단 구간에서 고장률이 매우 높게 나타났습니다.

## 주요 인사이트
장비 유형별 고장률 차이를 고려해 우선 점검 대상 장비군을 선별할 수 있습니다.
공구 마모도 150분 이상 구간을 예방정비 기준선으로 검토할 수 있습니다.
토크의 극단값 구간은 운영 리스크가 높아 이상 상태 조기 탐지 기준으로 활용할 수 있습니다.
열, 과부하, 전력 관련 고장이 주요 원인으로 나타나 해당 영역 중심의 예방정비 전략 수립이 가능합니다.
시각화 결과

1. 제품 타입별 고장률
2. 공구 마모 구간별 고장률
3. 토크 구간별 고장률

## 프로젝트 의의

본 프로젝트는 설비 운전 데이터와 고장 이력을 바탕으로 장비 유형, 공구 마모도, 토크 조건에 따른 고장 리스크를 분석했습니다.
분석 결과, 특정 장비 유형과 고마모·극단 토크 구간에서 고장률이 높게 나타났으며, 이를 통해 제한된 정비 자원을 우선 배분할 수 있는 기준을 도출할 수 있었습니다.
단순 EDA에 그치지 않고, 정비 우선순위와 운영 리스크 관점에서 SQL 기반 분석을 수행했다는 점에서 의미가 있습니다.

## 회고 및 보완점
- 공개 데이터 기반 프로젝트이므로 실제 군수·정비 현장의 복잡한 운영 제약은 모두 반영하지 못했습니다.
- 이후에는 정비 인력 수, 부품 재고, 다운타임 비용, 장비 중요도 같은 운영 요소를 추가해 더욱 현실적인 정비 우선순위 모델로 확장할 수 있습니다.
- 향후에는 대시보드 형태의 시각화나 예측 모델링까지 연결해 프로젝트를 발전시킬 수 있습니다.
