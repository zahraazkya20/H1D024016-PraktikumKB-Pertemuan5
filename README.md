# Sistem Pakar Diagnosa Penyakit THT

Program sistem pakar berbasis Python GUI yang mampu mendiagnosa penyakit di bidang **Telinga, Hidung, dan Tenggorokan (THT)** berdasarkan gejala yang dimasukkan oleh pengguna, dilengkapi dengan saran penanganan singkat untuk setiap penyakit yang terdeteksi.

---

## Fitur Program

- Mendeteksi **23 jenis penyakit THT** sesuai data modul praktikum
- **37 pertanyaan gejala** interaktif dengan jawaban YA/TIDAK
- **Progress bar** yang menunjukkan posisi pertanyaan saat ini
- Kode gejala ditampilkan di setiap pertanyaan (G1–G37)
- Output menampilkan **nama penyakit** dan **saran penanganan singkat**
- Antarmuka grafis (GUI) menggunakan Tkinter
- Opsi untuk mengulang diagnosa setelah selesai

---

## Daftar Penyakit yang Dapat Dideteksi

| No | Penyakit | Gejala Utama |
|----|----------|--------------|
| 1 | Tonsilitis | Demam, sakit kepala, nyeri menelan, batuk, nyeri tenggorokan |
| 2 | Sinusitis Maksilaris | Demam, sakit kepala, batuk, hidung tersumbat, hidung meler |
| 3 | Sinusitis Frontalis | Demam, sakit kepala, hidung tersumbat, dahi sakit |
| 4 | Sinusitis Etmoidalis | Demam, hidung tersumbat, nyeri antara mata, nyeri pinggir hidung |
| 5 | Sinusitis Sfenoidalis | Demam, hidung tersumbat, batuk, nyeri leher |
| 6 | Abses Peritonsiler | Demam, suara serak, air liur menetes, getah bening |
| 7 | Faringitis | Demam, nyeri menelan, nyeri tenggorokan, nyeri leher |
| 8 | Kanker Laring | Suara serak, nafas abnormal, berat badan turun |
| 9 | Deviasi Septum | Hidung tersumbat, pendarahan hidung, infeksi sinus |
| 10 | Laringitis | Demam, leher bengkak, tenggorokan gatal |
| 11 | Kanker Leher & Kepala | Benjolan leher, tumbuh di mulut, perubahan suara |
| 12 | Otitis Media Akut | Demam, nyeri telinga, mual, radang gendang telinga |
| 13 | Contact Ulcers | Nyeri menelan, suara serak |
| 14 | Abses Parafaringeal | Nyeri menelan, leher bengkak |
| 15 | Barotitis Media | Sakit kepala, nyeri telinga |
| 16 | Kanker Nasofaring | Hidung tersumbat, pendarahan hidung |
| 17 | Kanker Tonsil | Nyeri tenggorokan, benjolan di leher |
| 18 | Neuronitis Vestibularis | Mual muntah, bola mata bergerak tidak normal |
| 19 | Meniere | Nyeri telinga, mual, serangan vertigo, telinga penuh |
| 20 | Tumor Saraf Pendengaran | Sakit kepala, tuli, tubuh tidak seimbang |
| 21 | Kanker Leher Metastatik | Benjolan di leher |
| 22 | Otosklerosis | Tuli, telinga berdenging |
| 23 | Vertigo Postural | Bola mata bergerak tidak normal |

---

## Cara Menjalankan

**Requirement:**
- Python 3.x
- Tkinter (sudah built-in pada Python, tidak perlu instalasi tambahan)

**Jalankan program:**
```bash
python tugas_pert5.py
```

---

## Cara Penggunaan

1. Jalankan program, jendela aplikasi akan terbuka
2. Klik tombol **Mulai Diagnosa** untuk memulai sesi pemeriksaan
3. Baca setiap pertanyaan gejala dengan seksama
4. Jawab dengan menekan tombol **YA** (hijau) atau **TIDAK** (merah)
5. Ikuti progress bar hingga semua pertanyaan selesai
6. Hasil diagnosa beserta saran penanganan akan muncul dalam popup
7. Klik **Mulai Diagnosa** kembali jika ingin mengulang pemeriksaan

> ⚠️ **Perhatian:** Hasil diagnosa dari program ini bersifat informatif dan tidak menggantikan pemeriksaan langsung oleh dokter spesialis THT.
