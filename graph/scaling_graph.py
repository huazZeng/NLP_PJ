import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# 数据准备
labels = ['准确度 (%)', '训练时间 (s)', '显存占用 (GB)']
model_3B = [27.75, 1054.17, 16]  # 假设的3B模型数据
model_0_5B = [25.55, 1393.15, 8]  # 假设的0.5B模型数据

x = np.arange(len(labels))  # 标签位置
width = 0.35  # 条形宽度

fig, ax = plt.subplots(figsize=(10, 6))

# 绘制条形图
rects1 = ax.bar(x - width/2, model_3B, width, label='3B')
rects2 = ax.bar(x + width/2, model_0_5B, width, label='0.5B')

# 添加一些文本以描述图表内容
ax.set_xlabel('性能指标')
ax.set_ylabel('值')
ax.set_title('不同模型大小的性能对比')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

# 自动标签条形数值
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

# plt.show()
plt.savefig('scaling_graph.png')