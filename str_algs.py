def perevorot (a):
 print("Исходная строка:",a)
 b=""
 for i in range(len(a)):
   b=b+a[-i-1]
 print("Перевернутая строка",b)
str ="Hello, world!"
perevorot(str)