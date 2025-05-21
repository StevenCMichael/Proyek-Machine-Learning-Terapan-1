import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Memuat model dan scaler
try:
    model = joblib.load('model_rf.joblib')
    scaler = joblib.load('scaler.joblib')
except FileNotFoundError as e:
    st.error(f"Error memuat file: {e}. Pastikan model_rf.joblib dan scaler.joblib ada.")
    st.stop()
except Exception as e:
    st.error(f"Error inisialisasi model atau scaler: {e}")
    st.stop()

st.title("Identifikasi Dini Risiko Mahasiswa Dropout")
st.write("Platform interaktif ini dirancang untuk membantu manajemen dan staf akademik Jaya Jaya Institut dalam mengidentifikasi mahasiswa yang memiliki potensi risiko untuk tidak melanjutkan studi (dropout) secara dini. Dengan memanfaatkan model prediktif berbasis data, sistem ini memungkinkan untuk mendukung keberhasilan studi mahasiswa")

# Menentukan rentang nilai untuk input numerik
min_value_generic = 0 
max_value_generic = 30 
min_grade = 0
max_grade = 18

col_1, col_2 = st.columns(2)
col_3, col_4 = st.columns(2) # Menambah kolom untuk menampung semua input

with col_1:
    st.header("Data Akademik Semester 1")
    opt_curricular_units_1st_sem_credited = st.slider("SKS Dikreditkan (Sem 1)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    opt_curricular_units_1st_sem_enrolled = st.slider("SKS Diambil (Sem 1)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    opt_curricular_units_1st_sem_evaluations = st.slider("Jumlah Evaluasi (Sem 1)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    opt_curricular_units_1st_sem_approved = st.slider("SKS Disetujui (Sem 1)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    val_curricular_units_1st_sem_grade = st.number_input("Nilai rata-rata (Sem 1)", min_value=float(min_grade), max_value=float(max_grade), value=0.0)
    opt_curricular_units_1st_sem_without_evaluations = st.slider("SKS Tanpa Evaluasi (Sem 1)", min_value=min_value_generic, max_value=max_value_generic, value=0)

with col_2:
    st.header("Data Akademik Semester 2")
    opt_curricular_units_2nd_sem_credited = st.slider("SKS Dikreditkan (Sem 2)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    opt_curricular_units_2nd_sem_enrolled = st.slider("SKS Diambil (Sem 2)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    opt_curricular_units_2nd_sem_evaluations = st.slider("Jumlah Evaluasi (Sem 2)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    opt_curricular_units_2nd_sem_approved = st.slider("SKS Disetujui (Sem 2)", min_value=min_value_generic, max_value=max_value_generic, value=0)
    val_curricular_units_2nd_sem_grade = st.number_input("Nilai rata-rata (Sem 2)", min_value=float(min_grade), max_value=float(max_grade), value=0.0)
    opt_curricular_units_2nd_sem_without_evaluations = st.slider("SKS Tanpa Evaluasi (Sem 2)", min_value=min_value_generic, max_value=max_value_generic, value=0)

with col_3: # Menggunakan kolom baru untuk input sisa fitur
    st.header("Informasi Umum")
    opt_daytime_evening_attendance = st.radio("Waktu Kuliah", options=["Siang", "Malam"], help="Pilih waktu kehadiran kuliah.")
    opt_scholarship_holder = st.radio("Memiliki Beasiswa", options=["Tidak", "Ya"], help="Apakah siswa memiliki beasiswa?")

with st.container():
    button_predict = st.button("Lakukan Prediksi")

with st.container(border=True):
    if button_predict:
        # Membuat DataFrame dengan SEMUA KOLOM yang digunakan oleh model Anda (yaitu, kolom di X)
        predict_data = {
            'Daytime_evening_attendance': [1 if opt_daytime_evening_attendance == "Siang" else 0], # Contoh encoding jika Daytime=1, Evening=0
            'Scholarship_holder': [0 if opt_scholarship_holder == "Tidak" else 1],
            'Curricular_units_1st_sem_credited': [opt_curricular_units_1st_sem_credited],
            'Curricular_units_1st_sem_enrolled': [opt_curricular_units_1st_sem_enrolled],
            'Curricular_units_1st_sem_evaluations': [opt_curricular_units_1st_sem_evaluations],
            'Curricular_units_1st_sem_approved': [opt_curricular_units_1st_sem_approved],
            'Curricular_units_1st_sem_grade': [val_curricular_units_1st_sem_grade],
            'Curricular_units_1st_sem_without_evaluations': [opt_curricular_units_1st_sem_without_evaluations],
            'Curricular_units_2nd_sem_credited': [opt_curricular_units_2nd_sem_credited],
            'Curricular_units_2nd_sem_enrolled': [opt_curricular_units_2nd_sem_enrolled],
            'Curricular_units_2nd_sem_evaluations': [opt_curricular_units_2nd_sem_evaluations],
            'Curricular_units_2nd_sem_approved': [opt_curricular_units_2nd_sem_approved],
            'Curricular_units_2nd_sem_grade': [val_curricular_units_2nd_sem_grade],
            'Curricular_units_2nd_sem_without_evaluations': [opt_curricular_units_2nd_sem_without_evaluations]
        }
        predict_df = pd.DataFrame(predict_data)

        # Urutan kolom yang benar (sesuai dengan X.columns di Colab)
        # Ini sangat penting untuk konsistensi dengan scaler dan model
        correct_column_order = [
            'Daytime_evening_attendance',
            'Scholarship_holder',
            'Curricular_units_1st_sem_credited',
            'Curricular_units_1st_sem_enrolled',
            'Curricular_units_1st_sem_evaluations',
            'Curricular_units_1st_sem_approved',
            'Curricular_units_1st_sem_grade',
            'Curricular_units_1st_sem_without_evaluations',
            'Curricular_units_2nd_sem_credited',
            'Curricular_units_2nd_sem_enrolled',
            'Curricular_units_2nd_sem_evaluations',
            'Curricular_units_2nd_sem_approved',
            'Curricular_units_2nd_sem_grade',
            'Curricular_units_2nd_sem_without_evaluations'
        ]

        # Memastikan DataFrame input memiliki kolom dan urutan yang benar
        try:
            predict_df = predict_df[correct_column_order]
        except KeyError as e:
             st.error(f"Error internal: Kolom yang dibutuhkan model tidak sesuai dengan input. Kolom hilang: {e}")
             st.stop()
        except Exception as e:
            st.error(f"Error saat mengatur urutan kolom: {e}")
            st.stop()


        # Menerapkan penskalaan pada data input menggunakan scaler yang dimuat
        try:
            predict_df_scaled = scaler.transform(predict_df)
        except Exception as e:
            st.error(f"Error saat menerapkan penskalaan: {e}. Pastikan scaler dimuat dengan benar dan data input memiliki format yang sesuai.")
            st.stop()


        # Melakukan prediksi probabilitas dan kelas menggunakan model yang dimuat
        try:
            predict_proba = model.predict_proba(predict_df_scaled)[0]
            predicted_class = model.predict(predict_df_scaled)[0]
        except Exception as e:
            st.error(f"Error saat melakukan prediksi: {e}. Pastikan model dimuat dengan benar dan data input sudah diskalakan.")
            st.stop()


        # Mengubah probabilitas menjadi persentase
        predict_proba_percentage = [round(x*100, 2) for x in predict_proba]
        # Menentukan label kelas (0: Dropout, 1: Graduate)
        labels = ['Dropout', 'Graduate']

        probability_metrics = pd.DataFrame(
            {"Kelas": labels, "Probabilitas": predict_proba_percentage}, columns=["Kelas", "Probabilitas"])

        # Menampilkan Hasil Prediksi
        st.subheader("Hasil Prediksi")
        st.write(f"Status diprediksi: **{labels[predicted_class]}**")
        st.write("Probabilitas Setiap Kelas :")
        st.table(probability_metrics)
