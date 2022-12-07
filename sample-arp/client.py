import json
import requests
import urllib.request
# url = 'http://ptsv2.com/t/3894f-1665744100/d/latest/json'
# r = requests.get(url)
# data = r.json()['FormValues']


# for x in data:
#     data[x] = data[x][0]


url = 'http://localhost:8090/data'

# data = requests.get(url).json()
data = urllib.request.urlopen(url).read()
data = json.loads(data)
print(data)


while True:
    ip = input("enter ip address:")
    if ip in data.keys():
        print(data[ip])
    else:
        print("ip address not found")
        mac = input("enter corresponding mac address: ")
        # urlpost = 'http://ptsv2.com/t/3894f-1665744100/data'
        data[ip] = mac
        # r = requests.post(urlpost, data=data)
    with open('data.json', 'w+') as outfile:
        json.dump(data, outfile, indent=4) 