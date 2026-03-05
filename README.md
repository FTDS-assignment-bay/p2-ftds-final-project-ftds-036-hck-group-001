# **DemandSense AI**
## **Market Demand and Sales Analysis**

## Repository Outline
```
main
├── Data Preprocessing
|   ├── dataset - Folder yang berisikan data-data mentah per bulan dari Desember 2023 sampai November 2025 dalam format xlsx
|   ├── cleaned_data_analysis.csv - Dataset yang sudah diolah dan dibersihkan untuk keperluan tim analisis
|   ├── data_pipeline.png - Gambar yang menunjukkan alur data pipeline di projek ini
|   ├── data_preprocessing.ipynb - File notebook yang berisikan untuk mengolah dan membersihkan data mentah menjadi dataset siap pakai untuk keperluan tim
|   |                              analisis dan tim modelling
|   ├── data_preprocessing_DAG.py - File untuk mengotomasi data pipeline dari loading data dari database, mengolah dan membersihkan data, dan upload data
|   ├── forecast_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (semua kategori produk)
|   ├── forecast_bathroom_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Bathroom & Cleaning)
|   ├── forecast_home_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Home Organization & Living)
|   ├── forecast_kitchen_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Kitchen & Dining)
|   ├── forecast_other_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Other)
|   ├── forecast_storage_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Food Storage &  Packaging)
|   ├── forecast_tools_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Tools & Hardware)
|   └── table_creation.sql - File untuk pembuatan tabel ke dalam database
├── Data Analysis
|   ├── dataset
│   |   ├── data_from_DE.csv - Dataset yang diperoleh dari tim Data Engineer yang digunakan sebagai sumber data utama untuk analisis
│   |   └── data_dashboard.csv - Dataset yang telah diproses dan dibersihkan untuk keperluan visualisasi dashboard
|   ├── data_analysis.ipynb - Notebook berisi proses eksplorasi data (EDA), analisis pola permintaan, serta identifikasi faktor yang mempengaruhi penjualan
|   └── sales_dashboard.pbix - Dashboard Power BI yang menampilkan insight utama dari hasil analisis data
└── Data Modelling
```

## Project Overview
Proyek ini bertujuan untuk menganalisis pola permintaan penjualan dalam dataset retail/e-commerce, serta membangun time-series forecasting model untuk memprediksi customer's demand dalam 1 bulan kedepan. Analisis dilakukan untuk memahami distribusi produk, tren penjualan bulanan, perilaku transaksi konsumen, serta faktor operasional yang mempengaruhi performa penjualan.

Hasil analisis ini digunakan untuk mengidentifikasi insight bisnis yang relevan serta memberikan gambaran mengenai dinamika permintaan sebelum dilakukan proses demand forecasting pada tahap selanjutnya.

## Problem Statement
Industri e-commerce menghadapi permintaan yang sering kali berubah-ubah karena berbagai faktor seperti musim dan periode promo, perubahan tren konsumen, aktivitas diskon dan voucher, serta faktor eksternal.  Perusahaan harus mampu mengelola ketersediaan stok per kategori produk, alokasi gudang & distribusi, perencanaan procurement, dan strategi promosi.

Tanpa sistem forecasting, perusahaan berisiko mengalami stockout (kehilangan potensi penjualan dan penurunan customer satisfaction), overstock (peningkatan biaya penyimpanan dan risiko dead inventory), dan perencanaan supply chain yang tidak optimal  yang dapat meningkatkan biaya logistik dan operasional. Dampak bisnis dari kondisi tersebut adalah menurunnya potensi revenue, rendahnya inventory turnover, inefisiensi working capital, dan melemahnya daya saing di pasar yang kompetitif.

Oleh karena itu, model Machine Learning forecasting diperlukan untuk memprediksi kuantitas produk terjual per kategori produk terhadap perubahan pola permintaan, sehingga perusahaan dapat mengurangi stockout dan overstock, mengurangi working capital, mengalokasikan budget promosi secara data-driven, mengurangi biaya logistik, dan memaksimalkan revenue.


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
