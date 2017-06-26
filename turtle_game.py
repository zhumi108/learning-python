import turtle

def draw_art():
	#获得一个窗口句柄
	window = turtle.Screen()
	window.bgcolor("blue")
	#点击窗口自动关闭
	
	#实例化一个turtle对象
	brad = turtle.Turtle()
	#设置形状为海龟
	brad.shape("turtle")
	brad.color("orange")
	brad.speed("fast")

	for i in range(1, 37):
		draw_diamond(brad)
		brad.right(10)

	brad.right(90)
	brad.forward(300)

	window.exitonclick()

def draw_diamond(turt):
	for i in range(1, 3):
		#向前走100步
		turt.forward(100)
		#右转45度
		turt.right(45)
		turt.forward(100)
		turt.right(135)

draw_art()