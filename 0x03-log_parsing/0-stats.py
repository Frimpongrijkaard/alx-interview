#!/usr/bin/python3
"""
    This is log parsing module.
"""

import sys
import signal


status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}


total_file_size = 0
line_count = 0

def print_stats():
    """Print the accumulated statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def process_line(line):
    """Process a single line of log data."""
    global total_file_size, line_count

    try:
        
        parts = line.split()

        
        if len(parts) < 7:
            return  

    
        status_code = parts[8]
        file_size = parts[9]

        
        try:
            total_file_size += int(file_size)
        except ValueError:
            pass  

        
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

    except IndexError:
        pass  

def handle_signal(signal, frame):
    """Handle the CTRL + C signal to print stats and exit."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_signal)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            process_line(line)

            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)