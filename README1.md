# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju adalah perusahaan multinasional yang telah berdiri sejak tahun 2000 dan kini memiliki lebih dari seribu karyawan yang tersebar di berbagai wilayah Indonesia. Sebagai perusahaan yang sudah mapan, Jaya Jaya Maju memiliki struktur organisasi yang kompleks dan dinamis. Namun, di balik pertumbuhan dan eksistensinya yang kuat, perusahaan menghadapi tantangan serius dalam aspek pengelolaan sumber daya manusia. Khususnya terkait dengan tingkat attrition yang tinggi yakni lebih dari 10%.

Attrition rate yang tinggi tidak hanya berdampak pada stabilitas operasional, tetapi juga dapat mempengaruhi efisiensi biaya, kontinuitas pengetahuan di dalam organisasi, serta moral karyawan yang tersisa. Untuk mengatasi isu ini secara lebih strategis, tim Human Resources (HR) merasa perlu memahami lebih dalam faktor-faktor apa saja yang mendorong keputusan karyawan untuk keluar dari perusahaan. Dengan kata lain, identifikasi penyebab utama attrition merupakan langkah krusial guna merancang kebijakan retensi yang lebih efektif.

Sebagai bagian dari upaya transformasi data-driven, HR Jaya Jaya Maju menginisiasi proyek analitik untuk mengolah data karyawan dan mengidentifikasi pola-pola yang dapat mengarah pada prediksi risiko attrition. Dalam konteks ini, teknologi seperti machine learning dan dashboard visual interaktif akan dimanfaatkan untuk mendukung pengambilan keputusan berbasis data (data-driven decision making).

### Permasalahan Bisnis

Beberapa permasalahan bisnis yang ingin diselesaikan dalam proyek ini meliputi:
1. Tingginya tingkat attrition karyawan (lebih dari 10%) yang dapat mengganggu stabilitas operasional perusahaan.
2. Ketiadaan sistem atau alat analitik yang dapat membantu HR dalam memahami dan memantau faktor-faktor penyebab karyawan keluar.
3. Kurangnya pemahaman berbasis data terkait karakteristik atau pola yang dimiliki karyawan yang cenderung resign.
4. Tidak adanya mekanisme prediktif yang dapat membantu HR dalam mengidentifikasi risiko attrition lebih awal.
5. Kebutuhan akan dashboard bisnis yang ringkas dan intuitif untuk memantau faktor-faktor utama penyebab attrition secara real-time.

### Cakupan Proyek

Proyek ini dirancang untuk menjawab kebutuhan manajer HR dalam memetakan dan memprediksi risiko attrition karyawan menggunakan pendekatan machine learning. Ruang lingkupnya mencakup:

1. Analisis Data Historis Karyawan
   
Menggunakan data internal yang telah disediakan oleh perusahaan, proses ini akan membantu menemukan pola-pola yang tersembunyi terkait perilaku dan karakteristik karyawan yang keluar.

2. Pemodelan Prediktif
   
Mengembangkan model machine learning yang mampu memprediksi apakah seorang karyawan berisiko keluar atau tidak, berdasarkan enam variabel utama yang dipilih dari hasil evaluasi feature importance.

3. Pembuatan Business Dashboard

Dashboard interaktif akan dikembangkan sebagai alat bantu visualisasi bagi tim HR untuk memonitor indikator-indikator utama secara real time. Tujuannya bukan hanya untuk melihat tren, tapi juga untuk mendeteksi potensi masalah sebelum terjadi.

4. Penyusunan Rekomendasi Strategis

Berdasarkan temuan model dan dashboard, proyek ini juga menyertakan rekomendasi konkret yang bisa diimplementasikan oleh perusahaan untuk meningkatkan retensi karyawan ke depannya.

### Persiapan

Sumber data: [employee_data.csv](https://docs.google.com/spreadsheets/d/1HckF1BG0nwB1-E8VyyCY6xwRib2-KIlnA2LwmMrJ3Wc/edit?usp=sharing)

Setup environment:

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV, cross_val_score
from imblearn.over_sampling import SMOTE
```

## Business Dashboard

Sebagai bagian dari upaya memahami dan mengelola tingkat attrition, sebuah dashboard interaktif telah dikembangkan untuk membantu tim HR memantau berbagai faktor kunci secara visual dan real-time. Dashboard ini bukan hanya menampilkan data mentah, tetapi menyajikan cerita—tentang siapa yang cenderung bertahan, siapa yang berisiko pergi, dan mengapa itu terjadi.

Enam faktor utama yang dipilih (berdasarkan model Random Forest) menjadi fokus utama dalam visualisasi. Melalui grafik dan diagram, pengguna dapat melihat pola-pola seperti:
1. Karyawan yang rutin lembur memiliki kecenderungan lebih tinggi untuk resign.
2. Mereka yang berada pada level stock option atau job level yang rendah tampak lebih tidak puas dan lebih sering keluar.
3. Karyawan yang merasa kurang puas terhadap lingkungan kerja maupun pekerjaannya cenderung lebih rentan untuk resign.
4. Karyawan dengan pengalaman kerja yang masih rendah juga menunjukkan potensi lebih tinggi untuk berpindah ke perusahaan lain.

Dashboard ini dirancang agar intuitif digunakan oleh manajer non-teknis, sehingga keputusan bisa diambil berdasarkan data yang mudah dicerna, bukan sekadar intuisi.

[link dashboard](https://lookerstudio.google.com/s/s0cTuODSUVo)

## Conclusion

Melalui analisis data dan pengembangan model prediktif, proyek ini berhasil mengidentifikasi faktor-faktor utama yang memengaruhi tingkat attrition karyawan di Jaya Jaya Maju. Dari berbagai algoritma yang diuji, model Random Forest menunjukkan performa terbaik. Meskipun selisihnya relatif kecil dibandingkan Gradient Boosting dan XGBoost. Random Forest unggul dalam hal akurasi, presisi, dan F1-Score. Serta menghasilkan jumlah false negative yang rendah, sebuah aspek penting dalam konteks prediksi attrition.

Faktor-faktor yang paling berpengaruh terhadap attrition meliputi aspek lembur, level opsi saham, level pekerjaan, kepuasan terhadap lingkungan dan pekerjaan, serta total pengalaman kerja. Temuan ini diperkuat dengan visualisasi dalam dashboard, yang menunjukkan tren serupa yaitu karyawan dengan beban kerja berat, kepuasan rendah, dan pengalaman kerja yang sedikit lebih berisiko untuk resign.

Secara keseluruhan, proyek ini memberikan dasar analitis yang kuat bagi HR untuk memahami dan mengantisipasi attrition, serta merancang strategi retensi yang lebih efektif dan terukur. Pemanfaatan model prediksi dan dashboard visual memungkinkan pengambilan keputusan yang lebih cepat, proaktif dan berbasis data nyata.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

Berdasarkan hasil analisis dan dashboard yang telah dibuat, berikut beberapa langkah strategis yang bisa diambil Jaya Jaya Maju untuk menekan angka attrition dan menciptakan lingkungan kerja yang lebih sehat serta berkelanjutan:

1. Tinjau dan Kelola Ulang Pola Lembur Karyawan

Salah satu temuan paling mencolok adalah tingginya tingkat attrition pada karyawan yang rutin bekerja lembur. Hal ini tidak hanya mengindikasikan ketidakseimbangan beban kerja, tapi juga potensi kelelahan mental. Perusahaan perlu:
  - Membatasi jam lembur mingguan secara ketat.
  - Memberikan cuti tambahan bagi karyawan yang secara konsisten lembur.
  - Melakukan monitoring dan evaluasi berkala pada divisi dengan tingkat lembur tertinggi.

2. Perbaiki Skema Kompensasi dan Penghargaan Karyawan Level Awal

Karyawan dengan stock option level dan job level rendah cenderung merasa tidak cukup dihargai. Untuk mengatasi ini, perusahaan bisa:
  - Menawarkan insentif non-finansial seperti pengakuan publik atau kesempatan pelatihan.
  - Memberikan opsi saham atau bonus tahunan sebagai bentuk apresiasi kontribusi.

3. Tingkatkan Kepuasan terhadap Lingkungan dan Budaya Kerja

Data menunjukkan bahwa lingkungan kerja yang kurang memuaskan menjadi salah satu pemicu utama attrition. Di luar faktor fisik, hal ini juga bisa mencerminkan budaya internal yang kurang suportif. Beberapa hal yang bisa dipertimbangkan:
  - Lakukan audit lingkungan kerja secara menyeluruh (fisik maupun psikologis)..
  - Bentuk tim budaya kerja yang bertugas menjaga semangat kolaboratif dan inklusif.

4. Rancang Program Pengembangan Karier yang Jelas dan Terukur

Karyawan, terutama yang masih di awal masa kerja, cenderung memiliki ekspektasi besar terhadap perkembangan karier. Ketika harapan ini tidak dikelola, mereka akan mudah tergoda untuk berpindah. Perusahaan sebaiknya:
  - Merancang jalur karier yang transparan sejak proses onboarding.
  - Menawarkan program mentoring bagi karyawan baru.
  - Menyediakan akses pelatihan teknis dan soft skill berbasis kebutuhan individu.

5. Lakukan Survei Kepuasan dan Exit Interview Secara Rutin

Melakukan survei berkala dan exit interview akan membantu perusahaan memahami tren yang muncul dan melakukan intervensi lebih cepat.
