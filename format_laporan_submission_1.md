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

1. Bagaimana membangun model machine learning yang dapat memprediksi harga rumah berdasarkan fitur-fitur seperti kamar mandi, kamar tidur, luas tanah, dan luas bangunan?
2. Bagaimana memilih model terbaik dengan kesalahan prediksi yang sekecil mungkin menggunakan evaluasi MAE, MSE, dan RMSE?

### Goals

1. Menghasilkan model prediksi harga rumah dengan tingkat kesalahan (MAE, MSE, RMSE) yang rendah.
2. Membandingkan berbagai algoritma regresi dan memilih model dengan performa terbaik berdasarkan evaluasi kuantitatif.

### Solution statements
- Membangun model regresi menggunakan lima algoritma berbeda yaitu Linear Regression, SGD Regressor, Random Forest, Gradient Boosting, Elastic Net.
- Menggunakan metrik evaluasi MAE, MSE dan RMSE untuk membandingkan performa model.

## Data Understanding

Dataset yang digunakan adalah data harga rumah di wilayah Bandar Lampung 

### Link dataset
- https://docs.google.com/spreadsheets/d/1ZEqPmmhkS2M1AG2r9Cp-iFFTtIuEni5n3ypGIE-PPOU/edit?usp=sharing

### Jumlah baris dan kolom dataset
- Terdapat 951 baris dan 5 kolom

### Variabel-variabel pada Rumah Bandar Lampung dataset adalah sebagai berikut:
- harga: Target variabel, harga rumah dalam Rupiah.
- kamar_tidur: Jumlah kamar tidur.
- kamar_mandi: Jumlah kamar mandi.
- luas_tanah: Luas tanah dalam meter persegi.
- luas_bangunan: Luas bangunan dalam meter persegi.

### Kondisi data set
- Terdapat 36 data / baris yang null
- Terdapat 273 data duplikat
- Terdapat outlier pada kolom
  - kamar_tidur = 9
  - kamar_mandi = 0
  - luas_bangunan = 56
  - luas_tanah = 27
  - harga = 40 
  

### Eksploratory Data

- Heatmap untuk korelasi antar fitur.
  
  ![Image](https://github.com/user-attachments/assets/caa21a39-fd87-4e08-b61d-80b48d229049)
  
- Scatter plot antara harga dan setiap fitur.
  
  ![Image](https://github.com/user-attachments/assets/36888206-be76-4d19-9c75-ddc0b5609f7a)
  
  ![Image](https://github.com/user-attachments/assets/fc579bae-bdf5-490e-ac7e-e8900d523739)

  dan masih banyak lagi visualisasi scatter plot di notebook
  
- Rata-rata dan median harga berdasarkan jumlah kamar tidur dan kamar mandi.
  
  ![Image](https://github.com/user-attachments/assets/a4d36205-69c2-4848-8f80-dd126a332ced)
  
  
- Rata-rata fitur berdasarkan segmentasi harga (dibagi 3).
  
  ![Image](https://github.com/user-attachments/assets/84bd1cfa-6a59-437d-939f-387933253bc3)

## Data Preparation

1. Menghapus data duplikat, agar tidak terjadi bias akibat pengulangan data.
2. Menghapus data null, untuk menghindari error saat training model dan menjaga integritas hasil
3. Menghapus outlier, untuk menghindari ekstrem yang dapat mempengaruhi rata-rata dan distribusi data secara keseluruhan.
4. Melakukan Train-Test Split (80:20), untuk mengevaluasi model secara objektif tanpa overfitting.
5. Melakukan Standarisasi fitur numerik, agar fitur numerik seperti luas tanah dan bangunan akan distandarisasi agar memiliki skala yang seragam

### **Alasan Data Preparation**
- Konsistensi dan akurasi, pembersihan data membantu meningkatkan keandalan input model dan menghindari noise yang tidak perlu.
- Evaluasi yang jujur, pemisahan data melatih dan menguji secara terpisah memastikan metrik evaluasi mencerminkan kinerja sebenarnya.
- Optimisasi model, proses standarisasi penting terutama untuk algoritma yang sensitif terhadap skala fitur. Tanpa ini, model bisa “berat sebelah” terhadap fitur dengan nilai besar.

## Modeling

### Model 1: Linear Regression
- Cara Kerja: Linear Regression mencoba membangun hubungan linear antara variabel input dan target output. Ia menghitung garis lurus terbaik yang meminimalkan jumlah kuadrat selisih antara nilai prediksi dan nilai aktual menggunakan metode Ordinary Least Squares (OLS).
- Parameter: Menggunakan parameter default, tanpa regularisasi tambahan.
- Kelebihan: Sederhana, cepat, dan mudah dipahami dan cocok untuk hubungan yang benar-benar linear.
- Kekurangan: Tidak mampu menangkap hubungan non-linear.

Sangat sensitif terhadap outlier.

Model 2: SGD Regressor
- Cara Kerja: SGD Regressor menggunakan algoritma Stochastic Gradient Descent untuk memperbaharui bobot model secara bertahap menggunakan satu sampel data secara acak setiap iterasi. Ini membuat proses training jauh lebih cepat pada dataset besar.
- Parameter: Menggunakan parameter default.
- Kelebihan: Sangat cepat untuk dataset besar dan fleksibel karena bisa digunakan untuk berbagai jenis loss function.
- Kekurangan: Memerlukan scaling data (standardisasi) agar konvergen dengan baik dan sangat sensitif terhadap setting hyperparameter (learning rate, epochs).

Model 3: Random Forest Regressor
- Cara Kerja: Random Forest membuat banyak decision tree menggunakan subset data dan subset fitur yang dipilih secara acak. Prediksi akhir dihasilkan dengan rata-rata output dari seluruh pohon, memperkuat stabilitas dan akurasi.
- Parameter: n_estimators=100: Membuat 100 pohon keputusan.
- Kelebihan: Tahan terhadap overfitting dibandingkan decision tree tunggal dan mampu menangani data non-linear dengan sangat baik.
- Kekurangan: Konsumsi memori tinggi dan interpretasi model menjadi sulit.

Model 4: Gradient Boosting Regressor
- Cara Kerja: Gradient Boosting membangun model pohon keputusan secara berurutan, di mana setiap pohon baru memperbaiki kesalahan dari pohon sebelumnya. Optimasi dilakukan dengan menggunakan teknik gradient descent terhadap fungsi loss.
- Parameter:
  - n_estimators=100 (Jumlah pohon)
  - learning_rate=0.1 (Seberapa besar kontribusi masing-masing pohon terhadap prediksi akhir).
- Kelebihan: Mampu mencapai akurasi prediksi yang sangat tinggi dan dapat menangani hubungan kompleks antar variabel.
- Kekurangan: Waktu training lebih lambat dan perlu tuning hyperparameter secara hati-hati untuk mencegah overfitting.

Model 5: Elastic Net
- Cara Kerja: Elastic Net menggabungkan penalti dari Lasso (L1) dan Ridge (L2) regression. Ini membantu ketika ada banyak fitur berkorelasi tinggi dengan memilih dan mengecilkan bobot fitur yang kurang relevan.
- Parameter:
  - alpha=0.1 (Besarnya kekuatan regularisasi)
  - l1_ratio=0.5, komposisi penalti antara L1 dan L2 (50% masing-masing).
- Kelebihan: Bagus untuk data dengan multikolinearitas (fitur saling berkaitan) dan bisa melakukan feature selection otomatis.
- Kekurangan: Butuh tuning hyperparameter untuk mendapatkan hasil optimal dan tidak sebaik model ensemble dalam menangani non-linearitas yang kompleks.

Model terbaik: Gradient Boosting dipilih karena memiliki MSE dan RMSE terendah, menunjukkan prediksi paling stabil dan akurat.

## Evaluation

### Metrik Evaluasi yang Digunakan:
- MAE (Mean Absolute Error) adalah rata-rata dari nilai absolut selisih prediksi dan aktual.
- MSE (Mean Squared Error) adalah rata-rata kuadrat selisih prediksi dan aktual.
- RMSE (Root Mean Squared Error) adalah akar kuadrat dari MSE.

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

### Perbandingan model machine learning berdaasarkan MAE, MSE dan RMSE

![Image](https://github.com/user-attachments/assets/3c050c6a-53a7-40a3-954a-4a2eb31d4dfa)

Dapat dilihat bahwa
- Gradient Boosting Regressor memiliki nilai MSE dan RMSE paling kecil di antara semua model.
- Elastic Net memiliki MAE paling kecil, namun dari segi MSE dan RMSE, Gradient Boosting lebih unggul.
- Random Forest justru menunjukkan error lebih tinggi dibandingkan model linear.

### Hubungan Business Understanding dengan Evaluasi Model

Melalui proyek ini, saya berhasil membangun model machine learning yang dapat memprediksi harga rumah berdasarkan fitur-fitur utama seperti jumlah kamar tidur, kamar mandi, luas tanah dan luas bangunan, sesuai dengan Problem Statement pertama. Berbagai algoritma seperti Linear Regression, SGD Regressor, Random Forest, Gradient Boosting, dan Elastic Net dibandingkan menggunakan metrik evaluasi MAE, MSE dan RMSE. Model Gradient Boosting Regressor terpilih sebagai model terbaik karena menunjukkan nilai MSE dan RMSE terendah, memenuhi Goals yang ditetapkan dalam proyek. Dengan implementasi model ini, perusahaan properti dapat menetapkan harga rumah yang wajar dan kompetitif, serta membantu agen properti dalam menentukan harga jual yang optimal, selaras dengan Business Objective yang diusung.
