import requests
import json
import datetime
import time
nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
headers = {"Content-Type": "application/json; charset=UTF-8"}
url = "http://192.168.85.1:8080/info"
for i  in range(0,10):
    info = {"id": i, "time": nowTime}
    response = requests.post(url, data=json.dumps(info), headers=headers).text
    print(response)
    time.sleep(3)

