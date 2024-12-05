import os
import json

def merge_json_to_jsonl(input_dir, output_file):
    # 打开输出文件以写入
    with open(output_file, 'w') as jsonl_file:
        # 遍历目录及子目录
        for root, dirs, files in os.walk(input_dir):
            for file in files:
                if file.endswith('.json'):
                    json_file_path = os.path.join(root, file)
                    # 读取 JSON 文件内容
                    with open(json_file_path, 'r',encoding="utf-8") as json_file:
                        data = json.load(json_file)
                        # 将 JSON 对象写入到 JSONL 文件中
                        json.dump(data, jsonl_file)
                        jsonl_file.write('\n')

# 示例使用
input_directory = './MATH/MATH/train'  # 输入目录路径
output_jsonl = 'MATH_train.jsonl'     # 输出 JSONL 文件路径
merge_json_to_jsonl(input_directory, output_jsonl)
