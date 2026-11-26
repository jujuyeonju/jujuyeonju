import turtle

screen = turtle.Screen()
screen.setup(600, 650)
screen.bgcolor("#F0F8FF")
screen.title("Luffy - Python Turtle")

t = turtle.Turtle()
t.speed(0)
t.pensize(3)


def move(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()
  t.setheading(0)


def draw_circle(x, y, r, fill_color="", line_color="black"):
  move(x, y - r)
  t.pencolor(line_color)
  if fill_color:
    t.fillcolor(fill_color)
    t.begin_fill()
  t.circle(r)
  if fill_color:
    t.end_fill()


# 1. 빨간 조끼 몸통
move(-72, -100)
t.fillcolor("#E63946")
t.begin_fill()
t.goto(72, -100)
t.goto(82, -210)
t.goto(-82, -210)
t.goto(-72, -100)
t.end_fill()

# 가슴 X자 흉터
t.pensize(4)
move(-18, -135)
t.goto(18, -175)
move(18, -135)
t.goto(-18, -175)
t.pensize(3)

# 2. 귀 & 왼쪽 귀걸이
draw_circle(-92, -15, 16, fill_color="#FFDAB9")
draw_circle(92, -15, 16, fill_color="#FFDAB9")

# 3. 얼굴 (살구색)
draw_circle(0, -10, 88, fill_color="#FFDAB9")

# 4. 눈 & 눈썹
draw_circle(-34, -2, 10, fill_color="white")
draw_circle(34, -2, 10, fill_color="white")
draw_circle(-34, -2, 4.5, fill_color="black")
draw_circle(34, -2, 4.5, fill_color="black")

t.pensize(4)
move(-48, 17)
t.goto(-22, 14)
move(22, 14)
t.goto(48, 17)
t.pensize(3)

# 5. 왼쪽 눈 밑 +자 흉터
move(-34, -18)
t.goto(-34, -30)
move(-40, -24)
t.goto(-28, -24)

# 6. 코 & 웃는 입
move(0, -4)
t.goto(-5, -17)
t.goto(4, -19)

move(-38, -38)
t.fillcolor("#FF6B6B")
t.begin_fill()
t.setheading(-60)
t.circle(44, 120)
t.goto(-38, -38)
t.end_fill()

# 7. 앞머리 (모자 챙 밑에서 내려오게 수정)
move(-78, 36)
t.fillcolor("#1C1C1C")
t.begin_fill()
t.goto(78, 36)
t.goto(65, 22)
t.goto(45, 34)
t.goto(22, 20)
t.goto(0, 35)
t.goto(-22, 20)
t.goto(-45, 34)
t.goto(-65, 22)
t.goto(-78, 36)
t.end_fill()

# 8. 밀짚모자 챙
move(-135, 45)
t.fillcolor("#F4C430")
t.begin_fill()
t.goto(135, 45)
t.goto(115, 36)
t.goto(-115, 36)
t.goto(-135, 45)
t.end_fill()

# 9. 밀짚모자 윗부분
move(-74, 45)
t.fillcolor("#F4C430")
t.begin_fill()
t.setheading(80)
t.circle(-75, 160)
t.goto(-74, 45)
t.end_fill()

# 10. 빨간 리본
move(-76, 45)
t.fillcolor("#E63946")
t.begin_fill()
t.goto(76, 45)
t.goto(74, 58)
t.goto(-74, 58)
t.goto(-76, 45)
t.end_fill()

t.hideturtle()
screen.mainloop()