# Primetrade.ai - Assignment 1: Trader Analysis

This repository contains the completion of the required data analysis, behavioral clustering, and predictive modeling based on historic trader data and the Fear & Greed index.

## Folder Structure

The directory contains exactly the deliverables requested:
1. `datasets/`
   - `historical_data.csv`
   - `fear_greed_index.csv`
2. `assignment_analysis_final.ipynb`
   - A single, structured Jupyter Notebook containing all required elements, code, outputs, and analysis for Parts A, B, and C.
3. `app.py`
   - A lightweight Streamlit dashboard to interactively explore trader segments, sentiment distributions, and the Random Forest classification model context. 
4. `outputs/`
   - A folder holding the generated charts (`.png`) and resulting structured data (`.csv`) which powers the dashboard and represents the evidence for the write-up.
5. `writeup.md`
   - A short (max 1-page) summary of methodology, extracted insights, and the actionable strategy recommendations.
6. `README.md`
   - You are reading it now! Setup and deployment instructions below.

## Setup & How to Run

### Prerequisites
You will need **Python 3.8+** installed.
You also need to ensure the 2 datasets are available in dataserts folder, to ruin the code.I am unable to attach history_data.csv becuase of its huge size.

### 1. Install Dependencies
Install the required packages utilizing pip from the command line:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit jupyter
```

### 2. View The Analysis
Open the Jupyter Notebook to walk through the detailed analysis line-by-line:
```bash
jupyter notebook assignment_analysis_final.ipynb
```
The notebook is pre-generated with insights. You can restart the kernel and run all cells to verify the results or produce new data artifacts directly in the `outputs/` folder.

### 3. Launch the Dashboard
The Streamlit app dynamically loads the metrics and charts created by the notebook. To explore the results, run:
```bash
python -m streamlit run app.py
```
This spawns a local web server (typically `http://localhost:8501`) mapping the distributions of trader clusters, predicting their capability, and showing market sentiment correlations beautifully.

