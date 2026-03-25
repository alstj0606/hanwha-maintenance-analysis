DROP TABLE IF EXISTS maintenance_raw;

CREATE TABLE maintenance_raw (
    udi INTEGER,
    product_id VARCHAR(20),
    type VARCHAR(5),
    air_temperature_k NUMERIC(10,2),
    process_temperature_k NUMERIC(10,2),
    rotational_speed_rpm INTEGER,
    torque_nm NUMERIC(10,2),
    tool_wear_min INTEGER,
    machine_failure INTEGER,
    twf INTEGER,
    hdf INTEGER,
    pwf INTEGER,
    osf INTEGER,
    rnf INTEGER
);