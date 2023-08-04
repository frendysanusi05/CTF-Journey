with open('output.txt', 'r') as f:
    data = f.read()[5:]

data = bytes.fromhex(data)
prefix = b'HTB{'
key = bytearray(4)

for i in range(len(key)):
    key[i] = prefix[i] ^ data[i]

flag = b''
for i in range(len(data)):
    flag += bytes([data[i] ^ key[i % len(key)]])
    
print(flag.decode())