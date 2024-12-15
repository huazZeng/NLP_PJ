import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 数据准备
math_data_style = {
    'Memory Usage': {'3B': 51.57, '0.5B': 19.16},
    'Training Time': {'3B': 4742.59, '0.5B': 2438.16},
    'Training Effectiveness': {'3B': 73.63, '0.5B': 42.99}
}

def plot_multi_comparison(data, dataset_name, filename):
    fig, axs = plt.subplots(1, len(data), figsize=(15, 5))  # Create a canvas with 3 subplots

    for idx, (metric_name, values) in enumerate(data.items()):
        
        labels = [metric_name]
        sft_value = values['3B']
        lora_value = values['0.5B']

        x = np.arange(len(labels))  # the label locations
        width = 0.15 # the width of the bars
        rects1 = axs[idx].bar(x - width/2, sft_value, width, label='3B')
        rects2 = axs[idx].bar(x + width/2, lora_value, width, label='0.5B')
        
        
        # Calculate the y-axis range
        min_value = min(sft_value, lora_value)
        max_value = max(sft_value, lora_value)
        margin = (max_value - min_value) * 0.1  # Add 10% margin space
        axs[idx].set_ylim([min_value - margin, max_value + margin])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        axs[idx].set_ylabel('Values')
        axs[idx].set_title(f'{metric_name} on {dataset_name} Dataset')
        axs[idx].set_xticks(x)
        axs[idx].set_xticklabels(labels)

        def add_labels(rects, ax):
            """Attach a text label above each bar in *rects*, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate(f'{height}',
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')

        add_labels(rects1, axs[idx])
        add_labels(rects2, axs[idx])

    plt.tight_layout()

    plt.savefig(filename)
    plt.close(fig)  # Close the figure to free memory


# 绘制三个指标在同一画布上
plot_multi_comparison(math_data_style, 'Model Comparison', "scaling_graph.png")