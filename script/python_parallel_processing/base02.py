import requests
import time

# 免费可用于测试的API
# https://jsonplaceholder.typicode.com/
# Free fake and reliable API for testing and prototyping.
urls = [
    'https://jsonplaceholder.typicode.com/posts/1',
    'https://jsonplaceholder.typicode.com/posts/2',
    'https://jsonplaceholder.typicode.com/posts/3',
    'https://jsonplaceholder.typicode.com/posts/4',
    'https://jsonplaceholder.typicode.com/posts/5'
]


# IO密集型任务，例如网络请求
def fetch_data(url):
    response = requests.get(url)
    return response.json()


if __name__ == '__main__':
    start_time = time.time()
    results = [fetch_data(url) for url in urls]
    end_time = time.time()

    print("Results:", results)
    print("Time Cost:", end_time - start_time, "seconds")
