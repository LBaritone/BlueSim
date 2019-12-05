import numpy as np 

class Camera() :

    def __init__(self, depth, width, height) :
        self.depth = depth
        self.width = width
        self.height = height
        self.area = self.width * self.height

        self.x = 0
        self.y = 0
        self.z = 0
        self.u = 0
        self.v = 0
        self.w = 0

        self.depth = 10

    def set_camera(self, x, y, z, u, v, w) :
        self.x = x
        self.y = y
        self.z = z
        self.u = u
        self.v = v
        self.w = w

    def get_camera(self) :

        up = np.array([0, 0, 1])
        front = np.array([self.u, self.v, self.w])
        front = front / np.linalg.norm(front)

        # find unit vectors to either side
        left_unit = np.cross(up, front)
        right_unit = -left_unit

        # extend vectors to find camera centers 
        left_center = left_unit * self.depth
        right_center = right_unit * self.depth

        # left camera edge points
        w_left = front * (self.width / 2.)
        h = up * (self.height / 2.)
        left_top_right = left_center + w_left + h
        left_bot_right = left_center + w_left - h 
        left_top_left = left_center - w_left + h
        left_bot_left = left_center - w_left - h 

        # right camera edge points 
        w_right = -front * (self.width / 2.)
        right_top_right = right_center + w_right + h
        right_bot_right = right_center + w_right - h 
        right_top_left = right_center - w_right + h
        right_bot_left = right_center - w_right - h 

        return [[left_top_left, left_top_right, 
                 left_bot_left, left_bot_right],
                [right_top_left, right_top_right, 
                 right_bot_left, right_bot_right]]


    def captured_by_camera(self, tile_corners) :

        cam_corners = self.get_camera()
        center = np.array([self.x, self.y, self.z])

        top_left, top_right, bot_left, bot_right = 
            [np.array(x) for x in tile_corners]


        # intersect plane and line: 
        # http://geomalgorithms.com/a05-_intersect-1.html
        # define plane through tile via normal 
        top_vec = top_right - top_left 
        top_vec = top_vec / np.linalg.norm(top_vec)
        side_vec = bot_left - top_right 
        side_vec = side_vec /  np.linalg.norm(side_vec)

        n = np.cross(side_vec, top_vec)
        w = center - top_left 

        for cam in cam_corners :
            for ray_point in cam :
                ray = np.array(ray_point) - center
                u = ray / np.linalg.norm(ray)
                s = - np.dot(n, w) / np.dot(n, u)

                inter = w + (s * u) + top_left 

                # condition for point inside box: 4 triangles area must = 
                # area of rectangle
                top_left_pt = inter - top_left
                pt_bot_left = bot_left - inter
                bot_right_pt = inter - bot_right
                pt_top_right = top_right - inter

                tri_area = 0.5 * np.cross(top_left_pt, pt_bot_left)
                tri_area += 0.5 * np.cross(bot_right_pt, pt_top_right)
                tri_area += 0.5 * np.cross(bot_right_pt, pt_bot_left)
                tri_area += 0.5 * np.cross(top_left_pt, pt_top_right)

                if tri_area > (self.rect_area + 0.05) :
                    return False
        return True












