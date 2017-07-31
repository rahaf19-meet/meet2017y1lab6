import turtle

turtle.shape('turtle')

square=turtle.clone()
square.shape('square')
square.goto(100,0)
square.stamp()
square.goto(100,100)
square.stamp()
square.goto(0,100)
square.stamp()
square.goto(0,0)
square.stamp()

triangle=turtle.clone()
triangle.shape('triangle')
triangle.penup()
triangle.goto(0,-200)
triangle.pendown()
triangle.goto(0,-100)
triangle.stamp()
triangle.goto(100,-200)
triangle.stamp()
triangle.goto(0,-200)
triangle.stamp()

turtle.penup()
turtle.goto(-100,0)
turtle.pendown()

turtle.mainloop()

