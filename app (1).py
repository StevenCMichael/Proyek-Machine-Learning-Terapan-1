import streamlit as st
import joblib
import pandas as pd
import numpy as np
import pandas as pd



df = pd.read_csv("cleaned.csv")

curricular_units_2nd_sem_approved = df["Curricular_units_2nd_sem_approved"].unique()
curricular_units_1st_sem_approved = df["Curricular_units_1st_sem_approved"].unique()
tuition_fees_up_to_date = df["Tuition_fees_up_to_date"].unique()
scholarship_holder = df["Scholarship_holder"].unique()
curricular_units_2nd_sem_enrolled = df["Curricular_units_2nd_sem_enrolled"].unique()
curricular_units_2nd_sem_evaluations = df["Curricular_units_2nd_sem_evaluations"].unique()
curricular_units_1st_sem_enrolled = df["Curricular_units_1st_sem_enrolled"].unique()
displaced = df["Displaced"].unique()

# preparing model
model = joblib.load(
    "model/student_dropout_model.joblib")

st.title("Klasifikasi Deteksi Potensi Dropout Siswa")
st.write("Sistem ini bertujuan untuk mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus pada Jaya Jaya Institut")

col_1, col_2 = st.columns(2)

with col_1:
    opt_curricular_units_1st_sem_approved = st.selectbox(
        "Jumlah satuan kurikulum yang disetujui pada semester pertama", np.sort(curricular_units_1st_sem_approved))
    opt_curricular_units_1st_sem_enrolled = st.selectbox(
        "Jumlah satuan mata kuliah yang diambil oleh mahasiswa pada semester pertama", np.sort(curricular_units_1st_sem_enrolled))
    opt_curricular_units_2st_sem_approved = st.selectbox(
        "Jumlah satuan kurikulum yang disetujui pada semester kedua", np.sort(curricular_units_2nd_sem_approved))
    opt_curricular_units_2nd_sem_enrolled = st.selectbox(
        "Jumlah satuan mata kuliah yang diambil oleh mahasiswa pada semester kedua", np.sort(curricular_units_2nd_sem_approved))
    opt_curricular_units_2nd_sem_evulations = st.selectbox(
        "Jumlah satuan kurikulum yang dievaluasi oleh mahasiswa pada semester kedua", np.sort(curricular_units_2nd_sem_evaluations))

with col_2:
    val_curricular_units_1st_grade = st.number_input(
        "Nilai rata-rata semester pertama", min_value=0, max_value=18)

    val_curricular_units_2nd_grade = st.number_input(
        "Nilai rata-rata semester kedua", min_value=0, max_value=18)
    
    opt_tuition_fees_up_to_date = st.radio("Biaya kuliah siswa sudah sesuai dengan yang berlaku", options=["Tidak Sesuai", "Sesuai"])

    opt_scholarship_holder = st.radio("Siswa memiliki beasiswa", options=["Tidak", "Ya"])

    opt_displaced = st.radio("Siswa merupakan orang terlantar", options=["Tidak", "Ya"])


with st.container():
    button_predict = st.button("Prediksi")


with st.container(border=True):
    if (button_predict):
        # inisilisasi dataframe baru
        predict_df = pd.DataFrame({
            "Curricular_units_2nd_sem_approved": opt_curricular_units_2st_sem_approved,
            "Curricular_units_2nd_sem_grade": val_curricular_units_2nd_grade,
            "Curricular_units_1st_sem_approved" : opt_curricular_units_1st_sem_approved,
            "Curricular_units_1st_sem_grade": val_curricular_units_1st_grade,
            "Tuition_fees_up_to_date": 0 if opt_tuition_fees_up_to_date == "Tidak Sesuai" else 1,
            "Scholarship_holder": 0 if opt_scholarship_holder == "Tidak" else 1,
            "Curricular_units_2nd_sem_enrolled": opt_curricular_units_2nd_sem_enrolled,
            "Curricular_units_1st_sem_enrolled": opt_curricular_units_1st_sem_enrolled,
            "Curricular_units_2nd_sem_evaluations": opt_curricular_units_2nd_sem_evulations,
            "Displaced": 0 if opt_displaced == "Tidak" else 1
        }, index=[0])



        # prediksi dengan model SVM
        predict = model.predict_proba(predict_df)
        predict_proba = model.predict_proba(predict_df)[0]
        predict_proba = [round(x*100, 2) for x in predict_proba]

        # penentuan kelas
        labels = ['Dropout', 'Tidak Dropout']
        probability_metrics = pd.DataFrame(
            {"Kelas": labels, "Probabilitas": predict_proba}, columns=["Kelas", "Probabilitas"])

        # tampilkan di web
        st.write(f"Prediksi : {labels[np.argmax(predict)]}")
        st.write("Probabilitas Setiap Kelas :")
        st.table(probability_metrics)
