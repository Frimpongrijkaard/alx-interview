#!/usr/bin/python3
""" This is Log parsing module 
"""
import sys
import signal

# Dictionary to store the count of status codes
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

# Variable to store the total file size
total_file_size = 0
line_count = 0

def print_stats():
    """Print the statistics gathered so far."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))

def process_line(line):
    """Process a single line of log data."""
    global total_file_size, line_count

    try:
        # Split the line based on expected format
        parts = line.split()
        if len(parts) < 7:
            return  # Skip if the format is incorrect

        # Extract relevant parts of the log
        ip_address = parts[0]
        date = parts[3][1:]
        method = parts[5][1:]
        path = parts[6]
        status_code = parts[8]
        file_size = parts[9]

        # Ensure the method and path match the expected format
        if method != "GET" or path != "/projects/260":
            return

        # Add file size to total, if it is an integer
        try:
            total_file_size += int(file_size)
        except ValueError:
            pass

        # Increment the corresponding status code count if valid
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

    except IndexError:
        pass  # Skip lines that don't match the expected format

def handle_signal(signal, frame):
    """Handle the CTRL + C signal to print stats and exit."""
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, handle_signal)

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            process_line(line)

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats()

    except KeyboardInterrupt:
        print_stats()
        sys.exit(0)