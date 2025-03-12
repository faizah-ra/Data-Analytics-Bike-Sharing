## Struktur Proyek
submission
├───dashboard
│   ├───data.csv
│   └───dashboard.py
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
1. Kapan waktu dengan jumlah penyewaan sepeda paling tinggi dan paling rendah?
2. Bagaimana pengaruh musim terhadap jumlah penyewaan sepeda?

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
   streamlit
   matplotlib
   seaborn
   pandas
   streamlit

## Hasil Analisis
**Tren Waktu Penyewaan**
- Jam sibuk: 17.00-18.00 (waktu pulang kerja)
- Jam sepi: 01.00-05.00 (dini hari hingga subuh)

**Pengaruh Musim**
- Musim Gugur: Jumlah sewa tertinggi (236 sewa/hari)
- Musim Semi: Jumlah sewa terendah (111 sewa/hari)

## Kontribusi
- Faizah Rizki Auliawati
- Email: frauliawati@gmail.com
- ID Dicoding: MC0092D5X2547
