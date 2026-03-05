# **DemandSense AI (Market Demand and Sales Analysis)**

![For accurate demand prediction!](demandSenseAI_logo.jpeg)

## Repository Outline
```
main/
├── Data Preprocessing/
|   ├── raw dataset/ - Folder yang berisikan data-data mentah per bulan dari Desember 2023 sampai November 2025 dalam format xlsx.
|   |
|   ├── analysis_dataset/
|   |   └── cleaned_data_analysis.csv - Dataset yang sudah diolah dan dibersihkan untuk keperluan tim analisis.
|   |
|   ├── modelling_dataset/
|   |   ├── forecast_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (semua kategori produk).
|   |   ├── forecast_bathroom_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Bathroom & Cleaning).
|   |   ├── forecast_home_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Home Organization & Living).
|   |   ├── forecast_kitchen_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Kitchen & Dining).
|   |   ├── forecast_other_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Other).
|   |   ├── forecast_storage_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Food Storage &  Packaging).
|   |   └── forecast_tools_data.csv - Dataset yang sudah dipersiapkan untuk keperluan tim modelling (kategori produk Tools & Accessories).
|   |
|   ├── data_pipeline.png - Gambar yang menunjukkan data pipeline dari projek ini.
|   ├── data_preprocessing.ipynb - File notebook untuk mengolah dan membersihkan data mentah agar siap pakai untuk keperluan analisis dan modelling
|   ├── data_preprocessing_DAG.py - File untuk mengotomasi data pipeline dari loading data dari database, mengolah dan membersihkan data, dan upload data.
|   └── table_creation.sql - File untuk pembuatan tabel ke dalam database.
|
├── Data Analysis/
|   ├── dataset/
│   |   ├── data_from_DE.csv - Dataset yang diperoleh dari tim Data Engineer yang digunakan sebagai sumber data untuk analisis.
│   |   └── data_dashboard.csv - Dataset yang telah diproses dan dibersihkan untuk keperluan visualisasi dashboard.
|   |
|   ├── data_analysis.ipynb - Notebook berisi proses eksplorasi data, analisis pola demand, dan identifikasi faktor yang mempengaruhi penjualan.
|   └── sales_dashboard.pbix - Dashboard Power BI yang menampilkan insight utama dari hasil analisis data.
|
├── Data Modelling/
│
├── deployment/
│   ├── src/
│   │   ├── eda.py - Script untuk menampilkan visualisasi dan insight hasil Exploratory Data Analysis (EDA) pada aplikasi.
│   │   ├── prediction.py - Script untuk menjalankan model forecasting dan menampilkan hasil prediksi permintaan.
│   │   └── streamlit_app.py - File utama aplikasi Streamlit yang mengatur layout dan navigasi halaman EDA serta Prediction.
│   │
│   ├── Dockerfile - File konfigurasi untuk membangun container aplikasi menggunakan Docker.
│   └── requirements.txt - Daftar dependensi Python yang diperlukan untuk menjalankan aplikasi deployment.
│
├── README.md - File berisikan ringkasan deskripsi dan dokumentasi dari projek ini.
└── demandSenseAI_logo.jpeg - Gambar mengenai logo DemandSense AI
```

## Project Overview
Proyek ini bertujuan untuk menganalisis pola permintaan penjualan dalam dataset retail/e-commerce, serta membangun time-series forecasting model untuk memprediksi customer's demand dalam 1 bulan kedepan. Analisis dilakukan untuk memahami distribusi produk, tren penjualan bulanan, perilaku transaksi konsumen, serta faktor operasional yang mempengaruhi performa penjualan.

Hasil analisis ini digunakan untuk mengidentifikasi insight bisnis yang relevan serta memberikan gambaran mengenai dinamika permintaan sebelum dilakukan proses demand forecasting pada tahap selanjutnya.

## Problem Statement
Industri e-commerce menghadapi permintaan yang sering kali berubah-ubah karena berbagai faktor seperti musim dan periode promo, perubahan tren konsumen, aktivitas diskon dan voucher, serta faktor eksternal.  Perusahaan harus mampu mengelola ketersediaan stok per kategori produk, alokasi gudang & distribusi, perencanaan procurement, dan strategi promosi.

Tanpa sistem forecasting, perusahaan berisiko mengalami stockout (kehilangan potensi penjualan dan penurunan customer satisfaction), overstock (peningkatan biaya penyimpanan dan risiko dead inventory), dan perencanaan supply chain yang tidak optimal  yang dapat meningkatkan biaya logistik dan operasional. Dampak bisnis dari kondisi tersebut adalah menurunnya potensi revenue, rendahnya inventory turnover, inefisiensi working capital, dan melemahnya daya saing di pasar yang kompetitif.

Oleh karena itu, model Machine Learning forecasting diperlukan untuk memprediksi kuantitas produk terjual per kategori produk terhadap perubahan pola permintaan, sehingga perusahaan dapat mengurangi stockout dan overstock, mengurangi working capital, mengalokasikan budget promosi secara data-driven, mengurangi biaya logistik, dan memaksimalkan revenue.

## Project Output
Output dari project ini adalah sebuah aplikasi yang memprediksi customer's demand dalam 1 bulan kedepan, serta sebuah dashboard untuk menganalisis pola permintaan penjualan.

## Data
Dataset ini berisi data transaksi pesanan e-commerce Indonesia dari Desember 2023 – November 2025, yang berisikan informasi seperti jumlah produk, biaya pengiriman, diskon, metode pembayaran, dan tujuan pengiriman. Setiap baris mewakili satu pesanan yang telah selesai atau dibatalkan. Dataset ini memiliki total 26,258 catatan pesanan dengan 50 kolom/atribut.

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

## Method
1. Database: PostgreSQL
2. Penanganan missing values: Imputation dengan nilai tertentu
3. Otomasi data pipeline: Airflow
4. Model Machine Learning: Hybrid Deep Learning Ensemble Model.
5. Metode training: Hybrid RNN + XGBoost Ensemble.
6. Metriks evaluasi: MAE (Mean Absolute Error), MAPE(Mean Absolute Percentage Error), Volume Accuracy (Mengukur akurasi total volume prediksi terhadap volume aktual)
7. Dashboard: Power BI
8. Deployment: HuggingFace

## Stacks
Programming langugage: SQL dan Python

Tools: Visual Studio Code, PostgreSQL, Power BI, dan HuggingFace

Library: psycopg2, pandas, numpy, glob, os, datetime, pendulum, elasticsearch, airflow, tensorflow, xgboost, scikit-learn, matplotlib, plotly, joblib

## Reference
URL Dataset: https://www.kaggle.com/datasets/bakitacos/indonesia-e-commerce-sales-and-shipping-20232025

URL HuggingFace: https://huggingface.co/spaces/Raifky/final_project_model

URL Presentation Slides: https://docs.google.com/presentation/d/1jSPtnN4fhYYo9X-LHmDsqbEbl2I3Py_hnNuDLsW3Z10/edit?usp=sharing




