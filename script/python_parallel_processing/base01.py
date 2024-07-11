import time


# CPU密集型任务，例如计算斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    numbers = [30, 31, 32, 33]
    # 统计耗时
    start_time = time.time()
    results_single = [fibonacci(num) for num in numbers]
    end_time = time.time()

    print("Results:", results_single)
    print("Time Cost:", end_time - start_time, "seconds")
