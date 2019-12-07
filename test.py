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
