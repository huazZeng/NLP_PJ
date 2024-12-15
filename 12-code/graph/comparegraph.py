import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 准备数据
x_labels = ['没有增强训练', '增强训练']
accuracy_05 = [27.75,42.99]  # 示例准确率，替换为实际数据
accuracy_3 = [ 63.23, 73.62]  # 示例准确率，替换为实际数据

# 创建图表
plt.figure(figsize=(8, 6))

# 绘制折线并在图例中添加标签 '3b' 和 '0.5b'
plt.plot(x_labels, accuracy_05, marker='o', label='3b')
plt.plot(x_labels, accuracy_3, marker='s', label='0.5b')

# 添加标题和坐标轴标签
plt.title('效果提升折线图') 
plt.xlabel('训练方式')
plt.ylabel('准确率')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图表
plt.savefig('compare_graph.png')
