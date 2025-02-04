## Overview

Coding task for Elisa Data Engineer position.

Testing instructions:

1. Set up containers
```
docker compose up
```
2. Open following url with browser

```
http://0.0.0.0:8000/docs
```

3. Updload test data to database

```
curl -X 'POST' \
  'http://0.0.0.0:8000/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@data.json;type=application/json'
 ```

4. Top 5 most utilized devices (on average) on a date

```
curl -X 'GET' \
  'http://0.0.0.0:8000/devices' \
  -H 'accept: application/json'  
```

5. Hourly rolling average of device utilization of a device between dates

```
curl -X 'GET' \
  'http://0.0.0.0:8000/average/?id=6D3A2286' \
  -H 'accept: application/json'
```

6. Shut down containers

```
docker compose down
```