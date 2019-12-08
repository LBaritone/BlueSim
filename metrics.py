import numpy as np
import matplotlib.pyplot as plt

data = np.array([[[14., 15., 16.,  9.,  4.,  8.,  9., 18., 23., 14.],
        [13., 14., 15.,  9.,  3.,  8., 11., 18., 22., 13.],
        [15., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [16., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [16., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [15., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [16., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [16., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [16., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.],
        [16., 12., 15.,  9.,  3.,  8., 11., 18., 22., 14.]],

       [[ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.],
        [ 8., 23., 25., 11.,  7.,  7.,  9., 23., 19., 24.]],

       [[16., 15., 23., 15.,  4.,  5.,  7.,  6.,  3.,  8.],
        [16., 15., 23., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [16., 15., 23., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [16., 14., 23., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [16., 14., 23., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [15., 13., 23., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [15., 12., 23., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [15., 12., 22., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [15., 12., 22., 16.,  3.,  5.,  7.,  6.,  3.,  8.],
        [15., 12., 22., 16.,  3.,  5.,  7.,  6.,  3.,  8.]],

       [[13., 12., 21.,  9.,  9., 12., 16., 24., 19., 24.],
        [13., 12., 22.,  9.,  9., 12., 16., 24., 19., 24.],
        [13., 12., 22.,  9.,  9., 12., 16., 24., 19., 24.],
        [13., 12., 23.,  9.,  9., 12., 16., 24., 19., 24.],
        [13., 12., 23.,  9.,  9., 12., 15., 23., 18., 23.],
        [13., 12., 23.,  9.,  9., 14., 16., 24., 19., 24.],
        [13., 12., 23., 10.,  9., 15., 16., 24., 19., 24.],
        [14., 12., 23., 10.,  8., 14., 16., 24., 19., 24.],
        [13., 12., 23., 10.,  8., 14., 16., 24., 19., 24.],
        [14., 12., 23., 10.,  8., 14., 16., 25., 19., 25.]]])

coverage = 0 
overlap = []
hist = []
col_sums = []

n = np.prod(data.shape)
walls, height, width = data.shape
for i in range(walls) :
	for j in range(height) :
		for k in range(width) :
			hist.append(data[i][j][k])
			if data[i][j][k] > 2 :
				coverage += 1
				overlap.append(data[i][j][k])

order = [0, 3, 1, 2]
for i in order :
	for j in range(width) :
		col_sums.append(np.average(data[i, :, j]))

print("coverage: ", coverage / float(n))
print("overlap: ", np.average(overlap))
# print(col_sums)
plt.plot(col_sums)
plt.savefig('data/coord_2_cov.png')
# plt.show()

plt.hist(col_sums, bins="auto")
plt.savefig('data/coord_2_hist.png')
# plt.show()


