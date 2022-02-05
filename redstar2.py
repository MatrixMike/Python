from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    # thonny gives warning for next line : abs : why?
    if abs(pos()) < 1:
        break
end_fill()
done()
