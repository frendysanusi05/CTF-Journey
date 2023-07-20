from Crypto.Util.number import *

N = 2095975199372471
e = 5449
ct = "{ciphertext}"

# use factordb.com to get p and q
p = {factor1}
q = {factor2}

#get totient(n) / (phi)
phi = (p-1)*(q-1)
d = inverse(e, phi)

res = []
for i in ct.split():
    c = int(i)
    m = pow(c, d, N)
    res.append(str(long_to_bytes(m))[2:-1])

print(''.join(res))