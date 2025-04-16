# 📊 Web Scraper: Finology Stock Screener

This project scrapes real-time stock market data from the Finology screener website using `requests`, `BeautifulSoup`, and `pandas`. The scraped data is structured into a clean DataFrame and exported to a CSV file for further analysis.

## 🔍 Features
- Scrapes stock data from [Finology Screener](https://ticker.finology.in/)
- Dynamically extracts table headers and rows
- Cleans and structures data using BeautifulSoup and Pandas
- Saves the cleaned data into a CSV file

## 🛠️ Technologies Used
- Python 3.x
- requests
- BeautifulSoup (bs4)
- pandas
- lxml (parser)

## 🚀 How It Works
1. Sends an HTTP GET request to the Finology screener page
2. Parses HTML content using BeautifulSoup
3. Locates the stock screener table and extracts headers
4. Iterates through rows and strips whitespace for clean formatting
5. Loads the data into a pandas DataFrame
6. Exports the DataFrame to a CSV file

## 📂 Output
The final output is saved at:
