import tkinter
import random
import time

class Ball():
	def __init__(self, canvas, paddle, color):
		self.canvas = canvas
		self.paddle = paddle
		self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
		self.canvas.move(self.id, 100, 100)
		starts = [-3, -2, -1, 1, 1, 2, 3]
		random.shuffle(starts)
		self.x = starts[0]
		self.y = -3
		self.canvas_height = self.canvas.winfo_height()
		self.canvas_width = self.canvas.winfo_width()
		self.hit_bottom = False

	def hit_paddle(self, pos):
		paddle_pos = self.canvas.coords(self.paddle.id)
		if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
				return True
		return False

	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		
		if pos[1] <= 0:# move down
			self.y = 1 

		if pos[3] >= self.canvas_height:# move up
			self.hit_bottom = True

		if self.hit_paddle(pos) == True:
			self.y = -2

		if pos[0] <= 0:#move right
			self.x = 2
		if pos[2] >= self.canvas_width:#move left
			self.x = -2

class Paddle:
	def __init__(self, canvas, color):
		self.canvas = canvas 
		self.id=canvas.create_rectangle(0,0,150,10,fill=color)
		self.canvas.move(self.id,200,350)
		self.x=0 
		self.started=False
		self.canvas_width=self.canvas.winfo_width()
		self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
		self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
		self.canvas.bind_all('<Button-1>',self.start_game)

	def draw(self):
		self.canvas.move(self.id,self.x,0)
		pos=self.canvas.coords(self.id)
		if pos[0]<=0:#left edge
			self.x = 0 
		elif pos[2]>=self.canvas_width:#right edge
			self.x = 0 

	def turn_left(self, evt):
		pos = self.canvas.coords(self.id)
		if pos[0] <= 0:
			self.x = 0 
		else:
			self.x = -3 

	def turn_right(self, evt):
		pos = self.canvas.coords(self.id)
		if pos[2] >= self.canvas_width:
			self.x = 0 
		else:
			self.x = 3 

	def start_game(self, evt):
		self.started = True

def run():
	tk = tkinter.Tk()
	tk.title("Game")
	#通知窗口管理器调整布局大小,0,0表示不能被拉升
	tk.resizable(0, 0)
	tk.wm_attributes("-topmost", 1)
	#创建一个长为400*500的画布,背景色为默认，边框为厚度为0
	canvas = tkinter.Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
	#注册组件
	canvas.pack()
	tk.update()

	paddle = Paddle(canvas, "blue")
	ball = Ball(canvas, paddle, "red")
	while 1:
		if ball.hit_bottom == False and ball.paddle.started:
			ball.draw()
			paddle.draw() 
		tk.update_idletasks()
		tk.update()
		time.sleep(0.01)

if __name__ == '__main__':
	run()