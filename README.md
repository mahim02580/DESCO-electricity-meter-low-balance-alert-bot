# ⚡ DESCO Electricity Meter Balance Notifier

This Python automation script checks your DESCO prepaid electricity meter balance using Selenium and sends an alert email automatically when the balance goes below a minimum threshold.

### 🚀 Features

* Logs into DESCO prepaid meter portal automatically

* Scrapes current balance using Selenium

* Sends Gmail email alert when balance is low

* Runs fully headless — no visible browser window

* Uses .env file for secure credential storage

### 🛠️ Requirements
Install dependencies: `pip install -r requirements.txt`

#### WebDriver Requirement
Make sure Chrome + ChromeDriver is installed.
Download ChromeDriver matching your Chrome version.

### 📦 Environment Setup

Create a .env file in the same directory as the script:

ACCOUNT_NUMBER=YOUR_METER_ACCOUNT_NUMBER
EMAIL=your_email@gmail.com
APP_PASSWORD=your_gmail_app_password


_⚠ Gmail requires an App Password — not regular password._

### ▶️ How to Run

Run manually from terminal:

`python main.py`

Or set a scheduled task / cronjob for auto-checking every hour.

### 📧 Email Alert Example

Subject: ⚠️ Electricity Meter Low Balance Alert!
Message example:
Current balance for meter account: 123456 is 95 BDT.