import os


# def merge_json_to_jsonl(input_dir, output_file):
#     # 打开输出文件以写入
#     with open(output_file, 'w') as jsonl_file:
#         # 遍历目录及子目录
#         for root, dirs, files in os.walk(input_dir):
#             for file in files:
#                 if file.endswith('.json'):
#                     json_file_path = os.path.join(root, file)
#                     # 读取 JSON 文件内容
#                     with open(json_file_path, 'r',encoding="utf-8") as json_file:
#                         data = json.load(json_file)
#                         # 将 JSON 对象写入到 JSONL 文件中
#                         json.dump(data, jsonl_file)
#                         jsonl_file.write('\n')

# # 示例使用
# input_directory = './MATH/MATH/train'  # 输入目录路径
# output_jsonl = 'MATH_train.jsonl'     # 输出 JSONL 文件路径
# merge_json_to_jsonl(input_directory, output_jsonl)


import json

# 读取原始数据
json_file_path = 'MATH_test.jsonl'
with open(json_file_path, 'r', encoding="utf-8") as json_file:
    data = [json.loads(line) for line in json_file]

# 将数据格式化为 JSONL 格式，每个问题和答案作为一个消息对象
output_file_path = 'MATH_train_fineture.jsonl'

prompt = '''You are a highly skilled mathematician capable of solving complex grade-school math problems step by step. Please read the problem carefully and solve it with clear reasoning. Follow these instructions:

- Identify the known information and the question being asked.
- Break the solution into logical steps, providing clear explanations for each.
- Show all calculations and intermediate results.
- Conclude with a final answer.

Output your response in the following format:
[Explanation and calculations]
#### [Final numerical answer]   

Here is the problem:
'''
with open(output_file_path, 'w', encoding="utf-8") as output_file:
    for item in data:
        message = {
            "role": "user",
            "content": prompt+ item["problem"]
        }
        assistant_message = {
            "role": "assistant",
            "content": item["solution"]
        }
        # 写入每个问题和答案对
        formatted_entry = {"messages": [message, assistant_message]}
        output_file.write(json.dumps(formatted_entry, ensure_ascii=False) + '\n')

    
                        