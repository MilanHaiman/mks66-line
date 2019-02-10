from display import *
from draw import *

screen = new_screen()
color = [ 140, 140, 140 ]

white = [255,255,255]

red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]

def dist2(x0,y0,x1,y1):
	return (x0-x1)**2.+(y0-y1)**2.

def dist(x0,y0,x1,y1):
	return dist2(x0,y0,x1,y1)**0.5

# draw_line(x,y,250,250,screen,color)

points=[[104,401],[284,381],[471,360],[34,101],[209,141],[294,160],[292,210],[243,225],[166,248]]

lines=[[0,2],[3,5],[6,8,white],[0,4,red],[4,2,green],[2,3,blue],[3,1,red],[1,5,green],[5,0,blue]]

for line in lines:
	if (len(line) > 2):
		col = line[2]
	else:
		col = color
	draw_line(points[line[0]][0],points[line[0]][1],points[line[1]][0],points[line[1]][1],screen,col)

# longlines=[[0,2],[3,5],[6,8]]

# for line in longlines:
# 	x0,y0,x1,y1=points[line[0]][0],points[line[0]][1],points[line[1]][0],points[line[1]][1]
# 	x2,y2,x3,y3=10*x0-9*x1,10*y0-9*y1,10*x1-9*x0,10*y1-9*y0
# 	draw_line(x2,y2,x3,y3,screen,color)



for i in range(9):
	col = color
	if (i>5):
		col = white
	for x in range(points[i][0]-10,points[i][0]+10):
		for y in range(points[i][1]-10,points[i][1]+10):
			if dist(points[i][0],points[i][1],x,y) <=3:
				plot(screen,col,x,y)


display(screen)
save_extension(screen, 'pappus.png')
