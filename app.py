import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Trader Performance Dashboard")

# load data
df = pd.read_csv("final_data.csv")

# filter
sentiment = st.selectbox("Select Sentiment", df["classification"].unique())

filtered_df = df[df["classification"] == sentiment]

# chart
st.subheader("Average PnL")

fig, ax = plt.subplots()
sns.barplot(data=filtered_df, x="Account", y="daily_pnl", ax=ax)
plt.xticks(rotation=90)

st.pyplot(fig)