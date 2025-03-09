import streamlit as st
st.set_page_config(page_title="Analisis Penyewaan Sepeda", layout="wide")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    df = pd.read_csv('hour.csv')
    
    df.rename(columns={
        'instant': 'Indeks',
        'dteday': 'Tanggal',
        'season': 'Musim',
        'yr': 'Tahun',
        'mnth': 'Bulan',
        'hr': 'Jam',
        'holiday': 'Hari_Libur',
        'weekday': 'Hari',
        'workingday': 'Hari_Kerja',
        'weathersit': 'Cuaca',
        'temp': 'Temperatur',
        'atemp': 'Temperatur_Terasa',
        'hum': 'Kelembapan',
        'windspeed': 'Kecepatan_Angin',
        'casual': 'Pengguna_Kasual',
        'registered': 'Pengguna_Terdaftar',
        'cnt': 'Jumlah_Sewa'
    }, inplace=True)
    
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    return df

df = load_data()

st.sidebar.title("Pengaturan")
st.sidebar.header("Filter Data")

# Pilih Tahun
tahun = st.sidebar.selectbox("Pilih Tahun", options=df['Tahun'].unique())

# Mapping label Musim
musim_dict = {1: 'Semi', 2: 'Panas', 3: 'Gugur', 4: 'Dingin'}
musim = st.sidebar.selectbox(
    "Pilih Musim",
    options=df['Musim'].unique(),
    format_func=lambda x: musim_dict[x]
)

st.title("Dashboard Analisis Penyewaan Sepeda")
st.markdown("""
### Visualisasi Data Penyewaan Sepeda Berdasarkan:
1. Pola Harian
2. Pengaruh Musim
""")

tab1, tab2, tab3 = st.tabs(["Pola Harian", "Pengaruh Musim", "Data Mentah"])

with tab1:
    st.header("Pola Penyewaan Harian")
    
    df_jam = df[df['Tahun'] == tahun].groupby("Jam")["Jumlah_Sewa"].mean().reset_index()
    
    plt.figure(figsize=(10, 5))
    sns.lineplot(x=df_jam["Jam"], y=df_jam["Jumlah_Sewa"], marker="o")
    plt.title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
    plt.xlabel("Jam dalam Sehari")
    plt.ylabel("Rata-rata Penyewaan")
    plt.xticks(range(0, 24))
    plt.grid()
    st.pyplot(plt)
    
    st.markdown("""
    **Insight:**
    - Puncak penyewaan terjadi pada jam 17-18 (waktu pulang kerja)
    - Penyewaan terendah terjadi dini hari (00:00-05:00)
    """)

with tab2:
    st.header("Pengaruh Musim Terhadap Penyewaan")
    
    df_musim = df.groupby('Musim', as_index=False)['Jumlah_Sewa'].mean()
    df_musim['Musim'] = df_musim['Musim'].map(musim_dict)
    
    plt.figure(figsize=(10, 5))
    sns.barplot(x='Musim', y='Jumlah_Sewa', data=df_musim, order=['Semi', 'Panas', 'Gugur', 'Dingin'])
    plt.title("Rata-rata Penyewaan Berdasarkan Musim")
    plt.xlabel("Musim")
    plt.ylabel("Rata-rata Penyewaan")
    st.pyplot(plt)
    
    st.markdown("""
    **Insight:**
    - Musim Gugur memiliki penyewaan tertinggi (rata-rata 236 sewa/hari)
    - Musim Semi memiliki penyewaan terendah (rata-rata 111 sewa/hari)
    """)

with tab3:
    st.header("Data Mentah")
    st.dataframe(df, height=400)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Penyewaan", df['Jumlah_Sewa'].sum())
    with col2:
        st.metric("Rata-rata Harian", round(df['Jumlah_Sewa'].mean(), 2))
    with col3:
        st.metric("Maksimum Harian", df['Jumlah_Sewa'].max())

with st.expander("Tentang Dataset"):
    st.markdown("""
    **Bike Sharing Dataset**
    - Mengandung data penyewaan sepeda per jam dari tahun 2011-2012
    - Fitur utama:
        - Variabel temporal (jam, hari, bulan, tahun)
        - Kondisi cuaca
        - Jumlah penyewa (casual & registered)
    """)
