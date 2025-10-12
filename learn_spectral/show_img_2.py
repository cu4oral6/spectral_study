import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

mat_data = sio.loadmat('../data/jasper.mat')
nRow = int(mat_data['nRow'][0][0])
nCol = int(mat_data['nCol'][0][0])
Y = mat_data['Y']  # (198, 10000)

# 转置并重塑为三维数组
hsi_data = Y.T.reshape((nRow, nCol, -1))  # -1自动推断波段数198

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 对单波段使用感知均匀的色图
plt.imshow(hsi_data[:, :, 50], cmap='viridis')  # 比'jet'更科学的色图
plt.colorbar()
plt.title('Viridis Colormap')
plt.show()

# 选择三个波段合成RGB（如第10/50/100波段）
rgb = np.dstack([
    hsi_data[:, :, 41],
    hsi_data[:, :, 27],
    hsi_data[:, :, 6]
])

# 归一化到0-255
rgb_normalized = (rgb - np.min(rgb)) / (np.max(rgb) - np.min(rgb)) * 255

plt.imshow(rgb_normalized.astype(np.uint8))
plt.title('伪彩色图像 (Bands 10/50/100)')
plt.axis('off')
plt.show()