from fractions import Fraction
print "Tinh y(n) = x(n)*h(n)"

print "Nhap chieu dai x(n)"
lenX = int(raw_input())
print "Nhap tung phan tu cua x(n)"
X = []
for i in range(0, lenX):
	X.append(Fraction(raw_input()))
print "Nhap vi tri bat dau cua X(n)"
posX = int(raw_input())

print "Nhap chieu dai h(n)"
lenH = int(raw_input())
print "Nhap tung phan tu cua h(n)"
H = []
for i in range(0, lenH):
	H.append(Fraction(raw_input()))
print "Nhap vi tri bat dau cua h(n)"
posH = int(raw_input())

start = posX + posH
end = lenX + lenH -1

temp = []
i = lenH - 1
while i > -1:
	temp.append(H[i])
	i -= 1
print "<==============>"
for i in range (0, end - start):
	output = "y(" + str(start+i) + ") = "
	sum = 0
	for j in range (0, lenX):
		output += str(X[j]) + "*"
		if ((lenH - 1 - i + j) > -1) & ((lenH - 1 - i + j) < lenH):
			output += str(temp[lenH - 1 - i + j])
			sum += X[j] * temp[lenH - 1 - i + j]
		else:
			output += str(0)
		if len(output) < 8 + 8*(j+1):
			output += " "*(8 + 8*(j+1) - len(output))
	output += " = " + str(sum)
	print output





