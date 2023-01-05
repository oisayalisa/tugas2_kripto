#E1E120051_SITTI NUR HALIZA_KSA
s = []
k = ['s','a','p','u','t','r','a','1']

panjangk = len(k)
for i in range(256):
    s.append(i)
print("s = ",s)

j = 0
for i in range(256):
    key_index = k[i % panjangk]
    j = (j + s[i] + ord(key_index)) % 256

    temp = s[i]
    s[i] = s[j]
    s[j] = temp
print()
print("s = ",s)
