import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

st.title("🎬 Movie Success Score Predictor")

st.write("Enter movie details to predict success score (0–100)")

# User inputs
released_year = st.number_input("Released Year", 1900, 2025, 2020)
runtime = st.number_input("Runtime (minutes)", 30, 300, 120)

genre = st.text_input("Genre", "Drama")
certificate = st.selectbox("Certificate", ["G", "PG", "PG-13", "R", "Not Rated"])
director = st.text_input("Director", "Christopher Nolan")

star1 = st.text_input("Star 1", "Actor 1")
star2 = st.text_input("Star 2", "Actor 2")
star3 = st.text_input("Star 3", "Actor 3")
star4 = st.text_input("Star 4", "Actor 4")

overview = st.text_area("Plot Overview", "A story about...")

votes = st.number_input("IMDB Votes", 0, 2000000, 50000)
gross = st.number_input("Gross Revenue", 0, 1000000000, 10000000)

if st.button("Predict"):
    input_df = pd.DataFrame([{
        "Released_Year": released_year,
        "Runtime": runtime,
        "Genre": genre,
        "Certificate": certificate,
        "Director": director,
        "Star1": star1,
        "Star2": star2,
        "Star3": star3,
        "Star4": star4,
        "Overview": overview,
        "No_of_Votes": votes,
        "Gross": gross
    }])

    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Movie Success Score: {prediction:.2f}")
