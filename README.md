# Project - Water Quality Analysis

## 📌 Project Overview
This project is part of **Week 1 Assignment** under the theme **Environmental Monitoring and Pollution Control**.  
The focus of the project is on **Water Quality Analysis** using the *Water Potability Dataset*.

## 📂 Files in this Repository
- `Week1_Water_Quality.ipynb` → Jupyter Notebook containing code for data understanding.
- `water_potability.csv` → Dataset used for analysis.

## 🧪 Steps Performed
1. Imported required libraries (`pandas`, `numpy`).
2. Loaded dataset using `pandas`.
3. Performed data exploration:
   - `.info()` → Dataset information.
   - `.describe()` → Summary statistics.
   - `.isnull().sum()` → Checked for missing values.

## 📊 Dataset Details
The dataset contains measurements of water quality such as:
- pH
- Hardness
- Solids
- Chloramines
- Sulfate
- Conductivity
- Organic Carbon
- Trihalomethanes
- Turbidity  
Target column: **Potability** (1 = Safe to drink, 0 = Unsafe).

## 🚀 How to Run
1. Clone this repository.
2. Open `Week1_Water_Quality.ipynb` in Jupyter Notebook / Google Colab.
3. Make sure `water_potability.csv` is in the same folder.
4. Run all cells.

## ✅ Status
- Week 1 requirement completed (Data understanding only).
- Next steps: Data cleaning, visualization, and ML model (for coming weeks).
- week 2 model implemantation completed
- week 3 model successfully deployed

- 💧 Water Quality Analysis Project

Project Overview

This project predicts the potability of water using machine learning. Users can input water quality parameters to check if water is safe to drink.


---

Week 1 – Dataset & Problem Definition

1. Dataset Search: Found a dataset water_potability.csv containing water quality parameters.


2. Problem Statement: Predict whether water is potable (safe) or non-potable (unsafe) using machine learning.


3. Data Preparation:

Checked for missing values

Handled missing data by filling with median values

Removed duplicates

Explored dataset using statistics and graphs (distributions, correlation, target count)





---

Week 2 – Model Implementation

4. Model Selection: Random Forest Classifier chosen due to balanced accuracy and interpretability.


5. Model Training:

Features scaled using StandardScaler

Dataset split into training (80%) and testing (20%)

Model trained on training set



6. Evaluation:

Model accuracy computed on test set

Classification report generated for precision, recall, F1-score




Outcome: Model achieved good accuracy in predicting potable vs non-potable water.


---

Week 3 – Deployment

7. Deployment Process:

Model and scaler saved using pickle

Streamlit app created for user-friendly water potability prediction

Users can input water parameters and get instant prediction



8. Deliverables Checked:

Notebook includes complete workflow (data exploration, preprocessing, model, app code)

App code ready for demonstration or submission





---

Usage Instructions

1. Install dependencies:

pip install pandas numpy scikit-learn streamlit matplotlib seaborn


2. Run the training section to save model and scaler:

python train_model.py  # or run the notebook


3. Launch the Streamlit app:

streamlit run app.py




---
