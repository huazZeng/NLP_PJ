import time
import gc

def big_number_loop_test(iterations=10_000_000, enable_gc=True):
    # 如果启用了垃圾回收，就先运行一次gc.collect()确保环境干净
    if enable_gc:
        gc.collect()

    # 记录开始时间
    start_time = time.perf_counter()

    # 关闭垃圾回收
    if not enable_gc:
        gc.disable()

    # 大数循环
    big_number = 0
    for i in range(iterations):
        big_number += 1 # 这里用一个相对较大的数

    # 恢复垃圾回收
    if not enable_gc:
        gc.enable()
        gc.collect()

    # 记录结束时间
    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    print(f"完成 {iterations} 次循环，耗时: {elapsed_time:.6f} 秒")
    return elapsed_time

# 测试性能
if __name__ == "__main__":
    iterations = 10_000_00000  # 可以调整这个值来改变循环次数
    test_with_gc = True  # 设置为False来禁用垃圾回收器
    big_number_loop_test(iterations, test_with_gc)