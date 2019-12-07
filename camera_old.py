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

    def set_camera(self, pos, vel) :
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.u = vel[0]
        self.v = vel[1]
        self.w = vel[2]

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

        top_left, top_right, bot_left, bot_right = [np.array(x) for x in tile_corners]
        tile_corners = [top_left, top_right, bot_left, bot_right]


        # intersect plane and line: 
        # http://geomalgorithms.com/a05-_intersect-1.html
        # define plane through tile via normal 
        top_vec = top_right - top_left 
        top_vec = top_vec / np.linalg.norm(top_vec)
        side_vec = bot_left - top_right 
        side_vec = side_vec /  np.linalg.norm(side_vec)

        n = np.cross(side_vec, top_vec)
        w = center - top_left 

        tile_in_cam = [True, True]
        for i in range(len(cam_corners)) :
            cam = cam_corners[i]
            # change to: find four intersections of 4 corner rays of camera on 
            # tile plane, then check to see if if all four corners of tile are 
            # within distance D to center (approximate outer image rectangle)
            # check to see if all four tile corners are contained within the outer
            # plane intersection with camera rays rectangle 

            inters_tile_plane = []
            for ray_point in cam :
                ray = np.array(ray_point) - center
                u = ray / np.linalg.norm(ray)
                s = - np.dot(n, w) / np.dot(n, u)

                inter = w + (s * u) + top_left 
                inters_tile_plane.append(inter)

            inter_top_l_top_r = inters_tile_plane[1] - inters_tile_plane[0]
            inter_top_l_bot_l = inters_tile_plane[2] - inters_tile_plane[0]
            inter_rect_area = np.linalg.norm(np.cross(inter_top_l_bot_l, 
                                                      inter_top_l_top_r))

            for tile_pt in tile_corners :
                # condition for point inside box: 4 triangles area must = 
                # area of rectangle
                top_left_pt = tile_pt - inters_tile_plane[0]
                pt_bot_left = inters_tile_plane[2] - tile_pt
                bot_right_pt = tile_pt - inters_tile_plane[3]
                pt_top_right = inters_tile_plane[1] - tile_pt

                tri_area = 0.5 * np.linalg.norm(np.cross(top_left_pt, pt_bot_left))
                tri_area += 0.5 * np.linalg.norm(np.cross(bot_right_pt, pt_top_right))
                tri_area += 0.5 * np.linalg.norm(np.cross(bot_right_pt, pt_bot_left))
                tri_area += 0.5 * np.linalg.norm(np.cross(top_left_pt, pt_top_right))

                if tri_area > (inter_rect_area + 0.05) and (
                    np.linalg.norm(tile_pt) >= self.depth) :
                    tile_in_cam[i] = False

        return tile_in_cam[0] or tile_in_cam[1]












