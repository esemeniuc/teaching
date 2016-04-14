fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.arange(20)
y = np.arange(20)
x2d, y2d = np.meshgrid(x, y)
kernel_2d = np.exp(-((x2d - 10) ** 2 + (y2d - 10) ** 2) / (2 * sigma ** 2))
kernel_2d = kernel_2d / np.sum(kernel_2d)
x2d, y2d, kernel_2d = x2d.ravel(), y2d.ravel(), kernel_2d.ravel()
ax.bar3d(x2d, y2d, x2d * 0, 1, 1, kernel_2d)
# <...>
