import ipaddress
ip = input("Enter the ip addresses")
mask = input("Enter the mask address")
result = ip+'/'+mask
print("subnet mask", result)
addr = ipaddress.ip_network(result, strict=False)
first = addr[0]
last = addr[-1]

print("first address ", first)
print("last address ", last)

        