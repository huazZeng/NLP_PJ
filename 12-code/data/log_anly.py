import json

def parse_and_average(file_path):
    total_memory = 0.0
    total_elapsed_time = 0
    total_remaining_time = 0
    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            # 解析 JSON 数据
            data = json.loads(line)
            
            # 累加 memory
            total_memory += data.get("memory(GiB)", 0.0)
            
            # 累加时间（转为秒）
            elapsed_time = time_to_seconds(data.get("elapsed_time", "0s"))
            remaining_time = time_to_seconds(data.get("remaining_time", "0s"))
            total_elapsed_time += elapsed_time
            total_remaining_time += remaining_time

            count += 1

    # 计算平均值
    avg_memory = total_memory / count if count else 0
    avg_elapsed_time = total_elapsed_time / count if count else 0
    avg_remaining_time = total_remaining_time / count if count else 0

    # 输出结果
    print(f"\nAveraged Results:")
    print(f"- Average Memory Usage: {avg_memory:.2f} GiB")
    print(f"- Average Elapsed Time: {seconds_to_hms(avg_elapsed_time)}")
    print(f"- Average Remaining Time: {seconds_to_hms(avg_remaining_time)}")

def time_to_seconds(time_str):
    """ 将时间字符串 (如 '1h 2m 49s') 转换为秒 """
    h, m, s = 0, 0, 0
    for part in time_str.split():
        if 'h' in part:
            h = int(part.replace('h', ''))
        elif 'm' in part:
            m = int(part.replace('m', ''))
        elif 's' in part:
            s = int(part.replace('s', ''))
    return h * 3600 + m * 60 + s

def seconds_to_hms(seconds):
    """ 将秒转换为小时、分钟、秒字符串格式 """
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{int(h)}h {int(m)}m {int(s)}s"

if __name__ == "__main__":
    # 文件路径
    file_path = "data\log\math_full.jsonl"  # 替换为你的 JSONL 文件路径
    
    # 调用解析和平均函数
    parse_and_average(file_path)
