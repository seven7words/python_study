from math import sqrt
end = int(input("请随便输入一个数 : "))
# end = int(sqrt(f))
# print(end)
is_can = True
for x in range(2,end+1):
    if end % x == 0 :
        is_can = False
        break
if is_can and end != 1:
    print("f是素数")
else:
    print('f不是素数')
