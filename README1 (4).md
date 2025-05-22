# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah sebuah institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal luas karena kualitas lulusannya yang baik serta reputasinya yang kuat di dunia pendidikan. Selama bertahun-tahun, institusi ini telah berhasil melahirkan banyak alumni yang berprestasi dan berkontribusi nyata di masyarakat.

Namun, di balik keberhasilan tersebut, terdapat satu tantangan serius yang tidak bisa diabaikan—tingginya angka mahasiswa yang mengalami dropout atau tidak menyelesaikan pendidikan mereka. Fenomena ini tentu menjadi perhatian penting, bukan hanya dari sisi reputasi akademik, tapi juga dari sisi tanggung jawab sosial institusi terhadap para peserta didik.

Untuk mengatasi tantangan ini secara lebih proaktif, Jaya Jaya Institut ingin mengadopsi pendekatan berbasis data. Dengan memanfaatkan teknologi machine learning, institusi berharap dapat memprediksi lebih awal siapa saja siswa yang berisiko tinggi mengalami dropout. Harapannya, siswa tersebut bisa segera diberikan pendampingan atau bimbingan yang tepat sebelum terlambat.ng).

### Permasalahan Bisnis

Beberapa permasalahan bisnis yang ingin diselesaikan dalam proyek ini meliputi:
1. Tingginya tingkat dropout mahasiswa yang berdampak negatif pada reputasi institusi, efektivitas program akademik dan akreditasi perguruan tinggi secara keseluruhan.
2. Ketiadaan sistem deteksi dini berbasis data yang dapat membantu institusi mengidentifikasi mahasiswa berisiko tinggi untuk keluar sebelum hal tersebut terjadi.
3. Kurangnya alat visualisasi dan monitoring terpusat, sehingga tim akademik kesulitan melakukan pemantauan progres mahasiswa secara berkala dan mengambil tindakan intervensi secara sistematis.

### Cakupan Proyek

Proyek ini berfokus pada pengembangan sistem prediksi dropout mahasiswa di Jaya Jaya Institut, dengan tujuan utama membantu pihak institusi dalam mengambil langkah preventif secara lebih dini dan terukur. Adapun cakupan utama yang akan dikerjakan meliputi:

1. Eksplorasi dan Pemahaman Data

Melakukan analisis awal terhadap dataset yang disediakan untuk memahami struktur, kualitas, dan pola data siswa.

2. Pemilihan Fitur Kunci

Mengidentifikasi empat variabel paling berpengaruh terhadap risiko dropout, menggunakan pendekatan feature importance dari model machine learning.

3. Pembangunan Model Prediktif

Membangun model machine learning yang mampu memprediksi kemungkinan seorang siswa akan dropout atau tidak, berdasarkan data historis yang tersedia.

4. Pembuatan Dashboard Monitoring

Mendesain dan mengimplementasikan dashboard interaktif yang menyajikan insight dari keempat faktor utama, agar pihak kampus dapat memantau dan menindaklanjuti risiko dropout secara efisien.

5. Interpretasi dan Rekomendasi Strategis

Memberikan penjelasan dan saran berbasis data kepada manajemen, guna mendukung upaya pembinaan dan retensi mahasiswa secara berkelanjutan.

### Persiapan

Sumber data: [employee_data.csv](https://docs.google.com/spreadsheets/d/1HckF1BG0nwB1-E8VyyCY6xwRib2-KIlnA2LwmMrJ3Wc/edit?usp=sharing)

Setup environment:

Menginstall library yang diperlukan

```
pip install -r requirements.txt
```

Menjalankan app.py
```
streamlit run app.py
```

## Business Dashboard

Dashboard yang dikembangkan dalam proyek ini bertujuan untuk membantu tim akademik Jaya Jaya Institut dalam mengidentifikasi mahasiswa yang berpotensi dropout secara lebih dini dan berbasis data. Dengan tampilan yang interaktif dan mudah dipahami, dashboard ini menyajikan hubungan antara empat variabel kunci dan status kelulusan mahasiswa (dropout atau graduate).

Empat variabel yang divisualisasikan adalah:

1. Curricular Units 1st Semester (Approved)

Terlihat jelas bahwa mahasiswa yang menyelesaikan lebih sedikit mata kuliah pada semester pertama cenderung memiliki risiko dropout yang lebih tinggi. Semakin sedikit unit yang mereka selesaikan, semakin besar kemungkinan mereka tidak melanjutkan studi.

2. Curricular Units 2nd Semester (Approved)

Pola serupa terlihat di semester kedua. Mahasiswa dengan jumlah unit yang disetujui rendah pada semester ini juga memiliki kemungkinan besar untuk tidak menyelesaikan pendidikan mereka.

3. Curricular Units 1st Semester (Grade)

Dari sisi nilai, mahasiswa dropout menunjukkan distribusi nilai yang lebih rendah dan lebih bervariasi, dibandingkan dengan mahasiswa yang lulus, yang nilainya relatif lebih tinggi dan stabil.

4. Curricular Units 2nd Semester (Grade)

Nilai semester kedua juga menjadi indikator penting. Rata-rata nilai mahasiswa dropout cenderung lebih rendah dibandingkan dengan mereka yang berhasil lulus, dengan variasi yang juga lebih lebar.

Dashboard ini memungkinkan pihak institusi untuk memantau keempat indikator ini secara berkala, sehingga mahasiswa yang menunjukkan gejala “risiko tinggi” dapat segera diberikan perhatian khusus, seperti bimbingan akademik, konseling atau intervensi personal lainnya.



[link dashboard](https://lookerstudio.google.com/s/nySOftuM4F4)

[link streamlit](https://proyek-machine-learning-terapan-1-rzs7r3ink57xerr7xrfzjf.streamlit.app/)

## Conclusion

Melalui analisis data dan pengembangan model prediktif, proyek ini berhasil mengungkap sejumlah pola penting yang berkaitan dengan fenomena dropout di Jaya Jaya Institut. Model XGBoost yang digunakan dalam proses ini menunjukkan performa terbaik dibandingkan model lain seperti Random Forest dan Gradient Boosting meskipun selisihnya relatif tipis.

XGBoost unggul dalam hal akurasi, presisi dan F1-Score, serta memiliki jumlah false negative yang lebih sedikit. Ini berarti model ini lebih andal dalam mengidentifikasi mahasiswa yang benar-benar berisiko dropout, sehingga intervensi bisa dilakukan dengan lebih tepat sasaran.

Secara keseluruhan, proyek ini memberikan fondasi berbasis data yang kuat untuk mendukung kebijakan retensi mahasiswa. Dengan menggabungkan kekuatan model prediktif dan visualisasi dashboard, Jaya Jaya Institut kini memiliki alat yang tidak hanya mampu memetakan risiko, tapi juga mendorong langkah-langkah preventif yang lebih manusiawi dan berdampak.

### Rekomendasi Action Items (Optional)

Berdasarkan hasil analisis dan dashboard yang telah dibuat, berikut beberapa langkah strategis yang bisa diambil Jaya Jaya Maju untuk menekan angka attrition dan menciptakan lingkungan kerja yang lebih sehat serta berkelanjutan:

1. Sistem Pemantauan Akademik Dini

Buat mekanisme otomatis untuk mengidentifikasi mahasiswa yang:
- Menyelesaikan kurang dari 5 SKS di semester pertama atau kedua
- Memiliki nilai rata-rata di bawah ambang batas tertentu (misalnya <12)

2. Program Pendampingan Spesifik untuk Mahasiswa Risiko Tinggi

Sediakan program pembimbingan atau mentoring yang diarahkan secara khusus untuk mahasiswa yang terdeteksi berisiko. Fokusnya bukan pada pendekatan general, tapi berbasis data: personalisasi intervensi berdasarkan profil performa akademik mereka.

3. Audit Beban dan Struktur Mata Kuliah Semester Awal

Karena dua semester pertama sangat menentukan, penting untuk mengevaluasi apakah beban kurikulum dan desain mata kuliah terlalu berat, terlalu teknis, atau kurang memberi ruang adaptasi. Perlu ada keseimbangan antara standar akademik dan kesiapan mahasiswa baru.

4. Memakai dashboard sebagai alat bantu pemantauan mahasiswa

5. Menggunakan model atau streamlit untuk memprediksi kemungkinan dropout
