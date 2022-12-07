import socket

dns = {
    "www.google.com": ["127.0.1.0", "127.0.1.1"],
    "www.amazon.in": ["194.165.0.1", "194.165.0.1"]
}

def dns_to_ip():
    name = input("Enter the domain name ")
    if name in dns:
        print(dns[name])
    if name not in dns:
        ip = input("Enter new ip address ")
        dns[name] = []
        dns[name].append(ip)

def ip_to_dns():
    found = 0
    ip = input("Enter the ip address ")
    for i in dns:
        for j in dns[i]:
            if ip == j:
                print("Found ",i)
                found = 1
    if found==0:
        inp = input("Enter the domain name ")
        dns[inp] = []
        dns[inp].append(ip)

while True:
    ch = int(input("dns_to_ip or ip_to_dns or quit (1or2or3):"))
    if ch==1:
        dns_to_ip()
    elif ch==2:
        ip_to_dns()
    else:
        break


