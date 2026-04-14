# NLP Scrapy Project - Real Estate Data

A simple data pipeline to scrape, clean, and process Vietnamese real estate data using Natural Language Processing (NLP).

## 📁 Project Structure

This project is organized as follows:

* **`assets/`**: Contains auxiliary files like `vietnamese-stopwords.txt`.
* **`data/`**: 
    * `raw/`: Raw scraped data from the websites.
    * `processed/`: Cleaned data (`clean_data.json`) and final data with NLP processing (`nlp_data.json`).
* **`notebooks/`**: Jupyter Notebooks for testing code and finding keywords (`test_nlp.ipynb`, `find_keywords.ipynb`).
* **`scrapy_crawler/`**: The web scraping source code (Scrapy framework).
* **`src/`**: The core processing logic.
    * `cleaner.py`: Cleans raw numbers, prices, and addresses.
    * `nlp_processor.py`: Handles text normalization, tokenization, and stopword removal (Underthesea).
    * `main_process.py`: The master script that runs the entire cleaning and NLP pipeline.
* **`download_stopwords.py`**: A quick script to download the Vietnamese stopwords dictionary.
* **`requirements.txt`**: List of Python dependencies.