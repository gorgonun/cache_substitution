from fifo import Fifo
from aleatory import Aleatory
from lfu import Lfu
from lru import Lru
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 main.py algorithm cache_size")
        exit(1)

    with open("file.txt") as file_:
        if sys.argv[1] == "fifo":
            func = Fifo(int(sys.argv[-1]))
        elif sys.argv[1] == "aleatory":
            func = Aleatory(int(sys.argv[-1]))
        elif sys.argv[1] == "lfu":
            func = Lfu(int(sys.argv[-1]))
        elif sys.argv[1] == "lru":
            func = Lru(int(sys.argv[-1]))
        for line in file_:
            normalized_line = [x.strip() for x in line.split(",")]
            for item in normalized_line:
                func.process(item)
                print(func)
