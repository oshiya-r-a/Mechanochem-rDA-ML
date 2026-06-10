# Machine Learning Prediction of Retro-Diels–Alder Reaction Outcomes

# Quick Links
  1. [Overview](#overview)
  2. [Repository Structure](#repository-structure)
  3. [Requirements](#requirements)
  4. [Citation](#citation)

## Overview
This repository contains the datasets, feature generation workflows, machine learning models, and analysis scripts used in the manuscript:

*"Spacer-Driven Control of Mechanochemical Reactivity in Retro Diels-Alder Reactions: Insights from DFT and Machine Learning"*

Mordred molecular descriptors derived from optimized reactant structures were used to construct datasets for predicting the feasibility of mechanochemical retro-Diels–Alder reactions. Multiple classification algorithms (Logistic Regression, SVM, Random Forest, XGBoost, and LightGBM) were trained and validated to identify the structural features governing mechanochemical reactivity. The pretrained models provided here enable reaction outcome prediction directly from the `.log` file of an optimized reactant molecule.

## Repository Structure
```
├── notebooks/                     # Google Colab notebooks for each model
│   ├── feature_extraction
│       ├── mordred_descriptors.ipynb 
│       └── mordred_environment.txt
│   ├── preprocessing
│       └── data_preprocessing.ipynb
│   └── models
│       ├── svm.ipynb                
│       ├── xgboost.ipynb           
│       ├── rf.ipynb
│       ├── light_gbm.ipynb           
│       └── logistic_regression.ipynb           
│  
├── dataset/
│   ├── raw               
│        └── MC_RDA_dataset.csv           
│   └── processed/                 
│        ├── X_train_final.csv
│        ├── X_test_final.csv
│        ├── y_train.csv
│        └── y_test.csv
│
└── README.md                     # Project documentation 
```

## Requirements
The Mordred descriptor generation workflow was developed using:

```
Python 3.1.1
NumPy 1.23.5
Open Babel 3.1.1
Mordred 1.2.0
pandas 2.3.1
RDKit 2023.03.3
pip 25.2
```

## Citation
