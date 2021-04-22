import requests

url='http://172.17.0.1:8888'
for i in range(0,15):
    response=requests.get(url)
    print(response.text)
