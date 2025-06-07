# 🗂️ News Sentiment Analysis – Weekly Project

This repository includes weekly tasks for sentiment and financial data analysis using Python, Git, and data science tools.

---

## 📌 Task 1 – Git, GitHub, and News EDA

This section contains the code for **Task 1** of the Week 1 challenge, focusing on:

- Setting up a Python project with Git & GitHub
- CI/CD integration using GitHub Actions
- Exploratory Data Analysis (EDA) on financial news data

---

### 📁 Folder Structure

```
├── .github/workflows/       # CI/CD configuration
├── data/                    # Raw dataset (CSV format)
├── notebooks/               # Jupyter notebooks (if any)
├── scripts/                 # Python scripts for EDA and analysis
├── src/                     # Source code or reusable modules
├── tests/                   # Unit tests
├── .gitignore
├── README.md
├── requirements.txt
```

---

### 🔧 Setup Instructions

1. **Clone the repo**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/news-sentiment-week1.git
   cd news-sentiment-week1
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

### 🚀 Scripts Overview

| Script                      | Description                                      |
|----------------------------|--------------------------------------------------|
| `eda_descriptive.py`       | Stats on headline length and publisher count     |
| `topic_modeling.py`        | NLP topic modeling using LDA                     |
| `time_series.py`           | Time series trends in publication dates          |
| `publisher_analysis.py`    | Domain-based publisher analysis                  |

---

### ✅ CI/CD

- CI pipeline uses GitHub Actions.
- Runs on every push to `main` or `task-*`.
- Executes unit tests from the `tests/` directory.

---

### 📊 Data

> **Note**: Large files like `data/raw_analyst_ratings.csv` are excluded from Git tracking via `.gitignore`.

---

## 📈 Task 2 – Quantitative Analysis Using PyNance and Technical Indicators

This task explores stock price data by applying key technical analysis indicators using Python. We use the `yfinance` and `pandas-ta` libraries to analyze historical stock prices and visualize market trends.

---

### 🧩 Tools & Libraries

- **[PyNance](https://pypi.org/project/pynance/)** or **[yfinance](https://pypi.org/project/yfinance/)** – to fetch historical stock price data
- **[pandas-ta](https://github.com/twopirllc/pandas-ta)** – for calculating technical indicators like SMA, RSI, and MACD
- **pandas** – data manipulation
- **matplotlib** – data visualization

---

### 🔧 Setup

Install dependencies:

```bash
pip install yfinance pandas-ta matplotlib
```

## 🧠 Task 3: News Sentiment and Stock Movement Correlation

This task investigates the relationship between daily news sentiment and corresponding stock price changes using sentiment analysis and financial metrics.

### 📌 Objective

To assess how news sentiment influences stock price movements by:
- Performing sentiment analysis on daily news headlines.
- Aligning sentiment scores with stock return data.
- Computing the correlation between sentiment and stock changes.

---

### 🧰 Tools & Libraries

- Python 🐍
- `pandas`, `numpy`
- `TextBlob` / `NLTK` (for sentiment scoring)
- `matplotlib`, `seaborn` (for visualization)
- `scipy.stats` (for correlation calculation)

---

### 🔄 Workflow

1. **Preprocessing**  
   - Parse and clean the news dataset.
   - Normalize dates and filter valid entries.

2. **Sentiment Analysis**  
   - Use TextBlob/NLTK to compute sentiment polarity scores for news headlines.
   - Average sentiment per day.

3. **Stock Movement Analysis**  
   - Calculate daily returns from stock prices.
   - Merge stock and sentiment data on date.

4. **Correlation Calculation**  
   - Use Pearson correlation to determine the linear relationship between sentiment and price movement.
   - Visualize the relationship using scatter plots.

### ✅ Dependencies

Install requirements with:

```bash
pip install -r requirements.txt


