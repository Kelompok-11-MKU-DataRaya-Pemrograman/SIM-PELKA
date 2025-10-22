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

