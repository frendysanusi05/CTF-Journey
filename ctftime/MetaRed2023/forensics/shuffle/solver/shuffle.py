import binascii

with open('shuffle.png', 'rb') as f:
    buff = f.read()

out_hex = ['{:02X}'.format(b) for b in buff]

for i in range(2, len(out_hex)-3, 6):
    temp1 = out_hex[i]
    temp2 = out_hex[i+1]
    out_hex[i] = out_hex[i+2]
    out_hex[i+1] = out_hex[i+3]
    out_hex[i+2] = temp1
    out_hex[i+3] = temp2

with open('shuffle_out.png', 'wb') as f:
    for i in out_hex:
        chunk = binascii.unhexlify(i.strip())
        f.write(chunk)