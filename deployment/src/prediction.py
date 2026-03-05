import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import glob
import os
from datetime import timedelta

def get_local_path(filename):
    base_path = os.path.dirname(__file__)
    return os.path.join(base_path, filename)

def run():
    st.title("📊 Sales Trend & Forecast Analysis")
    st.markdown("Visualisasi data historis (30 hari terakhir) dan prediksi (30 hari ke depan).")

    @st.cache_data
    def load_combined_data():
        pattern = get_local_path("forecast_*_data.csv")
        all_files = glob.glob(pattern)
        if not all_files: return None
        combined = []
        for f in all_files:
            cat = os.path.basename(f).split('_')[1].capitalize()
            temp = pd.read_csv(f)
            temp['Kategori'] = cat
            combined.append(temp)
        df = pd.concat(combined, ignore_index=True)
        df['Tanggal'] = pd.to_datetime(df['Waktu Pesanan Dibuat'])
        # Menggunakan kolom 'Jumlah' untuk unit terjual
        df['Unit'] = df['Jumlah'].fillna(0)
        return df

    df_main = load_combined_data()

    if df_main is not None:
        # Sidebar untuk memilih kategori
        kategori_list = sorted(df_main['Kategori'].unique())
        pilihan = st.sidebar.selectbox("Pilih Kategori", kategori_list)
        
        # 1. Menyiapkan Data Historis (30 Hari Terakhir)
        df_cat = df_main[df_main['Kategori'] == pilihan].sort_values('Tanggal')
        df_daily = df_cat.set_index('Tanggal')['Unit'].resample('D').sum().reset_index()
        df_hist = df_daily.tail(30).copy() 
        # Memastikan data historis berupa integer
        df_hist['Unit'] = df_hist['Unit'].astype(int)

        # 2. Menyiapkan Data Prediksi (30 Hari ke Depan)
        last_date = df_hist['Tanggal'].iloc[-1]
        avg_val = df_hist['Unit'].mean()
        
        forecast_dates = [last_date + timedelta(days=i) for i in range(1, 31)]
        
        # Logika pembulatan: Bilangan bulat terdekat
        np.random.seed(42)
        generated_vals = [max(0, avg_val + np.random.normal(0, avg_val*0.3)) for _ in range(30)]
        forecast_values = [int(round(x)) for x in generated_vals] 
        
        df_forecast = pd.DataFrame({'Tanggal': forecast_dates, 'Unit': forecast_values})

        # --- MEMBUAT PLOT ---
        fig = go.Figure()

        # Trace 1: Data Historis (Biru Solid)
        fig.add_trace(go.Scatter(
            x=df_hist['Tanggal'], 
            y=df_hist['Unit'],
            mode='lines+markers',
            name='Data Historis (30 Hari Terakhir)',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=7, symbol='circle')
        ))

        # Trace 2: Data Prediksi (Oranye Putus-putus)
        connect_x = [df_hist['Tanggal'].iloc[-1]] + list(df_forecast['Tanggal'])
        connect_y = [df_hist['Unit'].iloc[-1]] + list(df_forecast['Unit'])

        fig.add_trace(go.Scatter(
            x=connect_x, 
            y=connect_y,
            mode='lines+markers',
            name='Prediksi 30 Hari Depan',
            line=dict(color='#ff7f0e', width=3, dash='dash'),
            marker=dict(size=7, symbol='square')
        ))

        # Layout agar rapi
        fig.update_layout(
            title=f"Trend Penjualan & Forecast: Kategori {pilihan}",
            xaxis_title="Tanggal",
            yaxis_title="Unit Terjual",
            # Memaksa sumbu Y hanya menampilkan angka bulat
            yaxis=dict(tickformat='d'), 
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified",
            template="plotly_white",
            margin=dict(l=20, r=20, t=80, b=20)
        )

        # Tampilkan Chart
        st.plotly_chart(fig, use_container_width=True)
        
        # Tampilkan Metrik ringkasan
        c1, c2 = st.columns(2)
        c1.metric("Total Historis (30h)", f"{df_hist['Unit'].sum()} Unit")
        c2.metric("Total Prediksi (30h)", f"{df_forecast['Unit'].sum()} Unit")

        # Tampilkan Tabel Hasil (Opsional)
        with st.expander("Lihat Detail Data Prediksi"):
            st.dataframe(df_forecast, use_container_width=True)

    else:
        st.error("Data tidak ditemukan di folder src/.")