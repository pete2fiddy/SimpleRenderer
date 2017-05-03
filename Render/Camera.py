from math import pi, cos, sin
import numpy
import Matrix.MatrixMath as MatrixMath

class Camera(object):
    '''camera spin order goes:
    about x
    about y
    about z
    '''
    def __init__(self, pos, camera_spins, view_angles = (pi/6.0, pi/6.0)):
        self.pos = pos
        self.camera_spins = camera_spins
        self.update_basis_vectors()
        self.view_angles = view_angles

    def update_basis_vectors(self):
        
        basis_vectors = numpy.array([[1.0,0.0,0.0],
                                    [0.0,1.0,0.0],
                                    [0.0,0.0,1.0]])
        
        rotated_basis_vectors = MatrixMath.apply_rotation(basis_vectors, self.camera_spins, self.pos)
        
        self.right_vec = rotated_basis_vectors[0]
        self.depth_vec = rotated_basis_vectors[1]
        self.up_vec = rotated_basis_vectors[2]
    
    def create_projection(self, td_points, screen_dim):
        points = numpy.zeros((td_points.shape[0], 2))
        for i in range(0, points.shape[0]):
            rel_vector = td_points[i] - self.pos
            points[i] = self.get_projection_position_of_rel_vector(rel_vector, screen_dim)
        return points    
    
    def get_projection_position_of_rel_vector(self, vector, screen_dim):
        z_depth = self.get_z_depth_of_rel_vector(vector)
        slice_dim = self.get_slice_dim_at_depth(z_depth)
        i_projection = numpy.dot(vector, self.right_vec)
        j_projection = numpy.dot(vector, self.up_vec)
        i_percent = (i_projection+(slice_dim[0]/2))/slice_dim[0]
        j_percent = (j_projection+(slice_dim[1]/2))/slice_dim[1]
        return numpy.array([i_percent*screen_dim[0], j_percent*screen_dim[1]])

    
    def get_z_depth_of_rel_vector(self, vector):
        return numpy.dot(self.depth_vec, vector)
    
    def add_spins(self, rot_vec):
        self.camera_spins += rot_vec
        self.update_basis_vectors()
        
    def get_slice_dim_at_depth(self, z_depth):
        return (2*cos(self.view_angles[0])*z_depth, 2*cos(self.view_angles[1])*z_depth)