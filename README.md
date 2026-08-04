# 🎬 Movie Box Office Predictor

A machine learning web application for predicting movie box office revenue using **Streamlit** and **Scikit-learn**.

> **Role**
>
> Individual Project
>
> - Built an end-to-end machine learning pipeline
> - Performed data preprocessing and feature engineering
> - Compared multiple regression models
> - Developed and deployed an interactive Streamlit application

---

# 📖 About

This project predicts movie box office revenue based on production and release information.

Users can input movie-related features such as budget, genre, runtime, rating, and release year. The application first classifies the movie into a similar market segment using clustering, then predicts domestic box office revenue and estimates worldwide revenue.

The project focuses on building an end-to-end machine learning workflow, from data preprocessing and model training to web deployment.

---

# 🏗️ Architecture

```text
Movie Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
K-Means Clustering
      │
      ▼
Regression Model Training
      │
      ▼
North America Revenue Prediction
      │
      ▼
Worldwide Revenue Estimation
      │
      ▼
Streamlit Web Application
```

---

# ⚙️ Tech Stack

### AI & Machine Learning

- Scikit-learn
- XGBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Web

- Streamlit

### Language

- Python

---

# ✨ Key Features

## 🎭 Movie Classification

- Clustered movies with similar characteristics using K-Means
- Determined the optimal number of clusters with the Elbow Method
- Classified new movie inputs before prediction

## 💰 Revenue Prediction

- Compared multiple regression models including:
  - Linear Regression
  - Random Forest Regressor
  - XGBoost Regressor
- Selected the best-performing model based on validation performance

## 🌍 Worldwide Revenue Estimation

- Predicted North American box office revenue
- Estimated worldwide revenue using historical revenue ratios
- Used the median ratio to improve robustness against outliers

## 🌐 Interactive Web Service

- Built a Streamlit application for real-time prediction
- Organized the application into multiple pages including:
  - Home
  - EDA
  - Machine Learning
  - Statistics
  - Project Information

---

# 📂 Project Structure

```text
.
├── app.py
├── data/
├── image/
├── jupyter_notebook/
├── model/
├── ui/
├── requirements.txt
└── README.md
```

---

# 📚 What I Learned

This project provided practical experience in building a complete machine learning service rather than training a single model.

I learned how preprocessing, feature engineering, clustering, regression modeling, and deployment work together as one pipeline.

While comparing different regression algorithms, I realized that higher model complexity does not always produce better performance. Careful feature selection and appropriate preprocessing often had a greater impact than simply adopting more sophisticated models.

The experience also introduced me to deploying machine learning models as interactive web applications, which later became the foundation for my larger AI service projects.

---

# 🚀 Future Improvements

- Expand the training dataset with recent movie releases
- Introduce ensemble prediction models
- Improve feature engineering using additional metadata
- Deploy the application with Docker
- Build REST APIs for external integration

---

# 📊 Dataset

- Source: Kaggle Movie Dataset
- Includes production budget, genre, runtime, MPAA rating, release year, theater count, and box office revenue

---

# 🌐 Live Demo

Streamlit Application

https://movie-profit-app-codekookiz.streamlit.app/

---
