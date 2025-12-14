#!/usr/bin/env python3

import sys

# Mapper: Membaca baris CSV, output key=Jenis, value=Tonase
for line in sys.stdin:
    line = line.strip()
    # Lewati header
    if line.startswith("nama,jenis") or not line:
        continue
        
    try:
        # Parsing CSV manual (split by comma)
        parts = line.split(',')
        
        if len(parts) >= 3:
            jenis = parts[1].strip()
            tonase = parts[2].strip()
            
            # Validasi angka
            if tonase.isdigit():
                print("{}\t{}".format(jenis, tonase))
    except ValueError:
        continue