# **Market Demand and Sales Analysis**

## Repository Outline
```
data_analysis repository
├── dataset
│   ├── data_from_DE.csv - Dataset yang diperoleh dari tim Data Engineer yang digunakan sebagai sumber data utama untuk analisis
│   │
│   └── data_dashboard.csv - Dataset yang telah diproses dan dibersihkan untuk keperluan visualisasi dashboard
│
├── data_analysis.ipynb - Notebook berisi proses eksplorasi data (EDA), analisis pola permintaan, serta identifikasi faktor yang mempengaruhi penjualan
│
└── sales_dashboard.pbix - Dashboard Power BI yang menampilkan insight utama dari hasil analisis data
```

## Project Overview
Proyek ini bertujuan untuk menganalisis pola permintaan penjualan dalam dataset retail/e-commerce. Analisis dilakukan untuk memahami distribusi produk, tren penjualan bulanan, perilaku transaksi konsumen, serta faktor operasional yang mempengaruhi performa penjualan.

Hasil analisis ini digunakan untuk mengidentifikasi insight bisnis yang relevan serta memberikan gambaran mengenai dinamika permintaan sebelum dilakukan proses demand forecasting pada tahap selanjutnya.

## Analysis Scope
Analisis dalam proyek ini mencakup beberapa aspek utama, yaitu:

- Demand Overview:  
    Memahami distribusi penjualan berdasarkan kategori produk dan wilayah geografis.

- Demand Pattern:  
    Menganalisis tren penjualan bulanan, pertumbuhan penjualan, serta pola fluktuasi permintaan dari waktu ke waktu.

- Demand Drivers:  
    Mengidentifikasi faktor yang mempengaruhi penjualan seperti metode pembayaran, pola pembelian weekday vs weekend, serta faktor logistik.

- Operational Factors:  
    Mengevaluasi tingkat pengembalian produk dan pembatalan pesanan untuk memahami potensi hambatan dalam proses transaksi.

## Dashboard
Hasil analisis divisualisasikan dalam Power BI dashboard untuk mempermudah eksplorasi insight secara interaktif. Dashboard ini menampilkan ringkasan performa penjualan, distribusi permintaan produk, tren penjualan, serta beberapa indikator operasional utama yang relevan untuk pengambilan keputusan bisnis.