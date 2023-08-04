# Student Performance Indicator - Exploratory Data Analysis and Model Training

This repository combines the Exploratory Data Analysis (EDA) and Model Training phases of a machine learning project aimed at understanding student performance indicators. The project explores how various factors influence student test scores and develops predictive models based on these attributes.

## Project Overview

The project is divided into two main parts:

1. **Exploratory Data Analysis (EDA)**: This phase focuses on understanding the dataset and the relationships between student attributes and their test scores.

2. **Model Training**: In this phase, machine learning models are developed and evaluated to predict student math scores based on the provided features.

## 1. Exploratory Data Analysis (EDA)

In this phase, the project aims to gain insights into the dataset and the factors affecting student performance.

### 1.1 Problem Statement

The primary objective is to analyze how factors like gender, ethnicity, parental level of education, lunch type, and test preparation course impact student test scores.

### 1.2 Data Collection

The dataset, obtained from Kaggle, consists of 8 columns and 1000 rows, containing student attributes and their corresponding test scores.

### 1.3 Data Checks and Pre-Processing

Several data checks and pre-processing steps are performed, including handling missing values, duplicates, and ensuring correct data types. Basic statistical analyses are also conducted.

### 1.4 Data Visualization

Visualizations are utilized to understand relationships between variables and student performance. These include histograms, KDE plots, violin plots, pie charts, and pair plots.

## 2. Model Training

This phase involves developing machine learning models to predict student math scores based on the dataset's attributes.

### 2.1 Model Building

Various regressors from scikit-learn, CatBoost, and XGBoost libraries are used to build predictive models. The best-performing model is chosen based on metrics like accuracy, precision, recall, and F1-score.

### 2.2 Model Evaluation

Model performance is evaluated using appropriate metrics, and effectiveness in predicting student math scores is assessed.

### 2.3 Model Comparison and Selection

Multiple regression models are trained and compared, including Linear Regression, Lasso Regression, Ridge Regression, K-Neighbors Regressor, Decision Tree Regressor, Random Forest Regressor, XGBoost Regressor, CatBoost Regressor, and AdaBoost Regressor. The Ridge Regression model is selected for deployment due to its accuracy.

### 2.4 Linear Regression Analysis

A dedicated analysis of the Linear Regression model is presented, including accuracy calculation and a scatter plot illustrating predicted scores against actual scores.

### 2.5 Model Deployment and Feature Importance

The selected Ridge Regression model is deployed and stored using the `joblib` library. Additionally, feature importance is analyzed, showcasing which attributes have the most impact on predicting student math scores.

## Conclusion

This comprehensive project delves into both the Exploratory Data Analysis and Model Training phases. Through data exploration and visualization, the project uncovers insights into factors influencing student performance. The developed machine learning models enhance understanding by predicting student math scores based on attributes. The repository's Jupyter notebooks provide detailed code implementation and insights for those interested in exploring student performance indicators.