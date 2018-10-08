a = int(input("请输入第一个数撒"))
b = int(input("请输入第二个数撒"))
if a < b:
    (a,b) = (b,a)
print(a,b)

for i in (range(b,0,-1)):
    if a % i == 0 and b % i == 0 :
        print("最大公约数%d" %(i))
        print("最大公倍数%d"%((a*b)//i))
        break