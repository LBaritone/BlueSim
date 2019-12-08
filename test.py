from pprint import pprint
import numpy as np 

arena_size = np.array([1780, 1780, 1170])


res = 10
x_vals = np.linspace(0, arena_size[0], res)
y_vals = np.linspace(0, arena_size[1], res)
z_vals = np.linspace(0, arena_size[2], res)
zero = np.zeros((res, res))
x_end = np.full((res, res), arena_size[0])
y_end = np.full((res, res), arena_size[1])

zz, xz = np.meshgrid(z_vals, x_vals)
_, yz = np.meshgrid(z_vals, y_vals)

xz_zz_y_0 = np.array([xz, zero, zz])
xz_by_zz_y_0 = xz_zz_y_0.transpose()
xz_zz_y_end = np.array([xz, y_end, zz])
xz_by_zz_y_end = xz_zz_y_end.transpose()

yz_zz_x_0 = np.array([zero, yz, zz])
yz_by_zz_x_0 = yz_zz_x_0.transpose()
yz_zz_x_end = np.array([x_end, yz, zz])
yz_by_zz_x_end = yz_zz_x_end.transpose()

walls = [xz_by_zz_y_0, xz_by_zz_y_end, yz_by_zz_x_0, yz_by_zz_x_end]

pprint(walls)

tiles = []
for wall in walls :
	for i in range(res - 1) :
		for j in range(res - 1) :
			four = [wall[i, j], wall[i, j + 1], wall[i + 1, j], wall[i + 1, j + 1]]
			tiles.append(four)

print(len(tiles))
# pprint(xz_by_zz_y_0)
# pprint(xz_by_zz_y_0.shape)
# pprint(np.insert(xz_by_zz, 2, y_end, axis=0))


        # if self.behavior == 'expand':
        #     # find closest wall 
        #     diff_x_0 = loc[0]
        #     diff_x_end = arena_size[0] - loc[0]
        #     diff_y_0 = loc[1]
        #     diff_y_end = arena_size[1] - loc[1]
        #     walls = np.array([diff_x_0, diff_x_end, diff_y_0, diff_y_end])
        #     closest = np.argmin(walls)
        #     self.cur_wall = closest

        #     if walls[closest] < 15 :
        #         self.behavior = "turn"
        #     else:
        #         if closest == 0 :
        #             self.target_pos = np.array([0, loc[1], loc[2]])
        #         elif closest == 1 :
        #             self.target_pos = np.array([arena_size[0], loc[1], loc[2]])
        #         elif closest == 2 :
        #             self.target_pos = np.array([loc[0], 0, loc[2]])
        #         else :
        #             self.target_pos = np.array([loc[0], arena_size[1], loc[2]])

        #         move = self.target_pos# + centroid_pos
        #         # Global to Robot Transformation
        #         r_T_g = self.interaction.rot_global_to_robot(self.id)
        #         r_move_g = r_T_g @ move
        #         # Simulate dynamics and restrict movement #xx
        #         self.home(r_move_g)
        #         self.caudal = 1