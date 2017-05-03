from Render.Camera import Camera
import numpy
from math import pi
from PIL import Image
from Graphics.graphics import *
from time import sleep

camera = Camera(numpy.array([0.0,0.0,0.0]), numpy.array([0.0,0.0,0.0]))

td_points = numpy.array([[-1,5,-1],
                         [-1,5,1],
                         [1,5,1],
                         [1,5,-1]])


dim = numpy.array([200,200])
print("projections: ", camera.create_projection(td_points, dim))
projections = camera.create_projection(td_points, dim)

win = GraphWin("My Circle", dim[0], dim[1])


circles = []
for i in range(0, projections.shape[0]):
    pix = projections[i].astype(int)# dim * projections[i]
    c = Circle(Point(pix[0], pix[1]), 5)
    circles.append(c)
    
for i in range(0, len(circles)):
    circles[i].draw(win)
    
while(True):
    key = win.checkKey()
    rot_vec = numpy.zeros((3))
    '''if key == "a" or key == "q":
        rot_vec += numpy.array([.1,0,0])
    elif key == "w" or key == "s":
        rot_vec += numpy.array([0,.1,0])
    elif key == "e" or key == "d":
        rot_vec += numpy.array([0,0,.1])'''
    if key == "a":
        rot_vec += numpy.array([0,.1,0])
    elif key == "d":
        rot_vec += numpy.array([0,-.1,0])
    elif key == "w":
        rot_vec += numpy.array([0, 0,-.1])
    elif key == "s":
        rot_vec += numpy.array([0,0,.1])
        
    
    camera.add_spins(rot_vec)
    projections = camera.create_projection(td_points, dim)
    for i in range(0, len(circles)):
        #circles[i].undraw()
        pix = projections[i].astype(int)# dim * projections[i]
        #c = Circle(Point(pix[0], pix[1]), 5)
        #circles[i]=c
        circles[i].move(pix[0]-circles[i].getCenter().getX(), pix[1]-circles[i].getCenter().getY())
        #c.draw(win)
        
    sleep(0.001)
    
    
win.getMouse() # pause for click in window
win.close()

