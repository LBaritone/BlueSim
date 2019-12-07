import numpy as np


center = np.array([1, 0, 1])
x_w = np.array([1, 0, 0])
y_w = np.array([0, 1, 0])
z_w = np.array([0, 0, 1])

y_c = np.array([0, 0, 1])
x_c = np.array([0, 1, 0])
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

test = np.array([1.1, 0, 1, 1]).reshape(-1, 1)

W = 1
w = np.dot(P_left, test)[-1]

depth = (w * np.sign(np.linalg.det(P_left[:, :-1]))) / (W * np.linalg.norm(P_left[-1, 0:-1]))


print(depth)