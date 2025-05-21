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
    st.error(f"Error inisialisasi: {e}")
    st.stop()

st.title("Klasifikasi Deteksi Potensi Dropout Siswa")
st.write("Sistem ini bertujuan untuk mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus pada Jaya Jaya Institut")

min_approved = 0
max_approved = 30
min_enrolled = 0
max_enrolled = 30
min_evaluations = 0
max_evaluations = 20
min_grade = 0
max_grade = 18

col_1, col_2 = st.columns(2)

with col_1:
    st.header("Data Akademik Semester 1 & 2")
    opt_curricular_units_1st_sem_approved = st.slider("Jumlah SKS yang disetujui (Semester 1)", min_value=min_approved, max_value=max_approved, value=0)
    opt_curricular_units_1st_sem_enrolled = st.slider("Jumlah SKS yang diambil (Semester 1)", min_value=min_enrolled, max_value=max_enrolled, value=0)
    opt_curricular_units_2st_sem_approved = st.slider("Jumlah SKS yang disetujui (Semester 2)", min_value=min_approved, max_value=max_approved, value=0)
    opt_curricular_units_2nd_sem_enrolled = st.slider("Jumlah SKS yang diambil (Semester 2)", min_value=min_enrolled, max_value=max_enrolled, value=0)
    opt_curricular_units_2nd_sem_evulations = st.slider("Jumlah Evaluasi (Semester 2)", min_value=min_evaluations, max_value=max_evaluations, value=0)

with col_2:
    st.header("Nilai & Informasi Tambahan")
    val_curricular_units_1st_grade = st.number_input("Nilai rata-rata (Semester 1)", min_value=float(min_grade), max_value=float(max_grade), value=0.0)
    val_curricular_units_2nd_grade = st.number_input("Nilai rata-rata (Semester 2)", min_value=float(min_grade), max_value=float(max_grade), value=0.0)
    opt_scholarship_holder = st.radio("Memiliki Beasiswa", options=["Tidak", "Ya"])

with st.container():
    button_predict = st.button("Lakukan Prediksi")

with st.container(border=True):
    if button_predict:
        predict_df = pd.DataFrame({
            "Curricular_units_2nd_sem_approved": [opt_curricular_units_2st_sem_approved],
            "Curricular_units_2nd_sem_grade": [val_curricular_units_2nd_grade],
            "Curricular_units_1st_sem_approved" : [opt_curricular_units_1st_sem_approved],
            "Curricular_units_1st_sem_grade": [val_curricular_units_1st_grade],
            "Scholarship_holder": [0 if opt_scholarship_holder == "Tidak" else 1],
            "Curricular_units_2nd_sem_enrolled": [opt_curricular_units_2nd_sem_enrolled],
            "Curricular_units_1st_sem_enrolled": [opt_curricular_units_1st_sem_enrolled],
            "Curricular_units_2nd_sem_evaluations": [opt_curricular_units_2nd_sem_evulations]
        })

        correct_column_order = [
            'Curricular_units_2nd_sem_approved',
            'Curricular_units_2nd_sem_grade',
            'Curricular_units_1st_sem_approved',
            'Curricular_units_1st_sem_grade',
            'Scholarship_holder',
            'Curricular_units_2nd_sem_enrolled',
            'Curricular_units_1st_sem_enrolled',
            'Curricular_units_2nd_sem_evaluations'
        ]
        try:
            predict_df = predict_df[correct_column_order]
        except KeyError as e:
             st.error(f"Error: Kolom tidak sesuai: {e}")
             st.stop()


        try:
            predict_df_scaled = scaler.transform(predict_df)
            predict_proba = model.predict_proba(predict_df_scaled)[0]
            predicted_class = model.predict(predict_df_scaled)[0]
        except Exception as e:
            st.error(f"Error prediksi: {e}")
            st.stop()


        predict_proba_percentage = [round(x*100, 2) for x in predict_proba]
        labels = ['Dropout', 'Graduate']

        probability_metrics = pd.DataFrame(
            {"Kelas": labels, "Probabilitas": predict_proba_percentage}, columns=["Kelas", "Probabilitas"])

        st.subheader("Hasil Prediksi")
        st.write(f"Status diprediksi: **{labels[predicted_class]}**")
        st.write("Probabilitas Setiap Kelas :")
        st.table(probability_metrics)
