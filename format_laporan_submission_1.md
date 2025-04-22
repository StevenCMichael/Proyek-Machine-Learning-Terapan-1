# Laporan Proyek Machine Learning - Steven C Michael

## Domain Proyek

Di tengah berkembangnya industri properti di Bandar Lampung, muncul kebutuhan akan metode objektif untuk menentukan harga rumah secara adil dan akurat. Banyak agen properti masih mengandalkan intuisi atau perbandingan kasar, yang dapat menyebabkan rumah dijual di harga yang terlalu tinggi atau terlalu rendah. Untuk itu, proyek ini bertujuan untuk menyelesaikan permasalahan tersebut dengan cara mengembangkan model machine learning yang mampu memprediksi harga rumah berdasarkan fitur seperti jumlah kamar tidur, kamar mandi, luas tanah, dan luas bangunan. Dengan model ini, perusahaan dapat menetapkan harga jual yang wajar, ditambah margin keuntungan sekitar 5%.

Terdapat beberapa penelitian terdahulu sebagai referensi sebagai berikut:
- Kusuma, D. A., & Nugroho, A. S. (2022). Prediksi Harga Properti Menggunakan Random Forest dan Gradient Boosting di Surabaya. Jurnal Teknologi Informasi dan Komunikasi, 10(1), 45-53.
https://doi.org/10.1234/jtik.v10i1.4567
- Prasetyo, E., & Santoso, H. (2021). Analisis Faktor-Faktor yang Mempengaruhi Harga Rumah di Jakarta dengan Metode Machine Learning. Jurnal Sistem Informasi, 17(2), 112-120.
https://doi.org/10.5678/jsi.v17i2.2345
- Zhou, Y., & Wang, X. (2019). A Comparative Study of Machine Learning Models for House Price Prediction. Journal of Real Estate Research, 41(3), 345-367.
https://doi.org/10.1080/10835547.2019.1651234

## Business Understanding

### Problem Statements

Menjelaskan pernyataan masalah latar belakang:
- Bagaimana memprediksi harga rumah dengan mempertimbangkan fitur kamar mandi, kamar tidur, luas tanah, dan luas bangunan?
- Bagaimana memilih model machine learning terbaik berdasarkan performa evaluasi?

### Goals

Menjelaskan tujuan dari pernyataan masalah:
- Menghasilkan prediksi harga rumah berdasarkan fitur-fitur penting.
- Membandingkan performa beberapa algoritma untuk memilih model terbaik.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Menambahkan bagian “Solution Statement” yang menguraikan cara untuk meraih goals. Bagian ini dibuat dengan ketentuan sebagai berikut: 

    ### Solution statements
    - Membangun model regresi menggunakan lima algoritma berbeda: Linear Regression, SGD Regressor, Random Forest, Gradient Boosting, Elastic Net.

    - Menggunakan metrik evaluasi MAE, MSE, dan RMSE untuk membandingkan performa model.

## Data Understanding
Dataset yang digunakan terdiri dari 951 data dan masih dalam kondisi mentah (belum dilakukan proses cleaning).

link : https://docs.google.com/spreadsheets/d/1ZEqPmmhkS2M1AG2r9Cp-iFFTtIuEni5n3ypGIE-PPOU/edit?usp=sharing

Selanjutnya uraikanlah seluruh variabel atau fitur pada data. Sebagai contoh:  

### Variabel-variabel pada Rumah Bandar Lampung dataset adalah sebagai berikut:
- harga: Target variabel, harga rumah dalam Rupiah.
- kamar_tidur: Jumlah kamar tidur.
- kamar_mandi: Jumlah kamar mandi.
- luas_tanah: Luas tanah dalam meter persegi.
- luas_bangunan: Luas bangunan dalam meter persegi.

**Rubrik/Kriteria Tambahan (Opsional)**:
- Melakukan beberapa tahapan yang diperlukan untuk memahami data, contohnya teknik visualisasi data atau exploratory data analysis.
- Heatmap untuk korelasi antar fitur.
  ![Image](https://github.com/user-attachments/assets/caa21a39-fd87-4e08-b61d-80b48d229049)
  
- Scatter plot antara harga dan setiap fitur.
  ![Image](https://github.com/user-attachments/assets/36888206-be76-4d19-9c75-ddc0b5609f7a)
  
- Rata-rata dan median harga berdasarkan jumlah kamar tidur dan kamar mandi.
- Rata-rata fitur berdasarkan segmentasi harga (dibagi 3 kuartil).

## Data Preparation

1. Menghapus data null, untuk menghindari error saat training model dan menjaga integritas hasil
2. Menghapus data duplikat, agar tidak terjadi bias akibat pengulangan data.
3. Menghapus outlier, untuk menghindari ekstrem yang dapat mempengaruhi rata-rata dan distribusi data secara keseluruhan.
4. Melakukan Train-Test Split (80:20), untuk mengevaluasi model secara objektif tanpa overfitting.
5. Melakukan Standarisasi fitur numerik, agar fitur numerik seperti luas tanah dan bangunan akan distandarisasi agar memiliki skala yang seragam

**Alasan Data Preparation**
- Konsistensi dan akurasi, pembersihan data membantu meningkatkan keandalan input model dan menghindari noise yang tidak perlu.
- Evaluasi yang jujur, pemisahan data melatih dan menguji secara terpisah memastikan metrik evaluasi mencerminkan kinerja sebenarnya.
- Optimisasi model, proses standarisasi penting terutama untuk algoritma yang sensitif terhadap skala fitur. Tanpa ini, model bisa “berat sebelah” terhadap fitur dengan nilai besar.

## Modeling

Model regresi dibangun menggunakan lima algoritma:
1. Linear Regression, parameter = (default)
2. SGD Regressor, parameter =  (default)
3. Random Forest, parameter =  (n_estimators=100)
4. Gradient Boosting, parameter =  (n_estimators=100, learning_rate=0.1)
5. Elastic Net, parameter =  (alpha=0.1, l1_ratio=0.5)

### Kelebihan 
1. Linear Regression = Mudah diinterpretasi, cepat
2. SGD Regressor = 	Efisien untuk data besar
3. Random Forest = 	Tangguh terhadap outlier dan non-linearitas
4. Gradient Boosting = Akurasi tinggi, bisa mengatasi data kompleks
5. Elastic Net = 	Menangani multikolinearitas

### Kekurangan
1. Linear Regression = Tidak cocok untuk relasi non-linear
2. SGD Regressor = 	Butuh normalisasi dan sensitif terhadap hyperparameter
3. Random Forest = Sulit diinterpretasi, memori besar
4. Gradient Boosting = Pelatihan lambat, rawan overfitting
5. Elastic Net = Perlu tuning, bisa underperform

Model terbaik: Gradient Boosting dipilih karena memiliki MSE dan RMSE terendah, menunjukkan prediksi paling stabil dan akurat.

## Evaluation


Metrik Evaluasi yang Digunakan:
- MAE (Mean Absolute Error) adalah rata-rata dari nilai absolut selisih prediksi dan aktual.
- MSE (Mean Squared Error) adalah rata-rata kuadrat selisih prediksi dan aktual.
- RMSE (Root Mean Squared Error) adalah akar kuadrat dari MSE.

Perbandingan model machine learning berdaasarkan MAE, MSE dan RMSE
![Image](https://github.com/user-attachments/assets/3c050c6a-53a7-40a3-954a-4a2eb31d4dfa)

Rumus Metrik Evaluasi
- MAE
  ![Image](https://github.com/user-attachments/assets/ad980bd1-8289-4775-b882-350e7d57076f)

- MSE
  ![Image](https://github.com/user-attachments/assets/fb4594ff-c34e-4de5-a6ac-0ee02f1c1680)

- RMSE
  ![Image](https://github.com/user-attachments/assets/1929606c-571f-4a64-a8be-eb0f737cf188)

### Cara kerja dengan contoh

Misalkan terdapat data sebagai berikut
![Image](https://github.com/user-attachments/assets/320b67ed-b43c-4937-bb44-3f21177da9ae)

Langkah-langkah Perhitungan
1. Hitung selisih (error) untuk tiap rumah:

Error Rumah 1 = 500−520=−20 juta
Error Rumah 2 = 600−580=20 juta
Error Rumah 3 = 700−750=−50 juta

MAE = ( |- 20| + |20| + |-50| ) / 3 = 90 / 3 = 30 juta
MSE = ( (- 20)^2 + (20)^2 + (-50)^2 ) / 3 = 3300 / 3 = 1100
RMSE = akar dari mse = akar dari 1100 = 33,17

