import numpy

def connect_points(points, image, color):
    for i in range(0, points.shape[0]):
        base = points[i]
        for j in range(0, points.shape[0]):
            draw_line(base, points[j], image, color)
            
def draw_polygon(poly_points, image, color):
    for i in range(0, poly_points.shape[0]):
        base = poly_points[i]
        if i != poly_points.shape[0]-1:
            draw_line(base, poly_points[i+1], image, color)
        else:
            draw_line(base, poly_points[0], image, color)
        

def draw_line(point1, point2, image, color):
    sub_vec = point2-point1
    vec_mag = numpy.linalg.norm(sub_vec)
    unit_vec = sub_vec/vec_mag
    for t in range(0, int(vec_mag)):
        pixel = (point1+unit_vec*t).astype(int)
        image[int(pixel[0]), int(pixel[1])] = color
    
        
    
    