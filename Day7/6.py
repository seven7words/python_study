def main():
    # 定义元祖
    t = ("seven",23,True,"重庆")
    print(t)
    #获取元祖中的元素
    print(t[0])
    print(t[3])
    #遍历元祖
    for member in t:
        print(member)
    #重新给元祖赋值
    #变量t重新引用了额新的元祖，原来的元祖 将被垃圾回收
    t = ("王大锤",20,True,"云南昆明")
    print(t)
    person = list(t)
    print(person)
    #列表可以修改它的元素
    person[0] = "李小龙"
    person[1] = 25
    print(person)
    #将列表转换成元祖
    fruits_list = ["apple","banana","orange"]
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)

if __name__ == '__main__':
    main()