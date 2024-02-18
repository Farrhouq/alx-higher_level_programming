#!/usr/bin/python3

import sys


def read_stdin_and_print():
    count = 0
    status_code_dict = {code: 0 for code in [200, 301, 400, 401,
                                             403, 404, 405, 500]}
    total_size = 0
    try:
        for line in sys.stdin:
            count += 1
            status_code = line.split()[-2]
            file_size = line.split()[-1]
            status_code_dict[int(status_code)] += 1
            total_size += int(file_size)

            if not count % 10:
                print("File size:", total_size)
                for key, value in status_code_dict.items():
                    if value:
                        print(f"{key}: {value}")

    except KeyboardInterrupt:
        print("File size:", total_size)
        for key, value in status_code_dict.items():
            if value:
                print(f"{key}: {value}")


if __name__ == "__main__":
    read_stdin_and_print()
