# import turtle as tt
#
# a = tt.Pen()
# for x in range(100):
#     a.forward(x)
#     a.left(90)
# tt.done()


# import turtle
# import random
# 绘制八边形
# turtle.circle(50, None, 8)

# 绘制螺旋图案
# turtle.TurtleScreen._RUNNING = True
# x = 0
# turtle.bgcolor("black")
# turtle.setpos(-25, 25)
# turtle.colormode(255)
# turtle.speed(0)
# while x > -1:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     turtle.pencolor(color)
#     turtle.forward(100 + x)
#     turtle.right(91)
#     x +=1
# turtle.done()


import turtle

# 用正方形绘制圆
# turtle.speed(0)   # 设置画笔运行的速度为最快
# for i in range(360):
#     turtle.setheading(i)
#     for i in range(4):
#         turtle.forward(100)
#         turtle.left(90)
# turtle.done()



# import turtle
# import random
#
# turtle.TurtleScreen._RUNNING = True
# turtle.speed(0)
# turtle.bgcolor("black")
# turtle.setpos(-25, 25)
# turtle.colormode(255)
# x = 0
# while x < 500:
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     turtle.pencolor(color)
#     turtle.circle(1 + x/10)
#     turtle.left(0.1)
#     x += 1
# turtle.done()


# 绘制螺旋线
import turtle
import random
turtle.TurtleScreen._RUNNING = True
turtle.bgcolor("white")
turtle.speed(0)
turtle.colormode(255)
turtle.pensize(0.5)
x = 0

while x > -1:
# for x in range(360):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    turtle.pencolor(color)
    x += 1
    turtle.forward(x/3)
    turtle.left(59)
turtle.done()



