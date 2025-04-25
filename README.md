# 🌾 Crop Production Prediction

This project aims to **predict crop production (in tons)** based on key agricultural factors such as **area harvested (hectares)**, **yield (kg/ha)**, and **year**, using machine learning. The goal is to support **agricultural planning, food security, supply chain management**, and **agri-tech innovation** through data-driven insights.

---

## 📊 Project Overview

- **Domain:** Agriculture
- **Tech Stack:** Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit
- **Machine Learning Model:** Regression (Random Forest, Linear Regression, etc.)
- **Output:** Streamlit web app for real-time prediction

---

## 📁 Dataset

- Source: [FAOSTAT](https://www.fao.org/faostat/en/)
- Columns:
  - `Area`: Region/Country
  - `Item`: Crop Name
  - `Element`: Area harvested, Yield, or Production
  - `Year`: Year of observation
  - `Unit`: ha / kg/ha / tons
  - `Value`: Numeric value of measurement

---

## 📌 Problem Statement

Accurately predicting crop production is crucial for:
- Ensuring **food security**
- Enabling **policy decisions** for subsidies and crop insurance
- Supporting **agri-business planning**
- Empowering **farmers** with timely insights

---

## 🔧 Project Workflow

### 1. Data Cleaning & Preprocessing
- Handled missing values and duplicates
- Converted dataset into pivoted format with separate columns for `Area Harvested`, `Yield`, and `Production`
- Categorical encoding for `Area` and `Item`

### 2. Exploratory Data Analysis (EDA)
- Crop and region-wise distribution
- Yearly production and yield trends
- Correlation heatmaps
- Outlier detection using boxplots

### 3. Model Building
- Trained multiple regression models:
  - Linear Regression
  - Random Forest Regressor
- Evaluated with R², MAE, and MSE

### 4. Streamlit App
- User inputs:
  - Region (Area)
  - Crop (Item)
  - Year
  - Area Harvested (ha)
  - Yield (kg/ha)
- Outputs:
  - Predicted Production in tons

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/crop-production-prediction.git
cd crop-production-prediction
