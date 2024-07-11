import requests
import concurrent.futures
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
    # Create a thread pool with a maximum of 5 threads (one for each URL)
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
        # Submit each URL fetching task to the thread pool
        futures = [executor.submit(fetch_data, url) for url in urls]
        # Wait for all futures (tasks) to complete
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    end_time = time.time()
    print("Results with thread pool:", results)
    print("Time taken with thread pool:", end_time - start_time, "seconds")
