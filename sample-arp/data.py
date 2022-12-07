import json

ip_mac = {
    "10.0.2.5": '00:16:3e:99:0b:db',
    "10.0.5.5": '00:16:4e:99:0b:db',
    "11.0.2.5": '00:16:5e:99:0b:db',
    "15.0.2.5": '00:15:7c:99:0b:db' ,
    "17.0.2.5": '00:20:3d:99:0b:db',
}

with open('data.json', 'w+') as outfile:
    json.dump(ip_mac, outfile, indent=4) 