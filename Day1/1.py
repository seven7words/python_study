from turtle import *

def nose(x,y):
    penup()
    goto(x,y)
    pendown()
    setheading(-30)
    begin_fill()
    a = 0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a = a + 0.08
            left(3)
            forward(a)
        else:
            left(3)
            forward(a)
    end_fill()

    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()
    pencolor(255/255, 155/255, 192/255)  # 画笔颜色
    setheading(10)
    begin_fill()
    circle(5)
    colormode(255)
    color(160, 82, 45)  # 返回或设置pencolor和fillcolor
    end_fill()

    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()

def main():
    # setting()           #画布、画笔设置
    nose(-100,100)      #鼻子
    # head(-69,167)       #头
    # ears(0,160)         #耳朵
    # eyes(0,140)         #眼睛
    # cheek(80,10)        #腮
    # mouth(-20,30)       #嘴
    done()

if __name__ == '__main__':
	main()
