#!/usr/bin/env python3

import sys

current_jenis = None
current_tonase = 0
jenis = None

# Reducer: Menjumlahkan tonase berdasarkan key (jenis)
for line in sys.stdin:
    line = line.strip()
    
    try:
        jenis, tonase = line.split('\t', 1)
        tonase = int(tonase)
    except ValueError:
        continue

    if current_jenis == jenis:
        current_tonase += tonase
    else:
        if current_jenis:
            print("{}\t{}".format(current_jenis, current_tonase))
        current_jenis = jenis
        current_tonase = tonase

if current_jenis == jenis:
    
    print("{}\t{}".format(current_jenis, current_tonase))