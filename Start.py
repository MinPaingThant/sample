from turtle import *

color('blue', 'orange')
begin_fill()
while True:
	forward(200)
	left(170)
	if abs(pos()) < 6:
		break 
end_fill()
done()
