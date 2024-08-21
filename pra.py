import turtle

t=turtle.Turtle()
t.speed(0)
a=5
b=0 
while(b<a):
    
    t.color("red")
    t.forward(a)
    t.right(90)
    t.color("black")
    t.forward(a)
    t.right(90)
    
    b+=1
    a=a+5

