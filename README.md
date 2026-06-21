# Automated Inventory
An automated tool to manage inventory and research market prices. The script monitors local stock levels and scrapes real-time pricing for items requiring a restock.

Key Features
Inventory Monitoring: Automatically flags items below your defined stock threshold.

Web Scraping: Uses Selenium to search and extract competitor pricing.

Data Cleaning: Uses Regex to provide clean, numeric price data for analysis.

Human-like Interaction: Mimics user behavior to avoid bot detection.

Structured Output: Exports all findings into a clean, easy-to-read CSV file.

Technologies
Python

Selenium

Pandas

Regular Expressions (re)

Getting Started
Install dependencies:

pip install selenium pandas

Ensure your inventory.csv is in the project folder.

Run the script:

python main.py



