import ipaddress

addr = input("enter ip address: ")
mask = input("enter mask: ")
network = ipaddress.ip_network(addr + '/' + mask, strict=False)

print("1. Subnet mask: ", network.netmask)
print("2. No. of address in each subset is", network.num_addresses)
print("3.1. First address:", network.network_address)
print("3.2. Last address:", network.broadcast_address)
