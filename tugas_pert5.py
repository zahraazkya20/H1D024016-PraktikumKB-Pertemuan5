import tkinter as tk
from tkinter import messagebox

# SISTEM PAKAR DIAGNOSA PENYAKIT THT

# KNOWLEDGE BASE
knowledge_base = {
    "Tonsilitis": {
        "gejala": ["G37", "G12", "G5", "G27", "G6", "G21"],
        "solusi": "Istirahat yang cukup, minum air hangat, berkumur air garam. Konsultasikan ke dokter THT untuk penanganan antibiotik jika diperlukan."
    },
    "Sinusitis Maksilaris": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29"],
        "solusi": "Gunakan pelega hidung (dekongestan) dan kompres hangat pada wajah. Segera periksakan ke dokter untuk mendapatkan terapi antibiotik yang tepat."
    },
    "Sinusitis Frontalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G26"],
        "solusi": "Istirahat, kompres hangat pada dahi, dan gunakan obat dekongestan. Konsultasikan ke dokter THT untuk evaluasi lebih lanjut."
    },
    "Sinusitis Etmoidalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G21", "G30", "G13", "G26"],
        "solusi": "Hindari alergen, gunakan pelega hidung, dan kompres hangat. Diperlukan pemeriksaan CT-scan sinus dan penanganan dokter spesialis THT."
    },
    "Sinusitis Sfenoidalis": {
        "gejala": ["G37", "G12", "G27", "G17", "G33", "G36", "G29", "G7"],
        "solusi": "Segera periksakan ke dokter THT karena sinusitis sfenoidalis dapat menimbulkan komplikasi serius. Terapi antibiotik diperlukan."
    },
    "Abses Peritonsiler": {
        "gejala": ["G37", "G12", "G6", "G15", "G2", "G29", "G10"],
        "solusi": "Segera ke IGD atau dokter THT. Abses peritonsiler biasanya memerlukan insisi dan drainase serta terapi antibiotik intravena."
    },
    "Faringitis": {
        "gejala": ["G37", "G5", "G6", "G7", "G15"],
        "solusi": "Istirahat, minum air hangat, konsumsi obat pereda nyeri tenggorokan. Periksakan ke dokter untuk memastikan penyebab (virus/bakteri)."
    },
    "Kanker Laring": {
        "gejala": ["G5", "G27", "G6", "G15", "G2", "G19", "G1"],
        "solusi": "Segera rujuk ke dokter spesialis onkologi THT. Diperlukan pemeriksaan laringoskopi, biopsi, dan penanganan lanjutan (operasi/radioterapi)."
    },
    "Deviasi Septum": {
        "gejala": ["G37", "G17", "G20", "G8", "G18", "G25"],
        "solusi": "Konsultasikan ke dokter THT. Penanganan bisa berupa obat-obatan untuk gejala atau prosedur septoplasti jika deviasi cukup parah."
    },
    "Laringitis": {
        "gejala": ["G37", "G5", "G15", "G16", "G32"],
        "solusi": "Istirahatkan suara, hindari berbisik berlebihan, minum air hangat, dan gunakan pelembap udara. Biasanya sembuh sendiri dalam 1-2 minggu."
    },
    "Kanker Leher & Kepala": {
        "gejala": ["G5", "G22", "G8", "G28", "G3", "G11"],
        "solusi": "Segera periksakan ke dokter spesialis onkologi. Diperlukan biopsi dan pemeriksaan pencitraan untuk diagnosis dan penentuan stadium."
    },
    "Otitis Media Akut": {
        "gejala": ["G37", "G20", "G35", "G31"],
        "solusi": "Konsultasikan ke dokter THT. Terapi antibiotik mungkin diperlukan. Hindari memasukkan benda ke telinga dan jaga telinga tetap kering."
    },
    "Contact Ulcers": {
        "gejala": ["G5", "G2"],
        "solusi": "Istirahatkan suara dan hindari makanan asam/pedas. Konsultasikan ke dokter THT untuk terapi suara dan penanganan refluks jika ada."
    },
    "Abses Parafaringeal": {
        "gejala": ["G5", "G16"],
        "solusi": "Segera ke dokter THT atau IGD. Abses parafaringeal adalah kondisi darurat yang memerlukan drainase bedah dan antibiotik intravena."
    },
    "Barotitis Media": {
        "gejala": ["G12", "G20"],
        "solusi": "Coba manuver Valsalva (tutup hidung, tiup perlahan). Konsumsi dekongestan dan konsultasikan ke dokter THT jika gejala berlanjut."
    },
    "Kanker Nasofaring": {
        "gejala": ["G17", "G8"],
        "solusi": "Segera periksakan ke dokter spesialis THT dan onkologi. Diperlukan nasofaringoskopi dan biopsi untuk konfirmasi diagnosis."
    },
    "Kanker Tonsil": {
        "gejala": ["G6", "G29"],
        "solusi": "Segera konsultasikan ke dokter spesialis THT-onkologi. Diperlukan pemeriksaan endoskopi dan biopsi untuk diagnosis pasti."
    },
    "Neuronitis Vestibularis": {
        "gejala": ["G35", "G24"],
        "solusi": "Istirahat total di tempat tidur pada fase akut. Konsumsi obat anti-vertigo dan antiemetik. Konsultasikan ke dokter THT atau neurologi."
    },
    "Meniere": {
        "gejala": ["G20", "G35", "G14", "G4"],
        "solusi": "Hindari garam berlebih, kafein, dan alkohol. Konsumsi obat anti-vertigo sesuai resep dokter. Diperlukan penanganan jangka panjang oleh dokter THT."
    },
    "Tumor Saraf Pendengaran": {
        "gejala": ["G12", "G34", "G23"],
        "solusi": "Segera rujuk ke dokter THT dan neurologi. Diperlukan MRI kepala dan audiometri untuk evaluasi. Penanganan bisa berupa observasi, radioterapi, atau operasi."
    },
    "Kanker Leher Metastatik": {
        "gejala": ["G29"],
        "solusi": "Segera rujuk ke dokter spesialis onkologi. Diperlukan pemeriksaan menyeluruh untuk menemukan sumber primer dan menentukan strategi terapi."
    },
    "Otosklerosis": {
        "gejala": ["G34", "G9"],
        "solusi": "Konsultasikan ke dokter THT. Dapat ditangani dengan alat bantu dengar atau prosedur stapedektomi tergantung tingkat keparahan."
    },
    "Vertigo Postural": {
        "gejala": ["G24"],
        "solusi": "Lakukan manuver Epley atau Semont di bawah pengawasan fisioterapis/dokter. Hindari gerakan kepala tiba-tiba. Biasanya membaik dengan latihan rehabilitasi."
    },
}

# DAFTAR KODE GEJALA DAN DESKRIPSINYA
deskripsi_gejala = {
    "G1":  "Nafas abnormal",
    "G2":  "Suara serak",
    "G3":  "Perubahan kulit",
    "G4":  "Telinga terasa penuh",
    "G5":  "Nyeri saat bicara atau menelan",
    "G6":  "Nyeri tenggorokan",
    "G7":  "Nyeri leher",
    "G8":  "Pendarahan hidung",
    "G9":  "Telinga berdenging (tinnitus)",
    "G10": "Air liur menetes",
    "G11": "Perubahan suara",
    "G12": "Sakit kepala",
    "G13": "Nyeri di pinggir hidung",
    "G14": "Serangan vertigo",
    "G15": "Getah bening membengkak",
    "G16": "Leher bengkak",
    "G17": "Hidung tersumbat",
    "G18": "Infeksi sinus",
    "G19": "Berat badan turun drastis",
    "G20": "Nyeri telinga",
    "G21": "Selaput lendir tampak merah",
    "G22": "Benjolan di leher",
    "G23": "Tubuh tidak seimbang",
    "G24": "Bola mata bergerak tidak normal (nistagmus)",
    "G25": "Nyeri wajah",
    "G26": "Dahi sakit",
    "G27": "Batuk",
    "G28": "Tumbuh / benjolan di mulut",
    "G29": "Benjolan di leher",
    "G30": "Nyeri di antara mata",
    "G31": "Radang gendang telinga",
    "G32": "Tenggorokan gatal",
    "G33": "Hidung meler",
    "G34": "Tuli / pendengaran menurun",
    "G35": "Mual dan muntah",
    "G36": "Letih dan lesu",
    "G37": "Demam",
}

# Kumpulkan semua kode gejala unik yang ada di knowledge base (urut)
semua_kode = sorted(set(
    g for data in knowledge_base.values() for g in data["gejala"]
), key=lambda x: int(x[1:]))

# Susun list of tuples (kode, teks_pertanyaan)
semua_gejala = [(k, f"Apakah Anda mengalami {deskripsi_gejala[k].lower()}?") for k in semua_kode]

# KELAS APLIKASI GUI
class AplikasiPakarTHT:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Penyakit THT")
        self.root.geometry("560x340")
        self.root.resizable(False, False)
        self.root.configure(bg="#F0F4F8")

        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        # HEADER
        frame_header = tk.Frame(self.root, bg="#1F3864", pady=12)
        frame_header.pack(fill="x")

        tk.Label(
            frame_header,
            text="Sistem Pakar Diagnosa Penyakit THT",
            font=("Arial", 13, "bold"), fg="white", bg="#1F3864"
        ).pack()

        tk.Label(
            frame_header,
            text="Telinga · Hidung · Tenggorokan",
            font=("Arial", 9), fg="#A8C4E0", bg="#1F3864"
        ).pack()

        # AREA PERTANYAAN
        self.frame_konten = tk.Frame(self.root, bg="#F0F4F8", padx=20, pady=14)
        self.frame_konten.pack(fill="both", expand=True)

        self.label_nomor = tk.Label(
            self.frame_konten, text="",
            font=("Arial", 9), fg="#888888", bg="#F0F4F8", anchor="w"
        )
        self.label_nomor.pack(fill="x")

        # Frame pertanyaan dengan border
        self.frame_tanya = tk.Frame(self.frame_konten, bg="white",
                                    relief="flat", bd=0, pady=10, padx=14)
        self.frame_tanya.pack(fill="x", pady=(4, 0))
        self.frame_tanya.configure(highlightbackground="#CBD5E0",
                                   highlightthickness=1)

        self.label_tanya = tk.Label(
            self.frame_tanya,
            text="Klik 'Mulai Diagnosa' untuk memulai pemeriksaan.",
            font=("Arial", 11), bg="white", wraplength=500,
            justify="left", anchor="w", fg="#2D3748"
        )
        self.label_tanya.pack(fill="x")

        # Progress bar
        self.label_progress = tk.Label(
            self.frame_konten, text="",
            font=("Courier New", 9), fg="#4A5568", bg="#F0F4F8"
        )
        self.label_progress.pack(anchor="w", pady=(6, 0))

        # FRAME TOMBOL YA / TIDAK (disembunyikan di awal)
        self.frame_jawaban = tk.Frame(self.frame_konten, bg="#F0F4F8")

        self.btn_ya = tk.Button(
            self.frame_jawaban, text="✔  YA", width=12,
            bg="#276749", fg="white", font=("Arial", 10, "bold"),
            relief="flat", cursor="hand2",
            command=lambda: self.jawab('y')
        )
        self.btn_tidak = tk.Button(
            self.frame_jawaban, text="✘  TIDAK", width=12,
            bg="#9B2335", fg="white", font=("Arial", 10, "bold"),
            relief="flat", cursor="hand2",
            command=lambda: self.jawab('t')
        )
        self.btn_ya.pack(side=tk.LEFT, padx=(0, 10))
        self.btn_tidak.pack(side=tk.LEFT)

        # TOMBOL MULAI
        self.btn_mulai = tk.Button(
            self.frame_konten, text="Mulai Diagnosa",
            bg="#2B6CB0", fg="white", font=("Arial", 10, "bold"),
            relief="flat", cursor="hand2", pady=6,
            command=self.mulai_tanya
        )
        self.btn_mulai.pack(pady=(12, 0))

    # MULAI SESI BARU
    def mulai_tanya(self):
        # Reset working memory
        self.gejala_terpilih = []
        self.index_pertanyaan = 0

        self.btn_mulai.pack_forget()
        self.frame_jawaban.pack(pady=(10, 0))
        self.tampilkan_pertanyaan()

    # TAMPILKAN PERTANYAAN SAAT INI
    def tampilkan_pertanyaan(self):
        if self.index_pertanyaan < len(semua_gejala):
            kode, teks = semua_gejala[self.index_pertanyaan]
            total = len(semua_gejala)
            no    = self.index_pertanyaan + 1

            self.label_nomor.config(
                text=f"Pertanyaan {no} dari {total}  [{kode}]"
            )
            self.label_tanya.config(text=teks)
            isi   = "█" * no + "░" * (total - no)
            self.label_progress.config(
                text=f"Progress: {isi}  ({no}/{total})"
            )
        else:
            # Semua pertanyaan selesai → jalankan mesin inferensi
            self.proses_hasil()

    # CATAT JAWABAN PENGGUNA
    def jawab(self, respon):
        # Jika ya, tambahkan kode gejala ke working memory (seperti assertz di Prolog)
        if respon == 'y':
            kode = semua_gejala[self.index_pertanyaan][0]
            self.gejala_terpilih.append(kode)

        self.index_pertanyaan += 1
        self.tampilkan_pertanyaan()

    # MESIN INFERENSI
    def proses_hasil(self):
        hasil = []
        for penyakit, data in knowledge_base.items():
            syarat = data["gejala"]
            # Penyakit terdeteksi jika SEMUA gejala syarat ada di working memory
            if all(s in self.gejala_terpilih for s in syarat):
                hasil.append((penyakit, data["solusi"]))

        # Susun pesan output 
        if hasil:
            pesan = f"Terdeteksi {len(hasil)} kemungkinan diagnosa:\n\n"
            for i, (penyakit, solusi) in enumerate(hasil, 1):
                pesan += f"{i}. {penyakit}\n"
                pesan += f"   Saran: {solusi}\n\n"
            pesan += "⚠ Hasil ini bersifat informatif. Konsultasikan ke dokter THT."
        else:
            pesan = (
                "Tidak terdeteksi penyakit THT yang spesifik.\n\n"
                "Kemungkinan gejala yang Anda alami tidak mencukupi\n"
                "untuk mencocokkan pola penyakit dalam database.\n\n"
                "Disarankan untuk tetap berkonsultasi ke dokter THT\n"
                "jika keluhan terus berlanjut."
            )

        messagebox.showinfo("Hasil Diagnosa Penyakit THT", pesan)

        # Reset tampilan 
        self.frame_jawaban.pack_forget()
        self.label_nomor.config(text="")
        self.label_progress.config(text="")
        self.label_tanya.config(
            text="Diagnosa selesai. Klik 'Mulai Diagnosa' untuk memeriksa kembali."
        )
        self.btn_mulai.pack(pady=(12, 0))

# MENJALANKAN APLIKASI
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiPakarTHT(root)
    root.mainloop()