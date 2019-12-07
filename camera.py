import numpy as np 

class Camera() :

    def __init__(self, depth, f1, f2) :

        self.x = 0
        self.y = 0
        self.z = 0
        self.u = 0
        self.v = 0
        self.w = 0

        self.K = np.eye(3, 3)
        self.K[0, 0] = f1
        self.K[1, 1] = f2

        self.depth = depth

    def set_camera(self, pos, vel) :
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        self.u = vel[0]
        self.v = vel[1]
        self.w = vel[2]

    def get_camera(self) :

        center = np.array([self.x, self.y, self.z])
        x_w = np.array([1, 0, 0])
        y_w = np.array([0, 1, 0])
        z_w = np.array([0, 0, 1])

        y_c = np.array([0, 0, 1])
        x_c = np.array([self.u, self.v, self.w])
        x_c_left = x_c / np.linalg.norm(x_c)
        x_c_right = - x_c_left

        # find unit vectors to either side
        z_c_left = np.cross(y_c, x_c_left)
        z_c_right = -z_c_left

        R_left = np.array([[np.dot(x_w, x_c_left), np.dot(y_w, x_c_left), np.dot(z_w, x_c_left)],
                           [np.dot(x_w, y_c), np.dot(y_w, y_c), np.dot(z_w, y_c)],
                           [np.dot(x_w, z_c_left), np.dot(y_w, z_c_left), np.dot(z_w, z_c_left)]])

        R_right = np.array([[np.dot(x_w, x_c_right), np.dot(y_w, x_c_right), np.dot(z_w, x_c_right)],
                           [np.dot(x_w, y_c), np.dot(y_w, y_c), np.dot(z_w, y_c)],
                           [np.dot(x_w, z_c_right), np.dot(y_w, z_c_right), np.dot(z_w, z_c_right)]])

        t_left = - np.dot(R_left, center)
        t_right = - np.dot(R_right, center)

        P_left = np.concatenate([R_left, t_left.reshape(-1, 1)], axis=1)
        P_right = np.concatenate([R_right, t_right.reshape(-1, 1)], axis=1)

        P_left = np.dot(self.K, P_left)
        P_right = np.dot(self.K, P_right)

        return [P_left, P_right]


    def captured_by_camera(self, pt) :

        P_left, P_right = self.get_camera()

        contained = False
        test = np.append(pt, 1).reshape(-1, 1)
        W = test[-1]
        w_left = np.dot(P_left, test)[-1]
        w_right = np.dot(P_right, test)[-1]

        depth_left = (w_left * np.sign(np.linalg.det(P_left[:, :-1]))) / (W * np.linalg.norm(P_left[-1, 0:-1]))
        depth_right = (w_right * np.sign(np.linalg.det(P_right[:, :-1]))) / (W * np.linalg.norm(P_right[-1, 0:-1]))

        depth_left = depth_left[0]
        depth_right = depth_right[0]

        if ((depth_left > 0 and depth_left < self.depth) or 
            (depth_right > 0 and depth_right < self.depth)) :
            contained = True

        return contained












