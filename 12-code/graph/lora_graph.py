import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # Use SimHei font
plt.rcParams['axes.unicode_minus'] = False  # Correctly display minus signs

gsm8k_data = {
    'Memory Usage': {'SFT': 19.76, 'LoRA': 8.41},
    'Training Time': {'SFT': 1054.17, 'LoRA': 1403.40},
    'Training Effectiveness': {'SFT': 27.75, 'LoRA': 28.73}
}

# Data for the MATH dataset
math_data = {
    'Memory Usage': {'SFT': 21.60, 'LoRA': 7.90},
    'Training Time': {'SFT': 839.47, 'LoRA': 1025.39},
    'Training Effectiveness': {'SFT': 9.80, 'LoRA': 8.00}
}


math_data_style = {
    'Memory Usage': {'3B': 51.57, '0.5B': 19.16},
    'Training Time': {'3B': 4742.59, '0.5B': 2438.16},
    'Training Effectiveness': {'3B': 73.63, '0.5B': 42.99}
}
# Define a function to plot multiple comparison charts on one canvas
def plot_multi_comparison(data, dataset_name, filename):
    fig, axs = plt.subplots(1, len(data), figsize=(15, 5))  # Create a canvas with 3 subplots

    for idx, (metric_name, values) in enumerate(data.items()):
        labels = [metric_name]
        sft_value = values['SFT']
        lora_value = values['LoRA']

        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars

        rects1 = axs[idx].bar(x - width/2, sft_value, width, label='SFT')
        rects2 = axs[idx].bar(x + width/2, lora_value, width, label='LoRA')

        # Calculate the y-axis range
        min_value = min(sft_value, lora_value)
        max_value = max(sft_value, lora_value)
        margin = 0.3*max_value # Add 10% margin space
        axs[idx].set_ylim([0, max_value + margin])

        # Add some text for labels, title and custom x-axis tick labels, etc.
        axs[idx].set_ylabel('Values')
        axs[idx].set_title(f'{metric_name} on {dataset_name} Dataset')
        axs[idx].set_xticks(x)
        axs[idx].set_xticklabels(labels)
        axs[idx].legend()

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

# Plot three metrics of the GSM8K dataset on one canvas
plot_multi_comparison(gsm8k_data, 'GSM8K', "GSM8K-LORA.png")

# Plot three metrics of the MATH dataset on one canvas
plot_multi_comparison(math_data, 'MATH', "MATH-LORA.png")
