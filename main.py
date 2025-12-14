# SIM-PELKA: Simulasi Manajemen Pelayanan Kapal di Pelabuhan
# Kontributor: Rizki Agustian, Fatiha Alyssa, Radithya Alfitoba

import csv
from datetime import datetime
import sqlite3

class Kapal:
    def __init__(self, nama, jenis, tonase):
        self.nama = nama
        self.jenis = jenis
        self.tonase = tonase
        self.status = "Antri"
        self.muatan = 0

    def bersandar(self):
        if self.status == "Antri":
            self.status = "Bersandar"
            print(f"{self.nama} telah bersandar di dermaga.")
        else:
            print(f"{self.nama} tidak dapat bersandar. Status saat ini: {self.status}")

    def bongkar_muat(self, volume):
        if self.status == "Bersandar":
            if self.muatan + volume > self.tonase:
                volume = self.tonase - self.muatan
            self.muatan += volume
            print(f"{self.nama} melakukan bongkar/muat sebanyak {volume} ton.")
        else:
            print(f"{self.nama} tidak dapat bongkar/muat. Status saat ini: {self.status}")

    def selesai_layanan(self):
        if self.status == "Bersandar":
            self.status = "Selesai"
            print(f"{self.nama} selesai layanan dan siap berangkat.\n")
        else:
            print(f"{self.nama} tidak dapat menyelesaikan layanan. Status saat ini: {self.status}")


def import_data_csv(nama_file):
    try:
        with open(nama_file, mode='r', newline='', encoding='utf-8') as file:
            dialect = csv.Sniffer().sniff(file.read(1024))
            file.seek(0)
            reader = csv.DictReader(file, dialect=dialect)
            data = []
            for row in reader:
                kapal = Kapal(row['nama'], row['jenis'], int(row['tonase']))
                data.append(kapal)
            return data
    except FileNotFoundError:
        print(f"File {nama_file} tidak ditemukan.")
        return []


def export_data_csv(nama_file, daftar_kapal):
    with open(nama_file, mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['nama', 'jenis', 'tonase', 'status', 'muatan']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for kapal in daftar_kapal:
            writer.writerow({
                'nama': kapal.nama,
                'jenis': kapal.jenis,
                'tonase': kapal.tonase,
                'status': kapal.status,
                'muatan': kapal.muatan
            })
    print(f"Data hasil simulasi telah diekspor ke '{nama_file}'.")


def tampilkan_daftar_kapal(daftar_kapal):
    print("\nDaftar Kapal di Pelabuhan:")
    for i, kapal in enumerate(daftar_kapal, 1):
        print(f"{i}. {kapal.nama} | Jenis: {kapal.jenis} | Tonase: {kapal.tonase} ton | "
              f"Status: {kapal.status} | Muatan: {kapal.muatan} ton")


def simulasikan_bongkar_muat(daftar_kapal):
    shift = 1
    while shift <= 2:
        print(f"\n--- Shift {shift} ---")
        for kapal in daftar_kapal:
            if kapal.status == "Antri":
                kapal.bersandar()
            elif kapal.status == "Bersandar":
                try:
                    volume = int(input(f"Masukkan volume bongkar/muat untuk {kapal.nama}: "))
                    kapal.bongkar_muat(volume)
                    kapal.selesai_layanan()
                except ValueError:
                    print("Input tidak valid, gunakan angka.")
        tampilkan_daftar_kapal(daftar_kapal)
        shift += 1

def setup_database():
    conn = sqlite3.connect('sim_pelka.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kapal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            jenis TEXT,
            tonase INTEGER,
            status TEXT,
            muatan INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    print("Database 'sim_pelka.db' siap digunakan.")

def simpan_ke_database(daftar_kapal):
    conn = sqlite3.connect('sim_pelka.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM kapal")

    for kapal in daftar_kapal:
        cursor.execute('''
            INSERT INTO kapal (nama, jenis, tonase, status, muatan)
            VALUES (?, ?, ?, ?, ?)
        ''', (kapal.nama, kapal.jenis, kapal.tonase, kapal.status, kapal.muatan))

    conn.commit()
    conn.close()
    print("Data berhasil disimpan ke database 'sim_pelka.db'.")


if __name__ == "__main__":
    print("=== SIM-PELKA: Simulasi Manajemen Pelayanan Kapal ===")

    setup_database()

    nama_file_input = input("Masukkan nama file CSV input (misal: kapal_data.csv): ")

    daftar_kapal = import_data_csv(nama_file_input)

    if not daftar_kapal:
        print("Menggunakan data default karena file CSV kosong atau tidak ditemukan.\n")
        daftar_kapal = [
            Kapal("Meratus Jaya", "Kargo", 5000),
            Kapal("Samudra Indah", "Kargo", 8000),
            Kapal("Nusantara", "Kargo", 3000)
        ]

    tampilkan_daftar_kapal(daftar_kapal)

    simulasikan_bongkar_muat(daftar_kapal)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nama_file_output = f"hasil_simulasi_{timestamp}.csv"

    export_data_csv(nama_file_output, daftar_kapal)

    simpan_ke_database(daftar_kapal)

    print("\nSimulasi selesai. Terima kasih telah menggunakan SIM-PELKA.\n")
