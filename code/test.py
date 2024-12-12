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

import re
import json
import random
# 读取原始数据
json_file_path = './AugMATH_part1/AugMATH_part1.jsonl'
with open(json_file_path, 'r', encoding="utf-8") as json_file:
    data = [json.loads(line) for line in json_file]
json_file_path = '.\AugMATH_part2\AugMATH_part2.jsonl'
with open(json_file_path, 'r', encoding="utf-8") as json_file:
    data.extend([json.loads(line) for line in json_file]) 
# 将数据格式化为 JSONL 格式，每个问题和答案作为一个消息对象
output_file_path = 'math_argu.jsonl'

prompt = '''You are a highly skilled mathematician capable of solving complex  math problems step by step. Please read the problem carefully and solve it with clear reasoning. Follow these instructions:

- Identify the known information and the question being asked.
- Break the solution into logical steps, providing clear explanations for each.
- Show all calculations and intermediate results.
- Conclude with a final answer.

Output your response in the following format:
[Explanation and calculations]
#### $[Final numerical answer]$ 

Here is the problem:
'''

count = 0 
matchcount = 0
with open(output_file_path, 'w', encoding="utf-8") as output_file:
    for item in data:
        # 随机抽取，10%的概率
        if random.random() < 0.12:  # 生成一个 0 到 1 之间的浮动数，如果小于 0.1，则抽取
            
           
            ANS_RE = re.compile(r"The answer is: \$(\-?[0-9\.,]+)\$")

            def remove_matched_content(text):
                # 使用 re.sub 将匹配的内容替换为空字符串
                return ANS_RE.sub("", text)
            match = ANS_RE.search(item["response"]) 
            item["response"] = remove_matched_content(item["response"])
            
            if match :
                matchcount += 1 
                match_str = match.group(1).strip()
                match_str = match_str.replace(",", "")
                count += 1 
                message = {
                    "role": "user",
                    "content": prompt + item["query"]
                }
                assistant_message = {
                    "role": "assistant",
                    "content": item["response"]+"\n"+"#### "+match_str
                }
                # 写入每个问题和答案对
                formatted_entry = {"messages": [message, assistant_message]}
                output_file.write(json.dumps(formatted_entry, ensure_ascii=False) + '\n')

     