# Stock Data Scraper

This project is a Scrapy spider that extracts stock data from Yahoo Finance, focusing on various sectors like consumer cyclicals, technology, healthcare, etc. The data includes stock symbols, company names, prices, market capitalization, and other financial metrics.

## File Structure

├── README.md </br>
├── &#95;pycache_</br>
│   └── creds.cpython-310.pyc </br>
├── creds.py </br>
├── desired.html </br>
├── extract_stocks.sh </br>
├── scrapy.cfg </br>
└── src </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  ├── &#95;init_.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── &#95;pycache_ </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── &#95;init_.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── items.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   └── settings.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── items.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── middlewares </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── &#95;init_.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── &#95;pycache_ </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   ├── &#95;init_.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   └── middlewares.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   └── middlewares.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── pipelines </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── &#95;init&#95;.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   ├── &#95;pycache&#95; </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   ├── &#95;init_.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   │   └── mongo_pipeline.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    │   └── mongo_pipeline.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    ├── settings.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    └── spiders </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ├── &#95;_init_.py </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ├── &#95;pycache_ </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   │   ├── &#95;init_.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   │   └── stocks_spider.cpython-310.pyc </br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   └── stocks_spider.py </br>


## Features

- Extracts stock data from predefined Yahoo Finance sector pages.
- Utilizes Scrapy-Splash to render JavaScript content.
- Stores extracted data in a MongoDB database.
- Customizable to add more sectors or modify data points.

## Installation

Ensure you have Python 3, pip, and MongoDB installed on your machine. Then, clone this repository and install the dependencies:

- ```bash``` 
- ```git clone https://github.com/vishwam7/stock_crawling_prediction.git``` 
- ```cd stock-data-scraper``` 
- ```pip install -r requirements.txt``` 


## Running the Spider

To start the spider and begin scraping, use the following command:

- ```bash``` 
- ```scrapy crawl stocks```


## Configuring MongoDB

The project uses MongoDB to store the scraped data. Configure your MongoDB URI, database, and collection name in the `settings.py` file:

- ```MONGO_URI = 'your_mongodb_uri'```
- ```MONGO_DATABASE = 'your_database_name'```
- ```MONGO_COLLECTION = 'your_collection_name'```


## Splash Setup

This project requires Splash for rendering JavaScript content. Make sure you have Splash running:

- ```bash```
- ```docker run -p 8050:8050 scrapinghub/splash```
- ```sudo docker pull scrapinghub/splash```
- ```sudo docker run -it -p 8050:8050 --rm scrapinghub/splash```


Update the `SPLASH_URL` in `settings.py` if your Splash instance is running on a different host or port.

## Project Structure

- `src/spiders/stocks_spider.py`: Main spider for scraping stock data.
- `src/items.py`: Defines the data structure for stock items.
- `src/pipelines/mongo_pipeline.py`: Pipeline for processing and storing items in MongoDB.
- `src/middlewares.py`: Middlewares including Scrapy-Splash configurations.
- `settings.py`: Project settings including Scrapy and MongoDB configuration.

## Contribution

Contributions are welcome! If you want to improve the scraper or add features, feel free to fork this repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
