# E-Commerce-Price-Tracker-Analytics-Dashboard
An automated system that tracks product prices across e-commerce websites by web-scraping and stores the data into MySQL database and provides real-time analytics through an interactive dashboard by PowerBI.

# Step 1: Creation of Project folder
mkdir book_scraper_project
cd book_scraper_project
python -m venv venv
source venv/Scripts/activate     
pip install requests beautifulsoup4 pandas

# Step 2: Create file scraper.py
Use the file above updated scraper.py

# Step 3: Runing of scraping function
python scrape_books.py
output:- 
Scraping page 1: https://books.toscrape.com/catalogue/page-1.html
...
✅ Scraped 200 books successfully!

# Step 4: Store Scraped data into MySQL database
# Install MySQL
If not installed: Download MySQL Community Edition

# During setup, remember:
Root password
Port (default 3306)

# Install Python connector
pip install mysql-connector-python sqlalchemy pymysql

# Create database
CREATE DATABASE book_scraper_db;
USE book_scraper_db;

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    price FLOAT,
    rating VARCHAR(10),
    availability VARCHAR(50)
);

# Run scraper.py
Scraping page 1: https://books.toscrape.com/catalogue/page-1.html
...
✅ Scraped 200 books successfully and saved to MySQL!
<img width="1920" height="1080" alt="Screenshot (24)" src="https://github.com/user-attachments/assets/345f3a3f-1143-4762-bec7-4ee3af115c48" />

# Step 5: Analytics Ready: Connect MySQL Data to Power BI
# Using PowerBI
Open Power BI Desktop → Home → Get Data → More…
Select MySQL database → Connect
Enter your database details:
  Server: localhost (if local)
  Database: book_scraper_db
  Username / Password: your MySQL login

Click Connect
  Select books table → Load

Now you can build visuals:
  Average price per rating
  Price distribution histogram
  Top 10 most expensive books

# Using Python for ML
Code snepet is in Analytics.py
<img width="1920" height="1080" alt="Screenshot (27)" src="https://github.com/user-attachments/assets/d9bbb15c-ee1f-490e-8568-cf253c97db89" />

# ETL Automation: Append New Pages / Data Automatically
ETL = Extract → Transform → Load.
# Windows Task Scheduler
  Open Task Scheduler → Create Task
  Name: Book Scraper Daily
  Trigger: Daily, set time
  Action: Start a program
  Program: python.exe
  Arguments: C:\path\to\scrape_books_mysql.py
  Save → It will run every day automatically.
<img width="1920" height="1080" alt="Screenshot (26)" src="https://github.com/user-attachments/assets/efc9b730-51d6-4d25-a1eb-09f3eec802a8" />

