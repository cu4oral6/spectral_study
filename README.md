## 24 周详细路线（每周待办）

### 🧩 阶段 A（Week 1–4）

**目标：掌握高光谱数据结构与基础操作**

**Week 1**

- 安装环境：`numpy, scipy, spectral, matplotlib, torch, scikit-learn`
- 下载 Indian Pines `.mat` 数据集
- 学习 `.mat` 文件结构与读取 (`scipy.io.loadmat`)
- 任务：绘制第 30、60、90 波段的灰度图
- 输出：3 张波段图 + 一张像元光谱曲线

**Week 2**

- 学习高光谱成像原理（反射率、波段、噪声）
- 对数据做归一化、坏波段剔除
- 可视化不同地物（农田、树、道路）光谱差异
- 输出：3 类地物平均光谱曲线对比图

**Week 3**

- 熟悉 Spectral Python（SPy）库：伪彩色显示、PCA 降维
- 使用 PCA 将波段降到 3 并可视化
- 输出：伪 RGB + PCA 三维散点图

**Week 4**

- 生成合成混合像素（线性组合几类地物光谱）

- 理解线性混合模型 (LMM)：

  x=Ma+nx=Ma+n

- 输出：生成的混合像素 + 对应丰度图

------

### 🧩 阶段 B（Week 5–8）

**目标：掌握几何端元提取与线性解混**

**Week 5**

- 学习 VCA 理论（端点投影几何）
- 实现 VCA 算法（可用 Laadr/VCA 库）
- 任务：在 Indian Pines 提取端元谱
- 输出：端元光谱可视化 + 顶点坐标表

**Week 6**

- 实现 FCLS（Fully Constrained Least Squares）
- 使用 VCA 提取的端元进行丰度求解
- 输出：丰度图（p 张）+ 重建误差图

**Week 7**

- 学习 N-FINDR 算法原理（体积最大化）
- 比较 N-FINDR 与 VCA 在不同端元数下的表现
- 输出：端元比较表 + RMSE/SAD 指标

**Week 8**

- 阅读综述论文（Bioucas-Dias, 2012）
- 整理笔记（线性解混的假设、局限、改进方向）
- 输出：小结报告（PPT 或 Markdown）

------

### 🧩 阶段 C（Week 9–12）

**目标：学习稀疏与优化型解混算法**

**Week 9**

- 学习稀疏解混思想（L1 正则、稀疏编码）
- 阅读 SUnSAL 论文
- 理解 ADMM 框架的解法逻辑

**Week 10**

- 实现 SUnSAL（使用 Python 版或自己写 ADMM）
- 使用 USGS 光谱库 + 真实数据实验
- 输出：SUnSAL 丰度图 + RMSE 曲线

**Week 11**

- 实现 SUnSAL-TV（空间正则）
- 对比 SUnSAL 与 SUnSAL-TV 在光滑区域的差异
- 输出：空间平滑前后效果图

**Week 12**

- 总结传统方法：VCA、N-FINDR、SUnSAL
- 输出：实验报告 + 可视化图集（端元谱 + 丰度图）

------

### 🧩 阶段 D（Week 13–16）

**目标：掌握基于深度学习的自编码解混**

**Week 13**

- 学习 Autoencoder 结构、loss 函数
- 实现简单 AE（如前文例子）
- 输出：训练曲线 + 重建光谱图

**Week 14**

- 设计“约束 AE”：
  - softmax 确保 abundance 和为 1
  - 非负约束 + 稀疏约束
- 输出：带约束 AE 的训练结果

**Week 15**

- 实现 VAE（变分自编码器）解混（可选）
- 对比 AE vs VAE 表现
- 输出：重建图 + loss 对比表

**Week 16**

- 阅读深度解混综述（例如：Deep Unmixing with Autoencoders, IEEE GRSL）
- 输出：论文笔记 + 模型架构对比图

------

### 🧩 阶段 E（Week 17–20）

**目标：深入非线性/空间-光谱联合解混**

**Week 17**

- 学习 3D-CNN、1D-CNN 在高光谱数据中的应用
- 实现简单 CNN 解混网络（1D 卷积 + softmax 输出）

**Week 18**

- 引入注意力机制（Spectral Attention Module）
- 比较 AE vs CNN-Attention 模型效果

**Week 19**

- 研究端元变异（Spectral Variability）
- 实验：为每个端元加入噪声 / 光照变化模拟

**Week 20**

- 整合：构建 Hybrid 模型（AE + CNN）
- 输出：农业场景下最优模型方案总结

------

### 🧩 阶段 F（Week 21–24）

**目标：复现论文 / 迁移大模型（HyperSIGMA）**

**Week 21**

- 学习 HyperSIGMA 的结构与 API
- 下载并试用其 `HyperspectralUnmixing` 子模块

**Week 22**

- 使用 HyperSIGMA 的预训练特征
  → 将其作为 AE 的输入层进行迁移学习
- 输出：迁移前后对比图 + 性能表

**Week 23**

- 阅读并复现一篇 2024 年后的深度解混论文（我可以帮你选）
- 输出：复现日志 + 对比报告

**Week 24**

- 整理成完整报告 / 论文草稿：
  - 实验设置
  - 方法比较
  - 可视化结果
  - 未来展望（端元变异、时序农业监测）