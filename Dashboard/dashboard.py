import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour_df = pd.read_csv("https://raw.githubusercontent.com/faizah-ra/data-analysis-bike-sharing/refs/heads/main/Dashboard/hour.csv")

# Preprocessing
hour_df['date'] = pd.to_datetime(hour_df['dteday'])

# Sidebar (Filter Rentang Waktu)
min_date = hour_df["date"].min() 
max_date = hour_df["date"].max()


with st.sidebar:
    st.image("https://www.planetizen.com/files/images/shutterstock_1727726158.jpg")

    # Input rentang tanggal
    start_date, end_date = st.date_input(
        label="📅 Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Streamlit App
st.title("Analisis Penyewaan Sepeda")

# Visualisasi 1: Pola Penyewaan Sepeda dalam 24 Jam
st.subheader("Pola Penyewaan Sepeda dalam 24 Jam")
hourly_rental = hour_df.groupby('hr')['cnt'].mean().reset_index()
hourly_rental.columns = ["Jam", "Jumlah_Sewa"]

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x=hourly_rental["Jam"], y=hourly_rental["Jumlah_Sewa"], marker="o", color="b", ax=ax)
ax.set_xlabel("Jam dalam Sehari")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Lonjakan dan Penurunan Penyewaan Sepeda dalam 24 Jam")
ax.set_xticks(range(0, 24))
ax.grid()
st.pyplot(fig)
st.write("""
📌 **Insight :**
-  Pola penyewaan sepeda membentuk dua puncak utama, yaitu pagi (sekitar jam 08:00) dan sore (sekitar jam 17:00 - 18:00).
-  Lonjakan pagi kemungkinan disebabkan oleh orang yang berangkat kerja atau sekolah.
-  Lonjakan sore terjadi saat jam pulang kerja, yang menunjukkan banyaknya pengguna sepeda untuk perjalanan pulang.
-  Aktivitas penyewaan sepeda menurun di tengah malam hingga subuh, yang wajar karena jam istirahat.
""")
st.markdown("---")

# Visualisasi 2: Pengaruh Musim terhadap Penyewaan Sepeda
st.subheader("Pengaruh Musim terhadap Penyewaan Sepeda")
# Mapping musim ke label baru tanpa mengubah kolom aslinya
season_mapping = {4: "Dingin", 3: "Gugur", 2: "Panas", 1: "Semi"}
hour_df["season_label"] = hour_df["season"].map(season_mapping)

# Hitung rata-rata penyewaan sepeda per musim
seasonal_rental = hour_df.groupby("season_label")["cnt"].mean().reset_index()
seasonal_rental.columns = ["Musim", "Rata-rata Penyewaan"]

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=seasonal_rental["Musim"], y=seasonal_rental["Rata-rata Penyewaan"], palette="coolwarm", ax=ax)
ax.set_xlabel("Musim")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Musim")
ax.grid(linestyle="--", alpha=0.8)

# Tampilkan plot di Streamlit
st.pyplot(fig)
st.write("""
📌**Insight:**
- Rata-rata penyewaan sepeda pada musim gugur adalah yang tertinggi dibanding musim lainnya, bisa jadi karena cuaca yang lebih nyaman untuk bersepeda (tidak terlalu panas atau dingin).
- Rata-rata penyewaan sepeda di musim semi jauh lebih rendah dibanding musim lainnya, kemungkinan penyebabnya adalah hujan lebih sering terjadi di musim ini, atau suhu yang masih relatif dingin setelah musim dingin.
- Musim panas memiliki penyewaan sepeda yang hampir setara dengan musim gugur, menunjukkan bahwa banyak orang tetap bersepeda meskipun cuaca lebih panas.
- Musim dingin juga memiliki angka penyewaan yang cukup tinggi, yang bisa jadi menunjukkan bahwa sebagian besar pengguna adalah commuter (pengguna harian) yang tetap menggunakan sepeda sebagai transportasi utama.
""")
st.markdown("---")

# Clustering Waktu dalam Sehari
# Fungsi untuk mengkategorikan jam ke dalam kategori waktu
def categorize_hour(hour):
    if 0 <= hour < 6:
        return "Dini Hari"
    elif 6 <= hour < 11:
        return "Pagi"
    elif 11 <= hour < 16:
        return "Siang"
    elif 16 <= hour < 21:
        return "Sore"
    else:
        return "Malam"

# Tambahkan kolom kategori waktu
hour_df["Kategori_Waktu"] = hour_df["hr"].apply(categorize_hour)

# Hitung rata-rata penyewaan sepeda per kategori waktu
grouped_by_time = hour_df.groupby("Kategori_Waktu")["cnt"].mean().reset_index()
grouped_by_time.columns = ["Kategori Waktu", "Rata-rata Penyewaan"]

# Urutan kategori waktu
order = ["Dini Hari", "Pagi", "Siang", "Sore", "Malam"]

# Visualisasi
st.subheader("Clustering Penyewaan Sepeda Berdasarkan Kategori Waktu")

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x=grouped_by_time["Kategori Waktu"], y=grouped_by_time["Rata-rata Penyewaan"], order=order, palette="coolwarm", ax=ax)

ax.set_xlabel("Kategori Waktu")
ax.set_ylabel("Penyewa Sepeda")
ax.set_title("Penyewaan Sepeda Berdasarkan Kategori Waktu")
ax.grid(linestyle="--", alpha=0.8)

# Tampilkan plot di Streamlit
st.pyplot(fig)
st.write("""
📌 **Insight :**
- Sore hari jadi puncak penyewaan, kemungkinan karena pulang kerja/sekolah.
- Pagi & siang tinggi, mencerminkan commuting & rekreasi.
- Malam & dini hari rendah, mungkin karena faktor keamanan & aktivitas berkurang.
- Pola ini menunjukkan bahwa penyewaan sepeda berhubungan erat dengan mobilitas harian dan kebiasaan pengguna.
""")
st.markdown("---")

# Clustering Cuaca
st.subheader("Clustering Cuaca terhadap Penyewaan Sepeda")
# Mapping musim
musim_dict = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
hour_df["Musim_Label"] = hour_df["season"].map(musim_dict)  # Kolom season sesuai dataset

# Hitung rata-rata penyewaan sepeda per musim
seasonal_rental = hour_df.groupby("Musim_Label")["cnt"].mean().reset_index()
seasonal_rental.columns = ["Musim_Label", "Jumlah_Sewa"]

# Fungsi untuk mengkategorikan musim berdasarkan penyewaan
def categorize_season(rental):
    if rental > seasonal_rental["Jumlah_Sewa"].quantile(0.75):
        return "Musim Tinggi"
    elif rental < seasonal_rental["Jumlah_Sewa"].quantile(0.25):
        return "Musim Rendah"
    else:
        return "Musim Sedang"

# Tambahkan kategori penyewaan ke seasonal_rental
seasonal_rental["Kategori_Penyewaan"] = seasonal_rental["Jumlah_Sewa"].apply(categorize_season)

# Urutan musim
order = ["Semi", "Panas", "Gugur", "Dingin"]

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(
    x=seasonal_rental["Musim_Label"],
    y=seasonal_rental["Jumlah_Sewa"],
    order=order,
    palette="coolwarm",
    ax=ax
)

# Tambahkan label angka di atas batang
for p in ax.patches:
    ax.annotate(f'{p.get_height():.0f}',
                (p.get_x() + p.get_width() / 2, p.get_height()),
                ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Label & styling
ax.set_xlabel("Musim", fontsize=12)
ax.set_ylabel("Penyewa Sepeda", fontsize=12)
ax.set_title("Penyewaan Sepeda Berdasarkan Musim", fontsize=14, fontweight='bold')
ax.set_xticklabels(order, fontsize=11)
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Tampilkan plot di Streamlit
st.pyplot(fig)
st.write("""
📌 **Insight :**
- Musim gugur memiliki penyewaan tertinggi, mungkin karena cuaca sejuk & nyaman.
- Musim panas & dingin moderat, kemungkinan karena suhu ekstrem memengaruhi minat pengguna.
- Musim semi terendah, mungkin akibat cuaca yang kurang mendukung atau curah hujan tinggi.
""")
st.markdown("---")
