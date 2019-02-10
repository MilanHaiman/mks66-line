from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
	if x0 > x1:
		x0, x1, y0, y1=x1, x0, y1, y0
	if 0 <= y1 - y0 <= x1 - x0:
		x=x0
		y=y0
		A=y1-y0
		B=-x1+x0
		d=2*A+B
		while x<=x1:
			plot(screen,color,x,y)
			if d>0:
				y+=1
				d+=2*B
			x+=1
			d+=2*A
		return
	if 0 <= x1 - x0 <= y1 - y0:
		x=x0
		y=y0
		A=y1-y0
		B=-x1+x0
		d=A+2*B
		while y<=y1:
			plot(screen,color,x,y)
			if d<0:
				x+=1
				d+=2*A
			y+=1
			d+=2*B
		return
	if 0 <= y0 - y1 <= x1 - x0:
		y0, y1 = y1, y0
		x=x0
		y=y0
		A=y1-y0
		B=-x1+x0
		d=2*A+B
		while x<=x1:
			plot(screen,color,x,y0 + y1 - y)
			if d>0:
				y+=1
				d+=2*B
			x+=1
			d+=2*A
		return
	if 0 <= x1 - x0 <= y0 - y1:
		y0, y1 = y1, y0
		x=x0
		y=y0
		A=y1-y0
		B=-x1+x0
		d=A+2*B
		while y<=y1:
			plot(screen,color,x,y0 + y1 - y)
			if d<0:
				x+=1
				d+=2*A
			y+=1
			d+=2*B
		return

