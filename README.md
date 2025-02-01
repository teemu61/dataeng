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
3. Disable ONLY_FULL_GROUP_BY
```
SET GLOBAL sql_mode = '';
```
4. If you are using DBeaver to access the mysql then in Connection settings -> Driver properties:
```
allowPublicKeyRetrival = true
```
5. Start app

With termianal go to dataeng project root folder (where the README.md file is located) and give command
```
poetry run python3 -m dataeng
```
Or you can open the code with PyCharm and run the app from __main__.py.

6. Upload test data to mysql
```
curl "http://127.0.0.1:8000/upload"
```
7. Top 5 most utilized devices (on average) on a date
```
curl "http://127.0.0.1:8000/devices" | jq '.'
```
8. Hourly rolling average of device utilization of a device between dates
```
curl "http://127.0.0.1:8000/average/?id=4AD20C95" | jq '.'
```