import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

# 加载.mat文件（假设结构为{'indian_pines_corrected': [145,145,200]}）
mat_data = sio.loadmat('../data/Pavia.mat')
print(mat_data.keys())  # 查看所有键
print(mat_data)
hsi_data = mat_data['pavia']  # 提取三维数组

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 检查数据维度
print(f"数据形状: {hsi_data.shape}")  # 应输出 (145, 145, 200)

# 显示第50波段（自动缩放灰度值）
band_idx = 50
plt.imshow(hsi_data[:, :, band_idx], cmap='gray')
plt.colorbar(label='反射率')
plt.title(f'Indian Pines - Band {band_idx}')
plt.show()

# 选择三个波段合成RGB（例：波段30/50/70）
rgb = np.dstack([
    hsi_data[:, :, 30],
    hsi_data[:, :, 50],
    hsi_data[:, :, 70]
])

# 归一化到0-255范围
rgb_normalized = (rgb - np.min(rgb)) / (np.max(rgb) - np.min(rgb)) * 255
plt.imshow(rgb_normalized.astype(np.uint8))
plt.title('Pseudo-RGB Image (Bands 30/50/70)')
plt.axis('off')
plt.show()
