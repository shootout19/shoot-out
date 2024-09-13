import requests
import argparse
import threading
from queue import Queue

# Define the worker function for threading
def worker(url_queue, wordlist, results):
    while not url_queue.empty():
        url = url_queue.get()
        for word in wordlist:
            target_url = f"{url}/{word}"
            try:
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    print(f"Found: {target_url}")
                    results.append(target_url)
            except requests.RequestException:
                pass
        url_queue.task_done()

def main(target_url, wordlist_file, threads):
    # Read wordlist from file
    with open(wordlist_file, 'r') as f:
        wordlist = [line.strip() for line in f if line.strip()]

    # Create a queue for URLs to be tested
    url_queue = Queue()
    url_queue.put(target_url)
    
    # List to store results
    results = []

    # Create and start threads
    thread_list = []
    for _ in range(threads):
        thread = threading.Thread(target=worker, args=(url_queue, wordlist, results))
        thread_list.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

    # Output results
    print("\nBrute-forcing completed.")
    if results:
        print("\nFound directories/files:")
        for result in results:
            print(result)
    else:
        print("No directories/files found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Directory brute-forcing script using requests.")
    parser.add_argument("-u", "--url", required=True, help="The base URL to brute-force.")
    parser.add_argument("-w", "--wordlist", required=True, help="File containing list of directories/files to test.")
    parser.add_argument("-t", "--threads", type=int, default=10, help="Number of concurrent threads (default: 10).")
    
    args = parser.parse_args()
    
    main(args.url, args.wordlist, args.threads)
