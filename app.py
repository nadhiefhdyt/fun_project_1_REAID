import streamlit as st

# Setup awal session_state
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "show_score" not in st.session_state:
    st.session_state.show_score = False
if "score" not in st.session_state:
    st.session_state.score = 0

# Judul Aplikasi
st.title("🧠 Seberapa Cerdas Kamu Hari Ini?")

# Input Nama
name = st.text_input("Masukkan namamu dulu ya:")

# Tombol Mulai Quiz
if st.button("Mulai Quiz"):
    if name.strip() == "":
        st.warning("⚠️ Nama tidak boleh kosong. Yuk isi dulu namamu!")
    else:
        st.session_state.quiz_started = True
        st.session_state.show_score = False  # reset skor saat mulai ulang

# Tampilkan soal jika quiz dimulai
if st.session_state.quiz_started:
    st.subheader(f"Halo {name}, ayo mulai quiznya!")
    score = 0  # reset skor lokal

    # Soal 1
    st.subheader("1. Ibukota dari negara Thailand adalah...")
    q1 = st.radio("Pilih jawabanmu:", ['A. Hanoi', 'B. Manila', 'C. Bangkok', 'D. Kuala Lumpur'], key="q1")
    if q1 == 'C. Bangkok':
        score += 1

    # Soal 2
    st.subheader("2. Apa hasil dari 15 x 4?")
    q2 = st.radio("Pilih jawabanmu:", ['A. 60', 'B. 45', 'C. 54', 'D. 40'], key="q2")
    if q2 == 'A. 60':
        score += 1

    # Soal 3
    st.subheader("3. Siapa pencipta lagu kebangsaan Indonesia Raya?")
    q3 = st.radio("Pilih jawabanmu:", [
        'A. Ki Hajar Dewantara',
        'B. Wage Rudolf Supratman',
        'C. Soekarno',
        'D. Hatta'
    ], key="q3")
    if q3 == 'B. Wage Rudolf Supratman':
        score += 1

    # Tombol Submit Jawaban
    if st.button("Lihat Skor"):
        st.session_state.score = score
        st.session_state.show_score = True

# Menampilkan hasil skor jika tombol "Lihat Skor" sudah ditekan
if st.session_state.show_score:
    st.success(f"🎉 Skor kamu: {st.session_state.score}/3")

    if st.session_state.score == 3:
        st.balloons()
        st.subheader(f"Hebat {name}! Kamu menjawab semua dengan benar 🎓")
        st.image("animasi.gif")
    elif st.session_state.score == 2:
        st.subheader(f"Bagus {name}! Cuma satu yang salah ✨")
        st.image("animasi1.gif")
    else:
        st.subheader(f"Yuk belajar lagi {name}, semangat! 📘")
        st.image("animasi2.gif")
