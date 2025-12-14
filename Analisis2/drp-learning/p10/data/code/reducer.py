#!/usr/bin/env python3

import sys

current_status = None
current_count = 0
status = None

# Reducer: Menjumlahkan count (1) berdasarkan key (status)
for line in sys.stdin:
    line = line.strip()
    
    try:
        status, count = line.split('\t', 1)
        count = int(count)
    except ValueError:
        continue

    if current_status == status:
        current_count += count
    else:
        if current_status:
            print("{}\t{}".format(current_status, current_count))
        
        current_status = status
        current_count = count

if current_status == status:
    print("{}\t{}".format(current_status, current_count))