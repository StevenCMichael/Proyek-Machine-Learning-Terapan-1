# Laporan Proyek Machine Learning - Nama Anda

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

Pada bagian ini, Anda perlu menjelaskan proses klarifikasi masalah.

Bagian laporan ini mencakup:

### Problem Statements

Menjelaskan pernyataan masalah:
- Bagaimana cara mengidentifikasi preferensi pengguna terhadap buku berdasarkan data rating?
- Bagaimana memprediksi buku mana yang kemungkinan besar akan disukai oleh pengguna namun belum pernah dibaca?

### Goals

Menjelaskan tujuan proyek yang menjawab pernyataan masalah:
- Menggunakan data rating pengguna untuk membangun profil preferensi yang merepresentasikan minat bacaan mereka.
- Menghasilkan daftar rekomendasi buku yang relevan, dengan mempertimbangkan kemiripan preferensi pengguna lain.
 

### Solution statements
- Mengajukan 2 solution approach yaitu model RecommenderNet dan NCF.
- Membangdingkan kedua model menggunakan metrik RMSE dan memilih model yang terbaik

## Data Understanding
Dataset yang digunakan dalam proyek ini bersumber dari [Kaggle Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset), yang terdiri dari tiga tabel utama: books.csv, ratings.csv, dan users.csv. Namun, untuk keperluan proyek ini, hanya tabel books dan ratings yang digunakan.

Variabel-variabel pada tabel books adalah sebagai berikut:
- ISBN: Nomor unik yang mengidentifikasi setiap buku.
- Book-Title: Judul buku.
- Book-Author: Nama penulis buku.
- Year-Of-Publication: Tahun penerbitan.
- Publisher: Nama penerbit.
- Image-URL-S, Image-URL-M, Image-URL-L: URL gambar sampul buku dalam tiga ukuran berbeda.

Kondisi Data:
- Jumlah buku: 242.135
- Jumlah penulis: 102.023
- Jumlah pengguna: 105.283
- Dataset masih dalam kondisi mentah dan mengandung beberapa nilai null, namun tidak ditemukan duplikasi data.
- Nilai rating berkisar dari 0 hingga 10, di mana 0 menunjukkan bahwa pengguna tidak memberikan rating eksplisit.
  
Eksplatory Data
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

RecommenderNet adalah model rekomendasi berbasis arsitektur klasik embedding matrix yang diperkuat dengan penambahan bias pada level pengguna dan item. Model ini melakukan prediksi rating melalui perhitungan dot product antara vektor pengguna dan vektor buku.

Arsitektur Singkat:
- Embedding untuk pengguna dan buku, masing-masing berukuran 50.
- Bias terpisah untuk pengguna dan buku.
- Aktivasi sigmoid untuk membatasi prediksi dalam rentang [0,1].

Kelebihan:
- Sederhana dan cepat dilatih, cocok untuk dataset besar.
- Memiliki interpretabilitas tinggi karena pendekatan matriks faktorisasi.

Kekurangan:
- Tidak mampu menangkap interaksi non-linear yang kompleks antara pengguna dan buku.
- Performa cenderung menurun bila data sangat sparse (banyak rating nol).

Top 10 rekomendasi buku berdasarkan model RecommenderNet
1. Harry Potter and the Sorcerer's Stone (Book 1)          
2. Harry Potter and the Goblet of Fire (Book 4)          
3. Harry Potter and the Order of the Phoenix (Boo...     
4. Harry Potter and the Prisoner of Azkaban (Book 3)     
5. Harry Potter and the Sorcerer's Stone (Harry P...     
6. To Kill a Mockingbird         
7. Harry Potter and the Chamber of Secrets (Book 2)      
8. The Fellowship of the Ring (The Lord of the Ri...     
9. The Hobbit : The Enchanting Prelude to The Lor...
10. Fahrenheit 451     

2. Neural Collaborative Filtering (NCF)

NCF adalah pendekatan yang menggabungkan embedding pengguna dan item ke dalam multilayer perceptron (MLP), memungkinkan model untuk mempelajari interaksi non-linear yang lebih kompleks antar fitur laten.

Arsitektur Singkat:
- Embedding dimensi 32 untuk pengguna dan buku.
- Jaringan MLP dengan dua hidden layer (64 dan 32 neuron).
- Aktivasi sigmoid di output layer.

Kelebihan:
- Mampu menangkap pola kompleks antara pengguna dan buku.
- Dapat diimprovisasi lebih lanjut dengan menambahkan side-feature (fitur tambahan pengguna atau buku).

Kekurangan:
- Lebih lambat dalam proses pelatihan dibanding model sederhana seperti RecommenderNet.
- Risiko overfitting lebih tinggi, terutama pada dataset kecil atau tidak seimbang.

Top 10 rekomendasi buku berdasarkan model NCF
1. Harry Potter and the Order of the Phoenix (Boo...          
2. The Hobbit : The Enchanting Prelude to The Lor...          
3. Harry Potter and the Goblet of Fire (Book 4)         
4. ANGELA'S ASHES         
5. Angels &amp; Demons    
6. To Kill a Mockingbird  
7. Harry Potter and the Sorcerer's Stone (Book 1)          
8. Nickel and Dimed: On (Not) Getting By in America        
9. The Lovely Bones: A Novel          
10. The Vampire Lestat (Vampire Chronicles, Book II)  

## Evaluation

Pada projek ini, model dievaluasi menggunakan RMSE (Root Mean Squared Error). RMSE (Root Mean Squared Error) adalah akar kuadrat dari rata-rata kuadrat selisih prediksi dan aktual.

- RMSE
  
  ![Image](https://github.com/user-attachments/assets/1929606c-571f-4a64-a8be-eb0f737cf188)

Contoh ara penggunaan RMSE

1. RecommenderNet
-Training RMSE: 0.3056
- Validation RMSE: 0.3839

Model RecommenderNet menunjukkan performa yang cukup stabil dengan perbedaan kecil antara error training dan validasi. Ini menunjukkan generalisasi yang baik meskipun model cukup sederhana.

2. Neural Collaborative Filtering (NCF)
- Training RMSE: 0.1052
- Validation RMSE: 0.4603

Meskipun model NCF mencapai RMSE training yang sangat rendah, nilai RMSE validasinya justru lebih tinggi dibanding RecommenderNet. Ini bisa menjadi indikasi awal adanya overfitting, di mana model belajar terlalu baik pada data latih tetapi kurang mampu menggeneralisasi pada data baru. Kesimpulannya adalah RecommenderNet lebih stabil dan cenderung lebih aman digunakan dalam konteks produksi atau real-user, karena error-nya lebih konsisten.

Ingatlah, metrik evaluasi yang digunakan harus sesuai dengan konteks data, problem statement, dan solusi yang diinginkan.

Misalkan terdapat data sebagai berikut

![Image](https://github.com/user-attachments/assets/320b67ed-b43c-4937-bb44-3f21177da9ae)

Langkah-langkah Perhitungan
1. Hitung selisih (error) untuk tiap rumah:

Error Rumah 1 = 500−520=−20 juta
Error Rumah 2 = 600−580=20 juta
Error Rumah 3 = 700−750=−50 juta

2. RMSE = akar dari ( (- 20)^2 + (20)^2 + (-50)^2 ) / 3 = akar dari  3300 / 3 =  akar dari 1100 = 33,17

**---Ini adalah bagian akhir laporan---**

_Catatan:_
- _Anda dapat menambahkan gambar, kode, atau tabel ke dalam laporan jika diperlukan. Temukan caranya pada contoh dokumen markdown di situs editor [Dillinger](https://dillinger.io/), [Github Guides: Mastering markdown](https://guides.github.com/features/mastering-markdown/), atau sumber lain di internet. Semangat!_
- Jika terdapat penjelasan yang harus menyertakan code snippet, tuliskan dengan sewajarnya. Tidak perlu menuliskan keseluruhan kode project, cukup bagian yang ingin dijelaskan saja.
