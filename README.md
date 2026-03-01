# 🎬 Predicting Movie Success Score using Machine Learning (0–100)

This project predicts a movie's success score (0–100) using machine learning models based on metadata and plot overview from the IMDb Top 1000 Movies dataset.

---

## 📌 Problem Statement
Movie success depends on multiple factors such as genre, director, cast, runtime, and audience engagement.  
The objective of this project is to build a regression model that predicts a movie’s success score using these features.

---

## 📂 Dataset
The dataset used in this project is the IMDb Top 1000 Movies dataset from Kaggle.

You can download it from:
https://www.kaggle.com/datasets/debanganghosh/imdb-dataset
After downloading, upload the CSV file to Google Colab before running the notebook.

Features used:
- Released Year  
- Runtime  
- Genre  
- Certificate  
- Director  
- Star1, Star2, Star3, Star4  
- Plot Overview  
- IMDb Votes  
- Gross Revenue  

Target Variable:
- Movie Success Score (scaled from IMDb rating to 0–100)

---

## ⚙️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- Google Colab  

---

## 🧠 Machine Learning Models
- Linear Regression  
- Random Forest Regressor  

---

## 🔄 Data Preprocessing
- Converted numeric columns to proper numeric format  
- Scaled numerical features using MinMaxScaler  
- Encoded categorical features using OneHotEncoder  
- Transformed plot overview using TF-IDF Vectorizer  
- Used ColumnTransformer and Pipeline for end-to-end processing  

---

## 📊 Evaluation Metrics
- Mean Absolute Error (MAE)  
- R² Score  

---

## 📈 Results
| Model | MAE | R² Score |
|------|-----|---------|
| Random Forest | ~3.22 | ~0.30 |
| Linear Regression | ~3.57 | ~0.31 |

Random Forest performed slightly better in terms of prediction error.

---

## 📉 Visualizations
- Distribution of target variable  
- Feature importance  
- Actual vs Predicted comparison  
- Error distribution  

---

## 🏁 Conclusion
The model is able to learn useful patterns from movie metadata and text features.  
Although perfect prediction is difficult due to the subjective nature of movie success, the model provides reasonable estimates.

---

## 🚀 Future Scope
- Use advanced ensemble models (XGBoost, LightGBM)  
- Add social media and review sentiment features  
- Apply deep learning for text understanding  

---

## ▶️ How to Run
1. Open the notebook in Google Colab  
2. Upload the dataset file  
3. Run all cells sequentially  

---

## 👤 Author
Vaibhav Gandhi
