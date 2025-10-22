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
