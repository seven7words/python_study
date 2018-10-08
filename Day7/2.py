def main():
    fruits = ["grape","apple","strawberry","waxberry"]
    fruits += ["pitaya","pear","mango"]
    for fruit in fruits:
        print(fruit.title(),end=" ")
    print()
    fruits2 = fruits[1:4]
    print(fruits2)
    # fruits3 = fruits 就是创建了一个新的引用
    # 可以通过完整切片操作来复制列表
    fruits3 = fruits[:]
    print(fruits3)
    fruits4 = fruits[-3:-1]
    print(fruits4)
    # 可以反向切片操作来获得倒转后的列表的拷贝
    fruits5 = fruits[::-1]
    print(fruits5)

if __name__ == '__main__':
    main()