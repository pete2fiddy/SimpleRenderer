from Render.Camera import Camera
import numpy
from math import pi
from PIL import Image
from time import sleep
from Geometry.Rectangle import Rectangle
import Graphics.LineDrawer as LineDrawer
import Matrix.MatrixMath as MatrixMath


box_size = 15
z_box_away = 20

left_camera_spins = numpy.array([0.0,0.0,0.0])
right_camera_spins = numpy.array([0.0,0.0,0.0])

camera = Camera(numpy.array([-0.5,0.0,0.0]), left_camera_spins)


box_polypoints = numpy.array([[[-(box_size//2),z_box_away,-(box_size//2)],
                         [-(box_size//2),z_box_away,(box_size//2)],
                         [(box_size//2),z_box_away,(box_size//2)],
                         [(box_size//2),z_box_away,-(box_size//2)]],
                         [[-(box_size//2),z_box_away + box_size,-(box_size//2)],
                         [-(box_size//2),z_box_away + box_size,(box_size//2)],
                         [(box_size//2),z_box_away + box_size,(box_size//2)],
                         [(box_size//2),z_box_away + box_size,-(box_size//2)]]])

sides = [0 for j in range(0, 4)]
for i in range(0, len(sides)):
    if i != 3:
        p1 = box_polypoints[0,i]
        p2 = box_polypoints[1,i]
        p3 = box_polypoints[1,i+1]
        p4 = box_polypoints[0,i+1]
        append_side = numpy.array([p1,p2,p3,p4])
        sides[i]=append_side
    else:
        p1 = box_polypoints[0,i]
        p2 = box_polypoints[1,i]
        p3 = box_polypoints[1,0]
        p4 = box_polypoints[0,0]
        append_side = numpy.array([p1,p2,p3,p4])
        sides[i]=append_side
        
print("sides: ", sides)
box_polypoints = box_polypoints.tolist()#numpy.array(box_polypoints.tolist().extend(sides))
for i in range(0, len(sides)):
    box_polypoints.append(sides[i])
box_polypoints = numpy.asarray(box_polypoints)
print("box polypoints: ", box_polypoints)


poly_projections = numpy.zeros((box_polypoints.shape[0], box_polypoints.shape[1], 2))




box_rotation = numpy.array([pi/2.5, pi/4.0, pi/3.0])

for i in range(0, box_polypoints.shape[0]):
    box_polypoints[i] = MatrixMath.apply_rotation(box_polypoints[i], box_rotation, numpy.array([0, z_box_away + (box_size//2), 0]))


dim = numpy.array([800,800])




for i in range(0, poly_projections.shape[0]):
    
    poly_projections[i] = camera.create_projection(box_polypoints[i], dim)






img = Image.new('L', (dim[0], dim[1]))
image = img.load()

for i in range(0, poly_projections.shape[0]):
    LineDrawer.draw_polygon(poly_projections[i], image, 255)

img.show()
