a = input("숫자를 입력하세요")
print("입력한 숫자는 : " + a)
a = int(a)
if a>5:
	print("크다")
else:
	print("작다")
for in i range(10):
	if a%i==0:
		print(i)