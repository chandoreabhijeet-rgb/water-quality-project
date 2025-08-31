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
