ip = input("Enter the ip address: ")
mask = int(input("enter the subnet mask: "))
print(f"the ip address with subnet mask: {ip}/{mask}")

print("Total no of hosts required is: ", pow(2, 32-mask))

ip_split = ip.split(".")
binary = list()

for x in ip_split:
    temp = bin(int(x))[2:]
    y = temp[::-1]
    while len(y) < 8:
        y += '0'
    temp = y[::-1]
    # print(temp)
    binary.append(temp)

total = ""
for x in binary:
    total += x

# print(total)

starting_address = total[0:mask]
ending_address = total[0:mask]


while len(starting_address) < 32:
    starting_address += '0'

while len(ending_address) < 32:
    ending_address += '1'
# print(starting_address)
# print(ending_address)


for i in range(0, 32, 8):
    if i != 0:
        print('.', end="")
    print(int(starting_address[i:i+8],2),end='')
    
print("\n")
for i in range(0, 32, 8):
    if i != 0:
        print('.', end="")
    print(int(ending_address[i:i+8], 2), end="")