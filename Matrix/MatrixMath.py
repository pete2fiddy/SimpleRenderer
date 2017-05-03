import numpy
from math import sin, cos


'''
rotations order:

about x, 
about y, 
about z
'''
def apply_rotation(points, rotations, rotation_point):
    out_points = numpy.zeros(points.shape)
    rot_matrices = numpy.zeros((3, 3, 3), dtype = float)
    rot_matrices[0] = numpy.array([[1,0,0], 
                                  [0, cos(rotations[0] ), -sin(rotations[0] )],
                                  [0, sin(rotations[0] ), cos(rotations[0] )]])
    
    rot_matrices[1] = numpy.array([[cos(rotations[1]), 0, sin(rotations[1])],
                                   [0, 1, 0],
                                   [-sin(rotations[1]), 0, cos(rotations[1])]])
    
    rot_matrices[2] = numpy.array([[cos(rotations[2]), -sin(rotations[2]), 0],
                                   [sin(rotations[2]), cos(rotations[2]), 0],
                                   [0,0,1]])
        
    mat_product = numpy.dot(numpy.dot(rot_matrices[0], rot_matrices[1]), rot_matrices[2])
    for i in range(0, out_points.shape[0]):
        out_points[i] = numpy.dot((points[i]-rotation_point), mat_product)
    return out_points + rotation_point