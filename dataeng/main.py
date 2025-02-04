from fastapi import FastAPI, UploadFile
from datetime import datetime, timedelta
import mysql.connector
import random
import string


app = FastAPI()

host = 'mysql'

conn = mysql.connector.connect(
    user='myuser', password='mypassword', host=host, database='mydatabase')
cur = conn.cursor()

@app.get("/")
def hello_world():
    return {"message": "OK"}

@app.get("/devices")
async def devices():
    return devices()

@app.get("/average/")
async def average(id: str):
    return average(id)

@app.post("/upload/")
async def upload_file(file: UploadFile):
    cont_byte = file.file.read()
    cont_str = cont_byte.decode("utf-8")
    cont_dict = eval(cont_str)
    upload(cont_dict)
    return upload(cont_dict)

def devices():
    try:
        conn = mysql.connector.connect(
            user='root', password='rootpassword', host=host, database='mydatabase')
        cursor = conn.cursor()
        query = """
        SELECT date, device_id, sum, row_num FROM(
        SELECT date, time, device_id, SUM(value) AS sum,
        ROW_NUMBER() OVER (PARTITION BY date ORDER BY SUM(value) DESC) AS row_num  
        FROM data
        GROUP BY date, device_id 
        ORDER BY date, sum desc ) AS d
        WHERE row_num < 6 """
        cursor.execute(query)
        result = cursor.fetchall()

        devices_list = []
        response = {}
        for tup in result:
            if tup[3] < 5:
                devices_list.append(tup[1])
            else:
                devices_list.append(tup[1])
                response[tup[0]] = devices_list
                devices_list = []
        cursor.close()
        conn.close()
        return {'response':response}
        # return response

    except Exception as err:
        print('Error message: ' + repr(err))

def average(id: str):
    try:
        conn = mysql.connector.connect(
            user='root', password='rootpassword', host=host, database='mydatabase')
        cursor = conn.cursor()
        query = """
        SELECT
           date, time, device_id, value,
           TRUNCATE(AVG(value)
                 OVER(ORDER BY time ROWS BETWEEN 3 PRECEDING AND CURRENT ROW), 2)
                 AS moving_average
        FROM data
        WHERE device_id = '""" + id + "'"

        cursor.execute(query)
        result = cursor.fetchall()

        response = {}
        for tup in result:
            response[tup[0]] = tup[4]

        cursor.close()
        conn.close()

        return response

    except Exception as err:
        print('Error message: ' + repr(err))


def upload(dataList: dict):
    conn = mysql.connector.connect(
        user='myuser', password='mypassword', host=host, database='mydatabase')
    cur = conn.cursor()

    try:
        for i, data in enumerate(dataList):
            date_str = data['date']
            date_object = datetime.strptime(date_str, "%d-%b-%Y")
            datetime_object = datetime.strptime(date_str, "%d-%b-%Y")
            rows = []
            for j, value in enumerate(data['values']):
                date_object = datetime_object.date()
                time_object = datetime_object.time()
                device_id = data['deviceID']
                random_value = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                rows.append((random_value, date_object, time_object, device_id, value))
                datetime_object = datetime_object + timedelta(minutes=5)
            sql = "INSERT INTO data (id, date, time, device_id, value) VALUES (%s, %s, %s, %s, %s)"
            cur.executemany(sql, rows)
            conn.commit()
            print(cur.rowcount, "record inserted.")

        count = cur.rowcount
        message = f"Inserted succesfully {count} records"
        return message

    except Exception as err:
        print('Error message: ' + repr(err))