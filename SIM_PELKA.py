# Rizki Agustian

# SIM-PELKA: Simulasi Manajemen Pelayanan Kapal di Pelabuhan

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

# Fatiha Alyssa

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

# Radithya Alfitoba

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
                volume = int(input(f"Masukkan volume bongkar/muat untuk {kapal.nama}: "))
                kapal.bongkar_muat(volume)
                kapal.selesai_layanan()
        tampilkan_daftar_kapal(daftar_kapal)
        shift += 1

if __name__ == "__main__":
    daftar_kapal = [
        Kapal("Meratus Jaya", "Kargo", 5000),
        Kapal("Samudra Indah", "Kargo", 8000),
        Kapal("Nusantara", "Kargo", 3000)
    ]

    tampilkan_daftar_kapal(daftar_kapal)
    simulasikan_bongkar_muat(daftar_kapal)
    print("\nSimulasi selesai. Terima kasih telah menggunakan SIM-PELKA.\n")
