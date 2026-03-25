import os
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
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

os.makedirs("output/graphs", exist_ok=True)

# 제품 타입별 고장률
query_type = """
SELECT
    type,
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw
GROUP BY type
ORDER BY failure_rate_percent DESC;
"""
df_type = pd.read_sql(query_type, engine)

plt.figure(figsize=(8, 5))
plt.bar(df_type["type"], df_type["failure_rate_percent"])
plt.title("Failure Rate by Product Type")
plt.xlabel("Product Type")
plt.ylabel("Failure Rate (%)")
plt.tight_layout()
plt.savefig("output/graphs/failure_rate_by_type.png")
plt.close()

# 공구 마모 구간별 고장률
query_wear = """
SELECT
    CASE
        WHEN tool_wear_min < 50 THEN 'under_50'
        WHEN tool_wear_min < 100 THEN '50_99'
        WHEN tool_wear_min < 150 THEN '100_149'
        ELSE '150_plus'
    END AS tool_wear_group,
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw
GROUP BY tool_wear_group
ORDER BY tool_wear_group;
"""
df_wear = pd.read_sql(query_wear, engine)

plt.figure(figsize=(8, 5))
plt.bar(df_wear["tool_wear_group"], df_wear["failure_rate_percent"])
plt.title("Failure Rate by Tool Wear Group")
plt.xlabel("Tool Wear Group")
plt.ylabel("Failure Rate (%)")
plt.tight_layout()
plt.savefig("output/graphs/failure_rate_by_tool_wear.png")
plt.close()

# 토크 구간별 고장률
query_torque = """
SELECT
    CASE
        WHEN torque_nm < 20 THEN 'under_20'
        WHEN torque_nm < 40 THEN '20_39'
        WHEN torque_nm < 60 THEN '40_59'
        ELSE '60_plus'
    END AS torque_group,
    ROUND(AVG(machine_failure::numeric) * 100, 2) AS failure_rate_percent
FROM maintenance_raw
GROUP BY torque_group
ORDER BY torque_group;
"""
df_torque = pd.read_sql(query_torque, engine)

plt.figure(figsize=(8, 5))
plt.bar(df_torque["torque_group"], df_torque["failure_rate_percent"])
plt.title("Failure Rate by Torque Group")
plt.xlabel("Torque Group")
plt.ylabel("Failure Rate (%)")
plt.tight_layout()
plt.savefig("output/graphs/failure_rate_by_torque.png")
plt.close()

print("그래프 저장 완료")