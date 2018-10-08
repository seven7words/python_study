f = float(input("请输入一个年份"))
is_true = f % 4 == 0 and f%100 != 0 or f % 400 == 0
print(is_true)