## Overview

Coding task for Elisa Data Engineer position.

Testing instructions:
1. Create mysql database

```
compose -f compose_mysql.yaml up 
```
2. Create `data` table

```
CREATE TABLE data (
    id varchar(255) NOT NULL,
    date date,
    time time, 
    device_id varchar(255),
    value varchar(255),
    PRIMARY KEY (id)
);
```
3. Start api from the `__main__.py` file
4. Upload test data to mysql
```
curl "http://127.0.0.1:8000/upload"
```
5. Top 5 most utilized devices (on average) on a date
```
curl "http://127.0.0.1:8000/devices" | jq '.'
```

6. Hourly rolling average of device utilization of a device between dates
```
curl "http://127.0.0.1:8000/average/?id=4AD20C95" | jq '.'
```