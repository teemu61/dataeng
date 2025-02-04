SET GLOBAL sql_mode = '';

CREATE TABLE data (
    id varchar(255) NOT NULL,
    date date,
    time time,
    device_id varchar(255),
    value varchar(255),
    PRIMARY KEY (id)
);