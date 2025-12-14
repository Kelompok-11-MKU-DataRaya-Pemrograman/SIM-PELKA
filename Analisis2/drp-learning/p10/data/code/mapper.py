#!/usr/bin/env python3

import sys

# Mapper: Output key=Status, value=1 (Counter)
for line in sys.stdin:
    line = line.strip()
    if line.startswith("nama,jenis") or not line:
        continue
        
    try:
        parts = line.split(',')
        if len(parts) >= 4:
            status = parts[3].strip() # Index 3 adalah status
            print("{}\t1".format(status))
            
    except ValueError:
        continue