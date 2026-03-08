import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

st.set_page_config(page_title="Trader Analysis Dashboard", layout="wide")

st.title("Trader Behavior Analysis & Predictive Modeling")
st.markdown("This dashboard explores trader behavioral archetypes, segments based on trade metrics, and the performance of our predictive model for next-day profitability.")

# Load Data
@st.cache_data
def load_data():
    trader_metrics = pd.read_csv('outputs/trader_metrics.csv')
    model_data = pd.read_csv('outputs/model_data.csv')
    predictions = pd.read_csv('outputs/predictions.csv')
    return trader_metrics, model_data, predictions

try:
    trader_metrics, model_data, predictions = load_data()
except FileNotFoundError:
    st.error("Data files not found in outputs/ directory. Please run the notebook or generate script first.")
    st.stop()

tab1, tab2, tab3 = st.tabs(["Trader Segments & Archetypes", "Sentiment Impact", "Predictive Modeling Highlights"])

with tab1:
    st.header("Trader Archetypes & Segments (Clustering & Rules)")
    st.markdown("Traders are grouped into predefined **Segments** (by median stats) and K-Means **Archetypes**.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Archetype Distribution")
        st.bar_chart(trader_metrics['Archetype'].value_counts())
    with col2:
        st.subheader("Segmentation Count")
        st.dataframe(trader_metrics.groupby(['Lev_Segment', 'Freq_Segment'])['Account'].count().unstack())
        
    st.subheader("Clustering: Trade Size vs Total Trades")
    try:
        img = Image.open('outputs/clustering_archetypes.png')
        st.image(img, use_container_width=True)
    except:
        st.info("Clustering image missing.")

with tab2:
    st.header("Sentiment Impact on Market")
    st.markdown("How differing levels of Fear and Greed visually correlate with overall trading performance in our dataset.")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Performance vs Sentiment")
        try:
            img_ps = Image.open('outputs/performance_vs_sentiment.png')
            st.image(img_ps, use_container_width=True)
        except:
            st.info("Performance vs Sentiment image missing.")
    with col2:
        st.subheader("Segments Distribution")
        try:
            img_ts = Image.open('outputs/trader_segments.png')
            st.image(img_ts, use_container_width=True)
        except:
            st.info("Segment distribution image missing.")

with tab3:
    st.header("Predictive Modeling: Next-Day Profitability")
    st.markdown("Predictive classifier (Random Forest) estimating whether a trader's next day will result in Profit, Loss, or Neutral based on behavior features.")
    
    colA, colB = st.columns(2)
    with colA:
        st.subheader("Feature Importance")
        try:
            img_fi = Image.open('outputs/predictive_features.png')
            st.image(img_fi, use_container_width=True)
        except:
            st.info("Feature importance image missing.")
            
    with colB:
        st.subheader("Model Validation")
        ct = pd.crosstab(predictions['Actual'], predictions['Predicted'], margins=True)
        st.dataframe(ct)
        accuracy = (predictions['Actual'] == predictions['Predicted']).mean()
        st.metric("Test Context Accuracy", f"{accuracy:.2%}")
