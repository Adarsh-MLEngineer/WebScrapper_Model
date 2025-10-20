import scrapy
from pathlib import Path
from scrapy.crawler import CrawlerProcess

class QuotesSpider(scrapy.Spider):
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
        self.log(f"✅ Saved file {output_dir / filename}")
        return filename


def scrape_url(url):
    process = CrawlerProcess(settings={
        "LOG_LEVEL": "INFO",  # reduce log clutter
    })
    process.crawl(QuotesSpider, url=url)
    process.start()  # the script will block here until crawling is finished

# Example usage:
scrape_url("https://en.wikipedia.org/wiki/Wiki")
