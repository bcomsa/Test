m1 = '2d0710181b01111f0817171401071c11091a0a'
m2 = '3c091311111a1a0e180003120d1a0811091a0a'
#m1 = '3b101c091d53320c000910'
#m2 = '071d154502010a04000419'
m1 = '1e1a1e0e170a16160100101f0a1c080714081e150f0c'
m2 = '071d15031e12020a011c1b1e040b0c12010c031b0c08'
m3 =  hex(int(m1,16)^int(m2,16))[2:-1]
key = ''.join(str(hex((ord(x))))[2:] for x in 'a')
keyxor = int(key,16)
print m1,m2,m3
for x in range(0,len(m3) - len(key) + 1,2):
	print x
	text = [] 
	crib = ''.join(m3[y:y+2]for y in range(x,x + len(key),2))
	for y in range(0,len(key),2):
		text.append(chr(int(crib[y:y+2],16) ^ int(key[y:y+2],16)))
	print ''.join(text)
