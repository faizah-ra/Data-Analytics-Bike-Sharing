# 🚲 Bike Sharing Data Analysis Dashboard using Streamlit

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Dashboard interaktif ini dirancang untuk menganalisis perilaku penyewaan sepeda berdasarkan data harian dan jam. Proyek dibangun menggunakan Python dan *Streamlit*, serta dilengkapi dengan visualisasi eksploratif untuk memahami pola penggunaan sepeda berdasarkan waktu, musim, dan hari kerja.

📌 Proyek ini merupakan bagian dari submission **Belajar Analisis Data dengan Python** di Dicoding.  
🎖️ **Rating Submission: 5/5 (Bintang Lima)**  
📁 Submission ID: `4087962`  
📅 Tanggal Kirim: `15 Maret 2025`

---

## 👩‍💻 Peran dan Tanggung Jawab sebagai System Analyst

Sebagai *System Analyst*, saya bertanggung jawab untuk:

- 💡 **Menganalisis kebutuhan pengguna** terkait informasi pola penyewaan sepeda.
- 🧩 **Mendesain alur data** dari *gathering*, *cleaning*, hingga visualisasi interaktif.
- 🖥️ **Mengimplementasikan dashboard Streamlit** yang mudah digunakan dengan filter dinamis.
- 📈 **Menyusun insight berbasis data** untuk menjawab pertanyaan bisnis utama.
- 📑 **Menyusun dokumentasi sistem** dan *user flow* dalam bentuk *notebook* dan markdown.

---

## 🧾 Pertanyaan Bisnis

1. Kapan terjadi lonjakan dan penurunan aktivitas penyewaan sepeda dalam 24 jam?
2. Bagaimana perbedaan musim memengaruhi rata-rata penyewaan sepeda?

---

## 📊 Hasil Analisis

### 🔄 Pola Waktu Harian
- **Lonjakan:** Jam 17.00–18.00 (jam pulang kerja)
- **Penurunan:** Jam 01.00–05.00 (dini hari)

### 🍂 Pengaruh Musim
- **Musim Gugur (Fall):** Aktivitas sewa tertinggi (236 sewa/hari)
- **Musim Semi (Spring):** Aktivitas sewa terendah (111 sewa/hari)

---

## 💻 Teknologi dan Library

- **Bahasa Pemrograman**: Python
- **Dashboard**: Streamlit
- **Visualisasi**: Seaborn, Matplotlib
- **Analisis Data**: Pandas
- **Lingkungan**: Jupyter Notebook, Google Colab, Terminal

---

## 🏗️ Struktur Proyek
data-analysis-bike-sharing/
├───dashboard
│   ├───dashboard.py      # Aplikasi Streamlit      
│   ├───day.csv           # Data penyewaan harian
│   └───hour.csv          # Data penyewaan per jam
├───data
│   ├───day.csv
│   └───hour.csv
├───notebook.ipynb        # Exploratory Data Analysis
├───README.md             # Dokumentasi proyek
├───requirements.txt      # Dependensi proyek
└───url.txt               # Link deploy 


---

## ⚙️ Cara Menjalankan Proyek

### 🔹 Google Colab (EDA)
1. Unduh `notebook.ipynb` dan `data/*.csv`
2. Buka [Google Colab](https://colab.research.google.com/)
3. Upload file, lalu jalankan sel-sel kode

### 🔹 Terminal (Dashboard)
```bash
# Clone project
git clone https://github.com/faizah-ra/bike-sharing-dashboard.git
cd bike-sharing-dashboard

# Buat virtual environment (opsional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate.bat

# Instal dependensi
pip install -r requirements.txt

# Jalankan dashboard
streamlit run dashboard/dashboard.py
```
---

## 👩‍💻 Tentang Pengembang

**Faizah Rizki Auliawati**  
Mahasiswa Informatika sekaligus seorang Data Enthusiast dengan minat mendalam pada bidang Machine Learning, System Analysis, dan pengembangan solusi berbasis data. Proyek ini merupakan bagian dari portofolio ilmiah dan praktikal untuk pengembangan sistem cerdas berbasis rekomendasi.

---

## 📄 Lisensi

Proyek ini berlisensi MIT. Lihat `LICENSE` untuk detail.
