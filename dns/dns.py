import socket
dns ={
    "www.google.com":["127.0.1.0","127.0.1.1"],
    "www.amazon.in":["194.165.0.1" , "194.165.0.1"]
}


def dns_to_ip():
    name = input("enter domain name:")
    ip = socket.gethostbyname(name)
    print("ip:", ip)
    if name not in dns.keys():
        dns[name] = []
    if name in dns.keys():
        if ip not in dns[name]:
            dns[name].append(ip)
            
def ip_to_dns():
    found = 0
    ip = input("enter ip:")
    for i in dns:
        for j in dns[i]:
            if j == ip:
                found = 1
                print("domain", i)
                break
        if found == 1:
            break
    if found == 0:
        print("ip not found")
        
while True:
    ch = int(input("dns_to_ip or ip_to_dns or quit (1or2or3):"))
    if ch == 3:
        break
    
    if ch == 1:
        dns_to_ip()
    elif ch == 2:
        ip_to_dns()
    