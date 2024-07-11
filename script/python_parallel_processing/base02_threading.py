import requests
import threading
import time

urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5'
]


def fetch_data(url):
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    start_time = time.time()
    # 为每个URL创建一个线程
    threads = [threading.Thread(target=fetch_data, args=(url,)) for url in urls]
    # 启动所有线程
    for thread in threads:
        thread.start()
    # 确保所有线程结束
    for thread in threads:
        thread.join()

    end_time = time.time()
    print("Time taken with threading:", end_time - start_time, "seconds")
