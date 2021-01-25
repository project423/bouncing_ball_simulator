from turtle import Turtle, Screen


from ball import Ball


wn = Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.setup(width=600, height=600)
wn.tracer(0)

balls = []

for _ in range(10):
    ball = Ball()
    balls.append(ball)
print(balls)


gravity = 0.001


while True:
    wn.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)
        
        #Check for a wall collision
        if ball.xcor() > 280:
            ball.reverse()
            ball.bounce_x()
            
        if ball.xcor() < -280:
            ball.reverse()
            ball.bounce_x()

        #Check for a bounce
        if ball.ycor() < -280:
            ball.sety(-280)
            ball.bounce_y()

        if ball.ycor() > 290:
            ball.sety(290)
            ball.bounce_y()
            
    # Check for collisions between the balls
    for i in range(0, len(balls)):
        for j in range(i+1, len(balls)):
            #Check for collision
            if balls[i].distance(balls[j]) < 20:
                #Switiching the direction
                balls[i].dx, balls[j].dx = balls[j].dx, balls[i].dx
                balls[i].dy, balls[j].dy = balls[j].dy, balls[i].dy
                # temp_dx = balls[i].dx
                # temp_dy = balls[i].dy

                # balls[i].dx = balls[j].dx
                # balls[i].dy = balls[j].dy

                # balls[j].dx = temp_dx
                # balls[j].dy = temp_dy



        
















wn.mainloop()