# Maintenance Analysis

## 프로젝트 개요
이 프로젝트는 AI4I 2020 Predictive Maintenance Dataset을 활용하여 설비 고장 패턴을 분석하고, 정비 우선순위와 운영 리스크를 파악하는 것을 목표로 합니다.

PostgreSQL 기반의 SQL 분석과 Python(pandas, matplotlib)을 활용한 데이터 적재 및 시각화를 수행했습니다.

## 사용 데이터
- AI4I 2020 Predictive Maintenance Dataset
- 출처: UCI Machine Learning Repository

## 사용 기술
- PostgreSQL
- SQL
- Python
- pandas
- SQLAlchemy
- psycopg2-binary
- matplotlib
- VSCode
- GitHub

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
├─ .gitignore
└─ README.md