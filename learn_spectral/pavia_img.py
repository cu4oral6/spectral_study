import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

# 加载ROSIS高光谱数据
try:
    mat_data = loadmat('../data/Pavia.mat')  # 替换为实际文件路径
    hsi_data = mat_data['pavia']  # 假设数据存储在'rosis_image'变量中
    wavelengths = mat_data['wavelengths']  # 波长信息
except FileNotFoundError:
    print("错误：未找到ROSIS数据文件，请检查文件路径")
    exit()
except KeyError:
    print("错误：数据文件中缺少必要的变量，请确认文件格式")
    exit()

# 验证数据维度
if hsi_data.ndim != 3 or hsi_data.shape[2] != 115:
    print(f"错误：数据维度异常，应为145x145x115，实际为{hsi_data.shape}")
    exit()


# 波段选择策略：近红外(NIR)、红波段(R)、绿波段(G)
# 查找波长范围对应的波段索引
def find_band_index(wavelength_range):
    return np.argmin(np.abs(wavelengths - wavelength_range), axis=1)


# 关键波长定位
ir_band = find_band_index(700)  # 近红外波段中心
red_band = find_band_index(650)  # 红波段中心
green_band = find_band_index(550)  # 绿波段中心

# 波段有效性验证
if not all(0 <= idx < 115 for idx in [ir_band, red_band, green_band]):
    print("错误：所选波段索引超出有效范围(0-114)")
    exit()

# 波段数据提取与归一化
print(
    f"使用的波段：NIR({wavelengths[ir_band]:.1f}nm), R({wavelengths[red_band]:.1f}nm), G({wavelengths[green_band]:.1f}nm)")

rgb_bands = [
    hsi_data[:, :, ir_band],  # 红色通道
    hsi_data[:, :, green_band],  # 绿色通道
    hsi_data[:, :, red_band]  # 蓝色通道
]

# 归一化处理
rgb_normalized = np.zeros((hsi_data.shape[0], hsi_data.shape[1], 3))
for i in range(3):
    band_data = rgb_bands[i]
    band_min, band_max = np.percentile(band_data, [2, 98])  # 忽略极端值
    rgb_normalized[:, :, i] = (band_data - band_min) / (band_max - band_min) * 255

# 转换为uint8类型并保存
rgb_image = rgb_normalized.astype(np.uint8)

# 可视化与保存
plt.figure(figsize=(12, 6))
plt.imshow(rgb_image)
plt.title("ROSIS伪彩色合成图像(NIR-R-G组合)")
plt.axis('off')
plt.savefig('./rosis_pseudocolor.png', bbox_inches='tight', dpi=300)
print("伪彩色图像已保存为rosis_pseudocolor.png")