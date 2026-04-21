# 📊 Trader Performance vs Market Sentiment

## 📌 Overview

This project analyzes how **market sentiment (Fear vs Greed)** impacts trader behavior and performance using historical trading data.

The goal is to identify patterns that can help in designing **data-driven trading strategies**.

---

## 📂 Dataset

Two datasets were used:

1. **Fear & Greed Index**

   * Columns: `timestamp`, `classification`, `date`
   * Represents market sentiment

2. **Historical Trader Data**

   * Includes: `Account`, `Side`, `Size USD`, `Closed PnL`, `Timestamp IST`, etc.
   * Represents trading activity and performance

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/narendra72/Trader-Performance-vs-Market-Sentiment.git
cd Trader-Performance-vs-Market-Sentiment
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn streamlit
```

---

## ▶️ How to Run

### Run Jupyter Notebook (Analysis)

```bash
jupyter notebook
```

### Run Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📊 Output

### Key Outputs:

* Daily PnL per trader
* Win rate analysis
* Trade frequency and size
* Long/Short ratio
* Fear vs Greed performance comparison
* Segment-based analysis

### Charts:

* Average PnL by sentiment
* Win rate comparison
* Trade behavior analysis
* Segment performance charts

---

## 🧠 Methodology

1. Data Cleaning:

   * Removed duplicates and handled missing values
   * Converted timestamps to daily level

2. Data Alignment:

   * Merged trader data with sentiment data using date

3. Feature Engineering:

   * Daily PnL per account
   * Win rate
   * Trade frequency
   * Long/Short ratio

4. Analysis:

   * Compared trader performance across Fear vs Greed days
   * Studied behavioral changes

5. Segmentation:

   * Frequent vs Infrequent traders
   * Consistent vs Inconsistent traders

---

## 📈 Insights

* Trader performance differs significantly between Fear and Greed markets
* Win rate and PnL are generally higher during Greed periods
* Traders tend to increase activity during Greed phases
* Long bias increases in Greed markets
* Consistent traders outperform across both market conditions

---

## 🚀 Strategy Recommendations

1. **Risk Control in Fear Markets**

   * Reduce trade size and trading frequency
   * Focus on capital preservation

2. **Selective Aggression in Greed Markets**

   * Increase activity only for consistent traders
   * Avoid overtrading for inexperienced traders

---

## 🤖 Bonus Work

* Built a predictive model to estimate next-day profitability
* Applied clustering to identify trader archetypes
* Developed a Streamlit dashboard for visualization

---

## 📌 Conclusion

This project demonstrates how combining **market sentiment with behavioral metrics** can lead to actionable trading strategies.

---

## 👤 Author

Narendra
BTech CSE (AI) Student
