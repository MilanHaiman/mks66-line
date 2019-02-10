from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

r=200.
a = [250+ r,250]
b = [250+r*-0.5,250+r*(3**(0.5))/2]
c = [250+r*-0.5,250-1*r*(3**(0.5))/2]
# print(a)
# print(b)
# print(c)

def dist2(x0,y0,x1,y1):
	return (x0-x1)**2.+(y0-y1)**2.

def dist(x0,y0,x1,y1):
	return dist2(x0,y0,x1,y1)**0.5

for x in range(500):
	for y in range(500):
		if -2*r<dist2(x,y,250,250)-(r**2)<2*r:
			color[0]=int(240*(dist(x,y,a[0],a[1])/(2*r)))
			color[1]=int(240*(dist(x,y,b[0],b[1])/(2*r)))
			color[2]=int(240*(dist(x,y,c[0],c[1])/(2*r)))
			# print(color)
			# color=[240*dist2(x,y,a[0],a[1])/(4*r*r), 240*dist2(x,y,b[0],b[1])/(4*r*r), 240*dist2(x,y,c[0],c[1])/(4*r*r)]
			draw_line(x,y,250,250,screen,color)

display(screen)
save_extension(screen, 'img.png')
