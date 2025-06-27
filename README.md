# **Sentiment-Driven Returns: PRIO3 (PetroRio) 2015 – 2024**

---

## 1 | Introduction
This project asks whether the **tone of Brazilian news headlines** contains a tradeable signal for PetroRio’s shares (ticker **PRIO3**).

* Scrape Portuguese headlines (2015-2024)  
* Score tone with **FinBERT-PT-BR** → `compound ∈ {-0.5, 0, +0.5}`  
* Build daily features: `compound_mean`, `compound_mag`, `art_count`  
* Join to B3 prices and compute forward returns out to **+90 days**  
* Analyse with event‐study curves, horizon bar-plots, violin distributions, correlation matrices, Granger causality and mean-difference tests.

---

## 2 | Main take-aways

| Finding | Evidence |
|---------|----------|
| **Intraday impact negligible** | Median `pct_d0` ≈ 0 % for all sentiment classes. |
| **Medium-term drift appears** | Neutral & Positive days beat Negative by 15–30 pp at D + 15 / 30. |
| **Statistical power weak so far** | Welch-t / Mann-Whitney on ≤ 7-day horizons not significant (p > 0.05). |
| **`compound_mean` ≈ `compound_mag`** | Pearson ρ ≈ 0.94. |
| **Sentiment–return link non-linear & lagged** | Pearson/Spearman ≈ 0 in short run; effect shows only after 5 + days. |

> **Bottom line:** headline tone doesn’t move PRIO3 intraday, yet there is early evidence of bullish drift 5–30 days after non-negative headlines—worth deeper back-testing with more data.

---

## 3 | Steps to reproduce

```bash
# Clone repo
git clone https://github.com/jp-alves/prio3-sentiment.git
cd prio3-sentiment

# 1) create env
conda env create -f environment.yml
conda activate prio3

# 2) download models
python -m spacy download pt_core_news_sm
python -m nltk.downloader vader_lexicon

# 3) scrape & clean
python src/scrape/scraping_news.py
python src/scrape/scraping_prices.py
python src/clean/clean_news.py
python src/clean/clean_prices.py

# 4) NLP + merge
python -m src.nlp.apply_sentiment
python analysis/merge.py

# 5) open notebook
jupyter lab                 # notebook/prio3_sentiment.ipynb
