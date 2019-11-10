from fifo import Fifo
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py cache_size")
        exit(1)

    with open("file.txt") as file_:
        abs = Fifo(int(sys.argv[-1]))
        for line in file_:
            normalized_line = [x.strip() for x in line.split(",")]
            for item in normalized_line:
                abs.process(item)
                print(abs)