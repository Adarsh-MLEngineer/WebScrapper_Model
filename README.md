# Web Crawler and NLP Analyzer

## Overview

This project demonstrates how to build a simple web crawler using **Scrapy** that downloads web pages and saves them as `.html` files.
The goal is to later expand this into a full web analysis pipeline that uses **Natural Language Processing (NLP)** and **Machine Learning (ML)** techniques to extract insights from the collected data.
Eventually, the project will include a graphical user interface (GUI) to make the process more interactive and user-friendly.

---

## Current Features

* Basic Scrapy spider that crawls a target website and saves HTML files locally.
* Automatically creates an output directory for saving the downloaded files.
* Simple and modular code structure that separates web scraping from data analysis.
* Can easily be extended to handle multiple URLs or more complex scraping tasks.

---

## Project Structure

```
my_project/
│
├── scraper/
│   ├── scrape_quotes.py     # Scrapy spider
│   └── output/              # Folder where HTML files are saved
│
└── analyzer/
    └── analyze_html.py      # Machine learning and NLP analysis script
```

---

## How It Works

### 1. Web Crawler (`scrape_quotes.py`)

The Scrapy spider (`QuotesSpider`) takes a URL as input, downloads the web page, and stores it in the `output` folder. Each saved file is named based on the page being scraped.

Example code excerpt:

```python
from scrapy import Spider
from pathlib import Path

class QuotesSpider(Spider):
    name = "quotes"

    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_urls = [url] if url else []

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        (output_dir / filename).write_bytes(response.body)
        self.log(f"Saved file {output_dir / filename}")
```

To run the crawler, navigate to the `scraper` directory and execute:

```bash
python scrape_quotes.py
```

This will create an `output` folder (if it doesn’t already exist) and store the crawled HTML pages there.

---

## Future Development

### 1. Machine Learning and NLP Integration

The next step is to process the collected HTML files using text extraction and NLP tools such as **BeautifulSoup**, **spaCy**, or **Hugging Face Transformers**.
This will enable the system to perform:

* Sentiment analysis
* Topic classification
* Named entity recognition
* Keyword and phrase extraction

These analyses can help identify trends, opinions, or topics from large sets of web data.

### 2. Data Visualization

Once the NLP analysis is in place, the project will include visualization components using **Matplotlib**, **Plotly**, or **Seaborn**.
This will make it possible to view patterns, frequency distributions, and clustering results in a more understandable form.

### 3. Graphical User Interface (GUI)

A GUI will make the tool easier to use for non-programmers.
Potential frameworks for this include:

* **Streamlit** (web-based dashboard)
* **Gradio** (interactive ML demo interface)
* **PyQt** (desktop application)

Through the GUI, users will be able to enter URLs, start scraping, and view the analyzed results directly from one interface.

### 4. Automation and Scalability

The crawler can be extended to handle:

* Batch scraping of multiple websites
* Scheduled crawling using tools like **Celery** or **Airflow**
* Data storage in databases such as **SQLite** or **MongoDB** for large-scale analysis

---

## Example Workflow

1. Crawl and save HTML pages:

   ```bash
   python scraper/scrape_quotes.py
   ```

2. Analyze the scraped content:

   ```bash
   python analyzer/analyze_html.py
   ```

3. (Future) Launch the GUI dashboard:

   ```bash
   streamlit run app.py
   ```

---

## Technology Stack

| Purpose             | Technology                        |
| ------------------- | --------------------------------- |
| Web Crawling        | Scrapy                            |
| Text Extraction     | BeautifulSoup                     |
| Machine Learning    | scikit-learn, spaCy, Transformers |
| Visualization       | Matplotlib, Plotly                |
| GUI                 | Streamlit or Gradio               |
| Database (optional) | SQLite, MongoDB                   |

---

## License

This project is open source and available under the **MIT License**.

---
