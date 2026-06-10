# Machine Learning Prediction of Retro-Diels–Alder Reaction Outcomes

# Quick Links
  1. [Overview](#overview)
  2. [Repository Structure](#repository-structure)
  3. [Requirements](#requirements)
  4. [Citation](#citation)

## Overview
This repository contains the datasets, feature generation workflows, machine learning models, and analysis scripts used in the manuscript:

"Spacer-Driven Control of Mechanochemical Reactivity in Retro Diels-Alder Reactions: Insights from DFT and Machine Learning"

Mordred molecular descriptors derived from optimized reactant structures were used to construct datasets for predicting the feasibility of mechanochemical retro-Diels–Alder reactions. Multiple classification algorithms (Logistic Regression, SVM, Random Forest, XGBoost, and LightGBM) were trained and validated to identify the structural features governing mechanochemical reactivity. The pretrained models provided here enable reaction outcome prediction directly from the `.log` file of an optimized reactant molecule.

## Repository Structure
```
├── notebooks/                     # Google Colab notebooks for each model
│   ├── svm.ipynb            
│   ├── xgboost.ipynb           
│   ├── rf.ipynb
│   ├── light_gbm.ipynb           
│   └── logistic_regression.ipynb           
│  
├── dataset/
│   ├── raw               
│        └── MC_RDA_dataset.csv           
│   └── processed/                 
│        ├── X_train_final.csv
│        ├── X_test_final.csv
│        ├── y_train_final.csv
│        └── y_test_final.csv
│
└── README.md                     # Project documentation 
```

## Requirements
All required Python packages are 
To install them, run:
```
pip install -r requirements.txt
```
## Citation
