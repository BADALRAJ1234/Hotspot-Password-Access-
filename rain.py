import turtle, time
sc = turtle.Screen()
pen = turtle.Turtle()

def semi_circle(col, rad, val):
   pen.color(col)
   pen.circle(rad, -180)
   pen.up()
   pen.setpos(val,0)
   pen.down()
   pen.right(180)
col = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
sc.setup(1000,700)
sc.bgcolor('white')
pen.right(500)
pen.width(300)
pen.speed(200)
for i in range(7):
    semi_circle(col[i],12*(i+8),-10*(i+1))
