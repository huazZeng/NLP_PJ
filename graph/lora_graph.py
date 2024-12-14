import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# 定义一个函数来绘制对比图
def plot_comparison(data, dataset_name,filename):
    labels = list(data.keys())
    sft_values = [data[label]['SFT'] for label in labels]
    lora_values = [data[label]['LoRA'] for label in labels]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, sft_values, width, label='SFT')
    rects2 = ax.bar(x + width/2, lora_values, width, label='LoRA')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Values')
    ax.set_title(f'Comparison on {dataset_name} Dataset')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def add_labels(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    add_labels(rects1)
    add_labels(rects2)

    fig.tight_layout()

    plt.savefig(filename)

# GSM8K 数据集的数据
gsm8k_data = {
    '显存占用': {'SFT': 19.76, 'LoRA': 8.41},
    '训练时间': {'SFT': 1054.17, 'LoRA': 1403.40},
    '训练效果': {'SFT': 27.75, 'LoRA': 28.73}
}

# MATH 数据集的数据
math_data = {
    '显存占用': {'SFT': 21.60, 'LoRA': 7.90},
    '训练时间': {'SFT': 839.47, 'LoRA': 1025.39},
    '训练效果': {'SFT': 9.80, 'LoRA': 8.00}
}

# 绘制两张图
plot_comparison(gsm8k_data, 'GSM8K',"GSM8K-LORA")
plot_comparison(math_data, 'MATH',"MATH-LORA")