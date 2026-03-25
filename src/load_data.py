import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

df = pd.read_csv("data/ai4i2020.csv")

df.columns = [
    "udi",
    "product_id",
    "type",
    "air_temperature_k",
    "process_temperature_k",
    "rotational_speed_rpm",
    "torque_nm",
    "tool_wear_min",
    "machine_failure",
    "twf",
    "hdf",
    "pwf",
    "osf",
    "rnf"
]

with engine.begin() as conn:
    conn.execute(text("TRUNCATE TABLE maintenance_raw;"))

# 4. 적재
df.to_sql("maintenance_raw", engine, if_exists="append", index=False)

print("데이터 적재 완료")