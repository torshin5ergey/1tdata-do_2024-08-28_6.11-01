import os
import sys
from datetime import datetime
import heapq  # min-heap data structure

#PATH = '/home/sandbox-admin/docker_python_app'

def greetings(name):
    """Greet user.
    """
    print(f"Hello, {name}!")

def print_current_datetime():
    """Print current date and time
    """
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def count_files(path):
    """
    """
    count_files = 0
    for _, _, filenames in os.walk(path):
        count_files += len(filenames)
    return count_files

def find_top10_largest_files(path):
    top10heap = []
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            filepath = os.path.join(dirpath, file)
            try:
                filesize = os.path.getsize(filepath)
                if len(top10heap) < 10:
                    heapq.heappush(top10heap, (filepath, filesize))
                else:
                    heapq.heappushpop(top10heap, (filepath, filesize))
            except FileNotFoundError:
                continue
            except OSError:
                continue

    top10heap.sort(reverse=True, key=lambda x: x[1])
    return top10heap

if __name__ == "__main__":
    # 1
    try:
        name = sys.argv[1]
    except IndexError:
        name = 'User'
    greetings(name)
    print_current_datetime()

    # 2
    try:
        path_for_processing = PATH
    except NameError:
        path_for_processing = '/'
    total_files = count_files(path_for_processing)
    print(f"Total number of files: {total_files}")

    # 3
    largest_files = find_top10_largest_files(path_for_processing)
    # Row length for justified output
    print_len_file = max((len(f) for f, _ in largest_files), default=0)
    print_len_size = max((len(f"{round(s/1024, 2)}") for _, s in largest_files), default=0)
    print("Top 10 largest files (in KB):")
    for file, size in largest_files:
        print(f"{(file).ljust(print_len_file)} ", end='')
        print(f"{str(round(size/1024, 2)).rjust(print_len_size)} KB")

