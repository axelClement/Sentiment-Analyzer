# Market Sentiment Analyzer: S&P 500

## 1. Project Overview

This repository contains an end-to-end data pipeline designed to extract, process, and analyze financial retail sentiment from social media interactions. Focusing on the S&P 500 index, the system scrapes data from major financial forums and applies Natural Language Processing (NLP) techniques to quantify market sentiment.

The primary objective of this project is to provide a structured approach to non-traditional financial data (alternative data), enabling the observation of correlations between retail investor sentiment and broader market movements.

## 2. Technical Architecture

The project is structured as a sequential data engineering and NLP pipeline:

1. **Data Ingestion (Scraping):** 
   Utilizes the Reddit API (via `praw`) to extract live data from high-volume financial subreddits (e.g., `r/stocks`, `r/investing`, `r/wallstreetbets`). The scraper filters posts based on a dynamically generated list of S&P 500 company tickers and general financial keywords.
2. **Natural Language Processing (Sentiment Analysis):**
   Applies VADER (Valence Aware Dictionary and sEntiment Reasoner) to the extracted text. VADER is highly optimized for social media text, effectively handling colloquialisms and financial jargon to yield a compound polarity score (Positive, Negative, or Neutral).
3. **Data Visualization:**
   Leverages `matplotlib` and `pandas` to aggregate the sentiment scores and visualize the macroscopic market outlook over the extracted dataset.

## 3. Tech Stack

- **Language:** Python 3.10+
- **Data Collection:** PRAW (Python Reddit API Wrapper), Requests
- **Data Processing:** Pandas
- **NLP / Sentiment Analysis:** vaderSentiment
- **Data Visualization:** Matplotlib

## 4. Installation and Setup

### Prerequisites
Ensure that Python is installed on your local machine along with `pip`. You will also need active Reddit API credentials (Client ID, Client Secret, and User Agent).

### Environment Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/axelClement/Sentiment-Analyzer.git
   cd Sentiment-Analyzer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure your API keys. You must define your credentials inside the [src/reddit_config.py](file:///c:/Users/Axel/Documents/Etudes/Annee_4/Stage/CV/Sentiment-Analyzer/src/reddit_config.py) file to authenticate the scraper.

## 5. Usage

The entire pipeline can be executed via the central orchestration script. 

```bash
python src/main.py
```

### Execution Flow:
1. **[scrape_reddit()](file:///c:/Users/Axel/Documents/Etudes/Annee_4/Stage/CV/Sentiment-Analyzer/src/reddit_scraper.py#6-60)**: Connects to the configured subreddits, filters posts based on S&P 500 keywords, and outputs a raw dataset (`data/reddit_sp500_posts.csv`).
2. **[analyze_sentiment()](file:///c:/Users/Axel/Documents/Etudes/Annee_4/Stage/CV/Sentiment-Analyzer/src/sentiment_analyzer.py#7-43)**: Reads the raw data, applies the NLP sentiment model to each post title, and outputs an enriched dataset (`data/sentiment_analysis_results.csv`).
3. **`visualize_combined_sentiment()`**: Consumes the enriched data to generate visual analytics and summary charts.

## 6. Project Structure

```text
Sentiment-Analyzer/
│
├── data/                               # Directory for raw and processed CSV files
├── src/                                # Source code directory
│   ├── main.py                         # Pipeline orchestrator
│   ├── reddit_config.py                # API authentication configuration
│   ├── reddit_scraper.py               # Data ingestion module
│   ├── sentiment_analyzer.py           # NLP processing module
│   ├── generate_keywords.py            # S&P 500 keyword generation logic
│   └── visualize_results.py            # Data visualization and graphing module
│
├── requirements.txt                    # Python dependencies
└── README.md                           # Project documentation
```
