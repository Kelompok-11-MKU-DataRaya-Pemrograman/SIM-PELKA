# SIM-PELKA

**SIM-PELKA** adalah simulasi berbasis teks yang dibuat untuk mengelola dan memantau status kapal serta aktivitas bongkar muat di area pelabuhan atau dermaga.  
Program ini dikembangkan menggunakan bahasa **Python**, dan berfokus pada implementasi konsep **Object-Oriented Programming (OOP)**.

---

## Tujuan Proyek
Proyek ini dibuat sebagai bagian dari tugas mata kuliah **MKU Data Raya dan Pemrograman** untuk mempraktikkan konsep:
- OOP (Object Oriented Programming)
- Function
- if Statement
- for / while Statement

---

## Fitur Utama
1. **Menampilkan Daftar Kapal**  
   Menampilkan informasi semua kapal yang terdaftar di pelabuhan.

2. **Fungsi Bersandar**  
   Kapal yang tiba di pelabuhan dapat bersandar dan menempati dermaga yang tersedia.

3. **Bongkar Muat Barang**  
   Kapal dapat melakukan proses bongkar muat barang di dermaga.

4. **Selesai Layanan & Berangkat**  
   Setelah proses selesai, kapal dapat meninggalkan pelabuhan dan dermaga kembali tersedia.

5. **Simulasi Aktivitas Pelabuhan**  
   Pengguna dapat mensimulasikan aktivitas pelabuhan secara interaktif melalui antarmuka berbasis teks.

6. **Penyimpanan Data ke Database (SQLite3)**  
   Setelah simulasi selesai, seluruh data kapal otomatis disimpan ke database lokal `sim_pelka.db` menggunakan SQLite3.

7. **Ekspor Data Otomatis dengan Timestamp**  
   Hasil simulasi akan diekspor otomatis ke file CSV dengan format nama:

---

## Cara Menjalankan Program
1. Pastikan sudah menginstal **Python 3.8–3.12** (direkomendasikan **Python 3.11**).
2. Clone repositori ini:
   ```bash
   git clone https://github.com/Kelompok-11-MKU-DataRaya-Pemrograman/SIM-PELKA.git
3. Jalankan program:
   ```bash
   python SIM_PELKA.py

---

## Catatan
- File `sim_pelka.db` akan otomatis dibuat di direktori kerja setelah program dijalankan.
- Setiap hasil simulasi disimpan secara unik berdasarkan timestamp agar tidak menimpa file sebelumnya.
