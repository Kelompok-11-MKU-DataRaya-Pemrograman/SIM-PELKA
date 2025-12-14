import csv
import random
import os

FILENAME = 'big_data_kapal.csv'
TARGET_SIZE_MB = 2.5 # Target > 2MB

# Data referensi
jenis = ['Kargo', 'Penumpang', 'Tanker', 'Tongkang', 'Ro-Ro']
status = ['Selesai', 'Bersandar', 'Antri']
names = ['Meratus', 'Samudra', 'Nusantara', 'Tanjung', 'Sinar', 'Baruna']

with open(FILENAME, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    size = 0
    # Loop terus sampai ukuran file melebihi target
    while size < (TARGET_SIZE_MB * 1024 * 1024):
        row = [
            f"{random.choice(names)} {random.randint(1,999)}", # Nama
            random.choice(jenis), # Jenis
            random.randint(3000, 20000), # Tonase
            random.choice(status), # Status
            random.randint(0, 5000) # Muatan
        ]
        writer.writerow(row)
        
        # Cek ukuran file sesekali
        if random.random() < 0.01: 
            f.flush()
            size = os.path.getsize(FILENAME)

# Hitung ukuran akhir
final_size_bytes = os.path.getsize(FILENAME)
final_size_mb = final_size_bytes / (1024 * 1024)

print(f"Selesai! {FILENAME} berhasil dibuat.")
print(f"Ukuran file akhir: {final_size_mb:.2f} MB")