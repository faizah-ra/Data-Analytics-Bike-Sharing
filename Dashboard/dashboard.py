import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour_df = pd.read_csv("https://raw.githubusercontent.com/faizah-ra/data-analysis-bike-sharing/refs/heads/main/Dashboard/hour.csv")

# Preprocessing
hour_df['date'] = pd.to_datetime(hour_df['dteday'])
season_mapping = {4: "Dingin", 3: "Gugur", 2: "Panas", 1: "Semi"}
hour_df["season_label"] = hour_df["season"].map(season_mapping)

# Clustering waktu preprocessing
def categorize_hour(hour):
    if 0 <= hour < 6: return "Dini Hari"
    elif 6 <= hour < 11: return "Pagi"
    elif 11 <= hour < 16: return "Siang"
    elif 16 <= hour < 21: return "Sore"
    else: return "Malam"
hour_df["Kategori_Waktu"] = hour_df["hr"].apply(categorize_hour)

# Sidebar
with st.sidebar:
    st.image("https://www.planetizen.com/files/images/shutterstock_1727726158.jpg")
    date_range = st.date_input(
    label="📅 Rentang Waktu",
    min_value=hour_df["date"].min(),
    max_value=hour_df["date"].max(),
    value=(hour_df["date"].min(), hour_df["date"].max())
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    st.error("❌ Harap pilih dua tanggal (awal dan akhir) untuk filter rentang waktu.")
    st.stop()

# Date filtering
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)
filtered_df = hour_df[(hour_df['date'] >= start_date) & (hour_df['date'] <= end_date)]

# Streamlit App
st.title("Analisis Penyewaan Sepeda")

# Visualization 1: Hourly Pattern
st.subheader("Pola Penyewaan Sepeda dalam 24 Jam")
hourly_rental = filtered_df.groupby('hr')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,5))
sns.lineplot(x='hr', y='cnt', data=hourly_rental, 
             marker="o", color="b", ax=ax)
ax.set(xlabel="Jam dalam Sehari", ylabel="Rata-rata Penyewaan",
       xticks=range(0,24), title="Lonjakan dan Penurunan Penyewaan Sepeda dalam 24 Jam")
ax.grid()
st.pyplot(fig)
st.write("""📌 **Insight :**
-  Pola penyewaan sepeda membentuk dua puncak utama, yaitu pagi (sekitar jam 08:00) dan sore (sekitar jam 17:00 - 18:00).
-  Lonjakan pagi kemungkinan disebabkan oleh orang yang berangkat kerja atau sekolah.
-  Lonjakan sore terjadi saat jam pulang kerja, yang menunjukkan banyaknya pengguna sepeda untuk perjalanan pulang.
-  Aktivitas penyewaan sepeda menurun di tengah malam hingga subuh, yang wajar karena jam istirahat.
""")

# Visualization 2: Seasonal Impact
st.subheader("Pengaruh Musim terhadap Penyewaan Sepeda")
seasonal_rental = filtered_df.groupby("season_label")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='season_label', y='cnt', data=seasonal_rental, 
            color="#1f77b4", ax=ax)
ax.set(xlabel="Musim", ylabel="Rata-rata Penyewaan",
       title="Rata-rata Penyewaan Sepeda Berdasarkan Musim")
ax.grid(linestyle="--", alpha=0.8)
st.pyplot(fig)
st.write("""📌**Insight:**
- Rata-rata penyewaan sepeda pada musim gugur adalah yang tertinggi dibanding musim lainnya, bisa jadi karena cuaca yang lebih nyaman untuk bersepeda (tidak terlalu panas atau dingin).
- Rata-rata penyewaan sepeda di musim semi jauh lebih rendah dibanding musim lainnya, kemungkinan penyebabnya adalah hujan lebih sering terjadi di musim ini, atau suhu yang masih relatif dingin setelah musim dingin.
- Musim panas memiliki penyewaan sepeda yang hampir setara dengan musim gugur, menunjukkan bahwa banyak orang tetap bersepeda meskipun cuaca lebih panas.
- Musim dingin juga memiliki angka penyewaan yang cukup tinggi, yang bisa jadi menunjukkan bahwa sebagian besar pengguna adalah commuter (pengguna harian) yang tetap menggunakan sepeda sebagai transportasi utama.
""")

# Visualization 3: Time Clustering
st.subheader("Clustering Penyewaan Sepeda Berdasarkan Kategori Waktu")
grouped_by_time = filtered_df.groupby("Kategori_Waktu")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='Kategori_Waktu', y='cnt', data=grouped_by_time,
            order=["Dini Hari", "Pagi", "Siang", "Sore", "Malam"],
            color="#1f77b4", ax=ax)
ax.set(xlabel="Kategori Waktu", ylabel="Penyewa Sepeda",
       title="Penyewaan Sepeda Berdasarkan Kategori Waktu")
ax.grid(linestyle="--", alpha=0.8)
st.pyplot(fig)
st.write("""📌 **Insight :**
- Sore hari jadi puncak penyewaan, kemungkinan karena pulang kerja/sekolah.
- Pagi & siang tinggi, mencerminkan commuting & rekreasi.
- Malam & dini hari rendah, mungkin karena faktor keamanan & aktivitas berkurang.
- Pola ini menunjukkan bahwa penyewaan sepeda berhubungan erat dengan mobilitas harian dan kebiasaan pengguna.
""")

# Visualization 4: Weather Clustering
st.subheader("Clustering Cuaca terhadap Penyewaan Sepeda")
seasonal_rental = filtered_df.groupby("season_label")["cnt"].mean().reset_index()

fig, ax = plt.subplots(figsize=(8,5))
sns.barplot(x='season_label', y='cnt', data=seasonal_rental,
            order=["Semi", "Panas", "Gugur", "Dingin"],
            color="#1f77b4", ax=ax)
ax.set(xlabel="Musim", ylabel="Penyewa Sepeda",
       title="Penyewaan Sepeda Berdasarkan Musim")
ax.grid(linestyle="--", alpha=0.7)
st.pyplot(fig)
st.write("""📌 **Insight :**
- Musim gugur memiliki penyewaan tertinggi, mungkin karena cuaca sejuk & nyaman.
- Musim panas & dingin moderat, kemungkinan karena suhu ekstrem memengaruhi minat pengguna.
- Musim semi terendah, mungkin akibat cuaca yang kurang mendukung atau curah hujan tinggi.
""")
