# Laporan Proyek Machine Learning - Steven C Michael

## Project Overview

Meningkatnya jumlah buku yang tersedia secara daring telah memberikan keuntungan besar bagi para pembaca, namun juga memunculkan tantangan dalam memilih buku yang benar-benar sesuai dengan minat individu. Dalam konteks ini, sistem rekomendasi menjadi alat penting yang mampu membantu pengguna menemukan bacaan yang relevan dan menarik. Salah satu pendekatan yang terbukti efektif dalam pengembangan sistem rekomendasi adalah collaborative filtering, sebuah teknik yang memanfaatkan kesamaan pola perilaku antar pengguna untuk memprediksi preferensi mereka di masa depan.

### Mengapa Proyek Ini Penting?

Industri penerbitan dan platform distribusi buku digital kini semakin bergantung pada personalisasi untuk mempertahankan pengguna dan meningkatkan engagement. Sistem rekomendasi yang akurat bukan hanya meningkatkan kepuasan pengguna, tetapi juga dapat mendorong penjualan dan loyalitas pelanggan. Tanpa sistem seperti ini, pengguna dapat merasa kewalahan oleh banyaknya pilihan, yang pada akhirnya bisa menurunkan minat baca.

Proyek ini bertujuan untuk mengembangkan sistem rekomendasi buku berbasis collaborative filtering yang mampu menyarankan buku-buku yang belum pernah dibaca namun kemungkinan besar disukai oleh pengguna, berdasarkan riwayat rating pengguna lain yang memiliki pola preferensi serupa. Dengan sistem ini, pengalaman pengguna dalam menjelajahi buku akan menjadi lebih personal, efisien, dan memuaskan.

Berikut adalah penelitan terdahulu yang menjadi referensi projek ini
- Razali, N.N.N., & Idrus, Z. (2024). Intelligence Book Recommendation System Using Collaborative Filtering. 5th International Conference on Information Technology and Security. 
- Mathew, P., Kuriakose, B., & Hegde, V. (2016). Book Recommendation System through Content Based and Collaborative Filtering Method. International Conference on Data Mining and Advanced Computing.
- Khalifeh, S., & Al-mousa, A. (2021). A Book Recommender System Using Collaborative Filtering Method. International Conference on Data Science, E-learning and Information Systems.
- Lutan, E.R., & Bădică, C. (2024). Literature Books Recommender System Using Collaborative Filtering and Multi-Source Reviews. 19th Conference on Computer Science and Intelligence Systems.

## Business Understanding

### Problem Statements
- Bagaimana cara membangun model prediksi rating buku yang akurat untuk meningkatkan kualitas sistem rekomendasi buku kepada pengguna?

### Goals
- Membangun model prediksi rating buku dengan error minimal.
- Menghasilkan model prediksi rating buku dengan nilai RMSE serendah mungkin (idealnya di bawah 0,3).


### Solution statements
- Mengajukan 2 solution approach yaitu model RecommenderNet dan NCF.
- Membangdingkan kedua model menggunakan metrik RMSE dan memilih model yang terbaik

## Data Understanding

- Link dataset
[Kaggle Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

### Dataset books

Jumlah Baris dan Kolom tabel books
- Jumlah baris: 271.360
- Jumlah kolom: 8

Variabel-variabel pada tabel books adalah sebagai berikut:
- ISBN: Nomor unik yang mengidentifikasi setiap buku.
- Book-Title: Judul buku.
- Book-Author: Nama penulis buku.
- Year-Of-Publication: Tahun penerbitan.
- Publisher: Nama penerbit.
- Image-URL-S, Image-URL-M, Image-URL-L: URL gambar sampul buku dalam tiga ukuran berbeda.

Kondisi tabel books sebagai berikut:
- Missing Values:
  - Book-Author: 2 nilai kosong
  - Publisher: 2 nilai kosong
  - Image-URL-L: 3 nilai kosong
  - Kolom lain tidak memiliki missing value.
- Data Duplikat: 0 duplikat terdeteksi.

### Dataset rating

Jumlah Baris dan Kolom
- Jumlah baris: 1.149.780
- Jumlah kolom: 3

Kondisi Data
- Missing Values: Tidak ada nilai kosong.
- Data Duplikat: Tidak ditemukan duplikat.

Uraian Fitur
- User-ID: Identifikasi unik untuk pengguna.
- ISBN: Nomor unik untuk identifikasi buku yang dirating.
- Book-Rating: Nilai rating yang diberikan pengguna terhadap buku (rentang 0-10, dengan 0 berarti tidak memberikan rating eksplisit).

### Eksploratory Analisis
- Jumlah buku: 242.135
- Jumlah penulis: 102.023
- Jumlah pengguna: 105.283
  
- Top 10 Author dengan buku terbanyak
  
![Image](https://github.com/user-attachments/assets/64722f7c-63a0-4c9a-97d6-47be21529921)

Penulis dengan jumlah buku terbanyak di dataset ini antara lain Agatha Christie (632 buku) dan William Shakespeare (567 buku).

- Top 10 Publisher dengan buku terbanyak
  
![Image](https://github.com/user-attachments/assets/898a6750-e87b-4499-ac8a-875f1d2e8d85)

Publisher dengan jumlah buku terbanyak di dataset ini antara lain Harlequin (7535 buku) dan Silhouette (4220 buku).

- Jumlah per rating

![Image](https://github.com/user-attachments/assets/83a790fd-101f-4a89-9ddd-33691e1ab544)

Masih banyak pengguna yang tidak memberi rating 

## Data Preparation
Tahapan data preparation dilakukan untuk memastikan bahwa data dalam kondisi siap pakai bagi model rekomendasi. Berikut langkah-langkah yang dilakukan secara berurutan:

1. Penggabungan Tabel:
- Menggabungkan books dan ratings berdasarkan kolom ISBN untuk mendapatkan detail buku bersamaan dengan rating.

2. Penggantian Nama Kolom:
- Kolom Book-Rating diganti menjadi rating untuk keseragaman dan kemudahan saat proses modeling.

3. Penghapusan Kolom Tidak Relevan:
- Kolom seperti Year-Of-Publication, Image-URL-S, Image-URL-M, Image-URL-L, Book-Author, ISBN, dan Publisher dihapus karena tidak berpengaruh langsung pada prediksi rating dan hanya menambah beban memori.

4. Pembersihan Data:
- Menghapus entri dengan nilai null agar menjaga kualitas data tersisa dan mencegah bias prediksi.
- Mengonfirmasi tidak ada duplikasi yang untuk mencegah pembelajaran berulang dari data yang sama.

5. Menghapus rating 0
- Rating 0 bukan berarti pengguna tidak menyukai buku tersebut namun pengguna tidak me-review buku tersebut sehingga jika rating 0 dianggap sebagai input yang sah, model bisa belajar dari noise, yakni data yang sebenarnya tidak memiliki makna evaluatif. Ini bisa membuat sistem rekomendasi merekomendasikan buku yang sebenarnya tidak pernah dinilai secara jujur oleh pengguna.

5. Filter Buku Populer:
- Memilih 150 buku dengan jumlah rating terbanyak agar proses pelatihan model tidak memakan memori berlebih. Ini juga membantu dalam menyaring item-item yang memang populer secara umum.

6. Encoding Identitas:
- Melakukan encoding pada User-ID dan Book-Title menjadi bentuk numerik agar bisa diterima oleh algoritma rekomendasi.

7. Pemetaan ID ke Nama:
- Menyimpan mapping dari user ke User-ID dan buku ke Book-Title agar dapat digunakan kembali pada saat prediksi dan interpretasi hasil.

8. Train-Test Split:
- Membagi dataset menjadi 80% data latih dan 20% data uji untuk memastikan generalisasi model terhadap data baru.

## Modeling
Dalam proyek ini, dua pendekatan sistem rekomendasi berbasis deep learning digunakan yaitu RecommenderNet dan Neural Collaborative Filtering (NCF). Keduanya dikembangkan menggunakan framework TensorFlow dan Keras. Kedua model memanfaatkan teknik embedding untuk merepresentasikan relasi laten antara pengguna dan buku berdasarkan data rating historis.

1. RecommenderNet

#### Cara Kerja Model

RecommenderNet mengadopsi pendekatan matrix factorization, di mana baik pengguna maupun buku direpresentasikan sebagai vektor embedding berdimensi tetap. Prediksi rating diperoleh dari hasil dot product antara vektor pengguna dan buku, ditambah dengan bias masing-masing entitas, lalu diaktivasi menggunakan fungsi sigmoid agar hasil prediksi berada dalam rentang 0–1.

- Embedding Layer: Mengubah ID pengguna dan buku menjadi vektor berdimensi 50.
- Bias Embedding: Menambahkan bias khusus untuk setiap pengguna dan buku.
- Dot Product: Mengukur tingkat kecocokan antara pengguna dan buku.
- Output Sigmoid: Mengubah hasil akhir menjadi skor prediksi antara 0 dan 1.

#### Arsitektur Singkat:
- Embedding untuk pengguna dan buku, masing-masing berukuran 50.
- Bias terpisah untuk pengguna dan buku.
- Aktivasi sigmoid untuk membatasi prediksi dalam rentang [0,1].

#### Kelebihan:
- Sederhana dan cepat dilatih, cocok untuk dataset besar.
- Memiliki interpretabilitas tinggi karena pendekatan matriks faktorisasi.

#### Kekurangan:
- Tidak mampu menangkap interaksi non-linear yang kompleks antara pengguna dan buku.
- Performa cenderung menurun bila data sangat sparse (banyak rating nol).

#### Top 10 rekomendasi buku berdasarkan model RecommenderNet
1. Harry Potter and the Sorcerer's Stone (Book 1)  
2. Harry Potter and the Prisoner of Azkaban (Book 3)  
3. Ender's Game (Ender Wiggins Saga (Paperback))  
4. To Kill a Mockingbird  
5. The Two Towers (The Lord of the Rings, Part 2)  
6. The Hobbit : The Enchanting Prelude to The Lord of the Rings  
7. Fried Green Tomatoes at the Whistle Stop Cafe  
8. Seabiscuit: An American Legend  
9. Harry Potter and the Goblet of Fire (Book 4)  
10. Harry Potter and the Order of the Phoenix (Book 5)  

2. Neural Collaborative Filtering (NCF)

#### Cara Kerja Model

NCF memperluas pendekatan matrix factorization dengan menambahkan Multilayer Perceptron (MLP) untuk menangkap hubungan non-linear antara pengguna dan item. Alih-alih dot product, vektor pengguna dan buku digabung lalu diproses oleh beberapa layer dense.

- Embedding Layer: Mengubah ID pengguna dan buku menjadi vektor berdimensi 50.
- Concatenation: Vektor pengguna dan buku digabung (bukan dikalikan).
- MLP Layer: Dua hidden layer digunakan untuk menemukan pola kompleks.
- Output Sigmoid: Hasil akhir berupa skor kemungkinan preferensi.

#### Arsitektur Singkat:
- Embedding dimensi 32 untuk pengguna dan buku.
- Jaringan MLP dengan dua hidden layer (64 dan 32 neuron).
- Aktivasi sigmoid di output layer.

#### Kelebihan:
- Mampu menangkap pola kompleks antara pengguna dan buku.
- Dapat diimprovisasi lebih lanjut dengan menambahkan side-feature (fitur tambahan pengguna atau buku).

#### Kekurangan:
- Lebih lambat dalam proses pelatihan dibanding model sederhana seperti RecommenderNet.
- Risiko overfitting lebih tinggi, terutama pada dataset kecil atau tidak seimbang.

#### Top 10 rekomendasi buku berdasarkan model NCF
1. The Two Towers (The Lord of the Rings, Part 2)  
2. To Kill a Mockingbird  
3. The Hobbit : The Enchanting Prelude to The Lord of the Rings  
4. Ender's Game (Ender Wiggins Saga (Paperback))  
5. The Fellowship of the Ring (The Lord of the Rings, Part 1)  
6. Into Thin Air : A Personal Account of the Mt. Everest Disaster  
7. Harry Potter and the Sorcerer's Stone (Book 1)  
8. Harry Potter and the Prisoner of Azkaban (Book 3)  
9. Harry Potter and the Goblet of Fire (Book 4)  
10. The Catcher in the Rye   

## Evaluation

Pada projek ini, model dievaluasi menggunakan RMSE (Root Mean Squared Error). RMSE (Root Mean Squared Error) adalah akar kuadrat dari rata-rata kuadrat selisih prediksi dan aktual.

### Contoh cara kerja RMSE
Misalkan terdapat data sebagai berikut

![Image](https://github.com/user-attachments/assets/320b67ed-b43c-4937-bb44-3f21177da9ae)

#### Langkah-langkah Perhitungan
1. Hitung selisih (error) untuk tiap rumah:

Error Rumah 1 = 500−520=−20 juta
Error Rumah 2 = 600−580=20 juta
Error Rumah 3 = 700−750=−50 juta

2. RMSE = akar dari ( (- 20)^2 + (20)^2 + (-50)^2 ) / 3 = akar dari 3300 / 3 = 1100

- RMSE
  
  ![Image](https://github.com/user-attachments/assets/1929606c-571f-4a64-a8be-eb0f737cf188)

### Evaluasi Model

1. RecommenderNet
- Training RMSE: 0.1341
- Validation RMSE: 0.1903

![Image](https://github.com/user-attachments/assets/44f2bab5-fcee-4607-88a0-1b8f0b7ec421)

Model RecommenderNet menunjukkan performa yang cukup stabil dengan perbedaan kecil antara error training dan validasi. Ini menunjukkan generalisasi yang baik meskipun model cukup sederhana.

2. Neural Collaborative Filtering (NCF)
- Training RMSE: 0.0462
- Validation RMSE: 0.2060

![Image](https://github.com/user-attachments/assets/389b3a7f-7b2d-4208-bc66-0ffaf2989551)

Meskipun model NCF mencapai RMSE training yang sangat rendah, nilai RMSE validasinya justru lebih tinggi dibanding RecommenderNet. Ini bisa menjadi indikasi awal adanya overfitting, di mana model belajar terlalu baik pada data latih tetapi kurang mampu menggeneralisasi pada data baru. Kesimpulannya adalah RecommenderNet lebih stabil dan cenderung lebih aman digunakan dalam konteks produksi atau real-user, karena error-nya lebih konsisten.

#### Evaluasi dan hubungan Business Understanding
Nilai ini menunjukkan bahwa model memiliki tingkat error yang cukup rendah dalam memprediksi rating buku, sehingga mampu menjawab problem statement yaitu meningkatkan relevansi rekomendasi buku. Pencapaian nilai RMSE ini juga memenuhi goal awal proyek yaitu dibawah 0,3, sehingga model prediksi cukup akurat untuk meningkatkan pengalaman pengguna. Dengan model ini,  sistem rekomendasi dapat memberikan saran buku yang lebih relevan, yang pada akhirnya meningkatkan engagement pengguna.
