#!/usr/bin/python3
"""modsd"""

import sys


def print_statistics(total_file_size, status_code_counts):
    """klfs"""
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts):
        print("{}: {}".format(status_code, status_code_counts[status_code]))


def main():
    """main"""
    total_file_size = 0
    status_code_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            try:
                parts = line.split()
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_file_size += file_size
                status_code_counts[status_code] = status_code_counts.get(
                    status_code, 0) + 1

                if i % 10 == 0:
                    print_statistics(total_file_size, status_code_counts)
            except (ValueError, IndexError):
                continue
    except KeyboardInterrupt:
        pass  # Continue processing with the accumulated statistics

    print_statistics(total_file_size, status_code_counts)


if __name__ == "__main__":
    main()
