import multiprocessing
import time


# CPU密集型任务，例如计算斐波那契数列
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # 创建一个进程池，这里使用默认的CPU核心数
    pool = multiprocessing.Pool()
    numbers = [30, 31, 32, 33]
    start_time = time.time()
    # 使用进程池并行计算每个数的斐波那契数
    results = pool.map(fibonacci, numbers)
    end_time = time.time()

    # 关闭进程池
    pool.close()
    pool.join()

    # 打印结果和耗时
    print("Results:", results)
    print("Time Cost with multiprocessing:", end_time - start_time, "seconds")
