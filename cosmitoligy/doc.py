import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data_s.csv")

df = load_data()
df.columns = df.columns.str.strip()

# Helper function to get key insight
def get_key_insight(series, label):
    counts = series.value_counts()
    if counts.empty:
        return f"No data available for {label}."
    top = counts.idxmax()
    top_count = counts.max()
    percent = (top_count / counts.sum()) * 100
    return f"**Key Insight:** The most common {label.lower()} is **{top}** ({top_count} respondents, {percent:.1f}%)."

# Title
st.title("Lakme Consumer Buying Behaviour Dashboard")

# Overview
st.header("Overview")
st.write("""
This dashboard presents key insights from a study conducted on 50 women to understand consumer buying behaviour towards Lakme cosmetic products.
""")

# Demographics
st.header("Demographic Insights")

st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.countplot(y=df['2.Age'], order=df['2.Age'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Age Group")
st.pyplot(fig)
st.markdown(get_key_insight(df['2.Age'], "Age Group"))

st.subheader("Marital Status")
fig, ax = plt.subplots()
sns.countplot(y=df['3.Marital status'], order=df['3.Marital status'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Marital Status")
st.pyplot(fig)
st.markdown(get_key_insight(df['3.Marital status'], "Marital Status"))

st.subheader("Education Level")
fig, ax = plt.subplots()
sns.countplot(y=df['4. Educational qualifications'], order=df['4. Educational qualifications'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Education Level")
st.pyplot(fig)
st.markdown(get_key_insight(df['4. Educational qualifications'], "Education Level"))

# Brand Preferences
st.header("Brand Preferences & Frequency")

st.subheader("Preferred Brands")
fig, ax = plt.subplots()
sns.countplot(y=df['5.which is the most preferred brand cosmetic product?'], order=df['5.which is the most preferred brand cosmetic product?'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Brand")
st.pyplot(fig)
st.markdown(get_key_insight(df['5.which is the most preferred brand cosmetic product?'], "Preferred Brand"))

st.subheader("Lakme Purchase Frequency")
fig, ax = plt.subplots()
sns.countplot(y=df['6.How frequently you purchase Lakme cosmetic products?'], order=df['6.How frequently you purchase Lakme cosmetic products?'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Frequency")
st.pyplot(fig)
st.markdown(get_key_insight(df['6.How frequently you purchase Lakme cosmetic products?'], "Lakme Purchase Frequency"))

# Spending and Organic Importance
st.header("Spending & Natural Ingredient Preference")

st.subheader("Monthly Spending")
fig, ax = plt.subplots()
sns.countplot(y=df['8.How much you spend on cosmetic products monthly?'], order=df['8.How much you spend on cosmetic products monthly?'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Spending")
st.pyplot(fig)
st.markdown(get_key_insight(df['8.How much you spend on cosmetic products monthly?'], "Monthly Spending"))

st.subheader("Importance of Natural/Organic Ingredients")
fig, ax = plt.subplots()
sns.countplot(y=df['9.How important is Natural/Organic ingredients in your cosmetic products?'], order=df['9.How important is Natural/Organic ingredients in your cosmetic products?'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Importance")
st.pyplot(fig)
st.markdown(get_key_insight(df['9.How important is Natural/Organic ingredients in your cosmetic products?'], "Importance of Natural/Organic Ingredients"))

# Advertisement and Trends
st.header("Advertisement Exposure & Trend Interest")

st.subheader("Ad Exposure")
fig, ax = plt.subplots()
sns.countplot(y=df['10.How often do you see cosmetic advertisement on media?'], order=df['10.How often do you see cosmetic advertisement on media?'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Ad Exposure")
st.pyplot(fig)
st.markdown(get_key_insight(df['10.How often do you see cosmetic advertisement on media?'], "Ad Exposure"))

st.subheader("Trend Interest")
fig, ax = plt.subplots()
sns.countplot(y=df['11.Are you interested in trying out new cosmetic trends?'], order=df['11.Are you interested in trying out new cosmetic trends?'].value_counts().index, ax=ax, palette="pastel")
ax.set_xlabel("Count")
ax.set_ylabel("Trend Interest")
st.pyplot(fig)
st.markdown(get_key_insight(df['11.Are you interested in trying out new cosmetic trends?'], "Trend Interest"))

# Suggestions
st.header("Suggestions")
st.write("Suggestions provided by the respondents:")
st.write(df['Suggest if any?'].dropna().unique())