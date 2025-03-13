## Struktur Proyek
submission
├───dashboard
│   ├───dashboard.py
│   ├───day.csv
│   └───hour.csv
├───data
│   ├───day.csv
│   └───hour.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt

# Data Analysis Bike Sharing Dashboard
Dashboard ini merupakan aplikasi analisis data penyewaan sepeda yang menampilkan visualisasi interaktif menggunakan Streamlit. Proyek ini mengolah data dari file CSV dan menyediakan insight mengenai pola penyewaan berdasarkan waktu dan kondisi (musim, hari kerja, dll).

## Pertanyaan Bisnis
1. Kapan terjadi lonjakan dan penurunan aktivitas penyewaan sepeda dalam 24 jam?
2. Bagaimana perbedaan musim mempengaruhi rata-rata penyewaan sepeda?

## Setup Environment

### Menggunakan Google Colab
1. Unduh dataset dan notebook dari repositori ini
2. Buka [Google Colab](https://colab.research.google.com/)
3. Upload file `notebook.ipynb` ke Colab
4. Jalankan sel-sel kode secara berurutan

### Menggunakan Shell/Terminal
Jika Anda ingin menggunakan terminal untuk setup, Anda bisa mengikuti langkah-langkah berikut:

1. Buat direktori baru untuk proyek Anda:
   bash
   mkdir proyek_analisis_data
   cd proyek_analisis_data

2. Install pustaka yang diperlukan menggunakan Pipenv:
   bash
   Copy code
   pipenv install
   pipenv shell
   pip install -r requirements.txt

3. Jalankan Aplikasi Streamlit
   Untuk menjalankan dashboard, gunakan perintah berikut di terminal:
   streamlit run dashboard.py

5. Pustaka yang Dibutuhkan
   pandas
   matplotlib
   seaborn
   streamlit

## Hasil Analisis
** Lonjakan dan Penurunan Aktivitas Penyewaan Sepeda**
- Lonjakan  : 17.00-18.00 (sore)
- Penurunan : 01.00-05.00 (dini hari hingga subuh)

**Pengaruh Musim**
- Musim Gugur: Jumlah sewa tertinggi (236 sewa/hari)
- Musim Semi: Jumlah sewa terendah (111 sewa/hari)

## Kontribusi
- Faizah Rizki Auliawati
- Email: frauliawati@gmail.com
- ID Dicoding: MC0092D5X2547
