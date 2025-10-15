# Get-Rewards — Selenium-Based Testing Trick

*Automated news-searching script that collects reward/coin points — proof-of-concept demo project*

> ⚠️ **Important:** This README documents a personal proof-of-concept automation you built. Automating interactions with third-party services can violate their terms of service and may be flagged as abuse. Use this project only for learning / testing on services you own or where explicit permission is granted. Do **not** use it to break rules or collect rewards from services where automation is prohibited.

---

## Project Summary

**Get-Rewards** is a lightweight Python + Selenium project that automates performing timed news searches (Bing News) to simulate user activity. The project was used as a practical experiment to understand web automation, browser drivers, and simple anti-detection techniques (randomized sleep), and — according to the project owner — has earned rewards worth **Rs. 3,000+**. The script is still being used to collect coins/points as a personal experiment.

---

## Key Features

* Automates sequential searches using Microsoft Edge (msedgedriver).
* Randomized wait times between searches to better simulate human behavior.
* Single-file Python script (`rewards.py`) that is easy to run and modify.
* Minimal dependencies; easily extensible for other simple automation tasks.
* Simple batch file wrapper for launching from Windows (`run_rewards.bat`).

---

## Tech Stack

* Python 3.13
* Selenium WebDriver for Microsoft Edge
* Microsoft Edge (Chromium) + `msedgedriver`
* Windows (tested on Windows 10 / 11)

---

## What’s in the repository

* `rewards.py` — main Python script (Selenium automation).
* `run_rewards.bat` (example) — batch file to run the script easily.
* `README.md` — this file.
* `notes.md` — (optional) experimental notes and results log (you can add).

---

## Prerequisites

1. Python 3.13 installed.
2. Microsoft Edge (Chromium) installed.
3. `msedgedriver.exe` matching your Edge version (download from Microsoft Edge WebDriver page).
4. Python packages:

   ```bash
   pip install selenium
   ```
5. Update script paths to match your machine:

   * `edge_driver_path` in `rewards.py` (path to `msedgedriver.exe`).
   * The batch file or the Python path in the `.bat` if you use one.

---

## Installation & Setup

1. Clone or copy the project folder to your machine (e.g., `C:\Users\<You>\Desktop\Get-Rewards`).
2. Put `msedgedriver.exe` somewhere accessible (for example: `C:\Users\<You>\Downloads\edgedriver_win64\msedgedriver.exe`).
3. Edit `rewards.py` and set:

   ```python
   edge_driver_path = "C:\\path\\to\\msedgedriver.exe"
   ```
4. (Optional) Create a batch file `run_rewards.bat` on Windows:

   ```bat
   @echo off
   cd /d "C:\path\to\project\folder"
   "C:\Users\<You>\AppData\Local\Programs\Python\Python313\python.exe" rewards.py
   pause
   ```

   Adjust the Python executable path and project folder path to match your environment.

---

## Usage

Run the script from terminal or double-click the batch file:

```bash
python rewards.py
```

The script will:

* Open Edge.
* Iterate over the list of search terms.
* Navigate to a Bing News search URL for each term.
* Wait a randomized interval (7–10 seconds by default) between searches.
* Quit the browser when finished.

You can customize:

* The `search_terms` list.
* Sleep interval bounds (`randint(...)`) to tune delays.
* The search engine or the URL format if needed.

---

## Example `rewards.py` snippet (how it works)

```python
formatted_term = search_term.replace(" ", "+")
search_url = f"https://www.bing.com/news/search?q={formatted_term}&form=QBNT"
driver.get(search_url)
time.sleep(randint(7, 10))
```

---

## Results / Achievements

* **Claimed rewards collected:** *Rs. 3,000+* (as used by the project owner for demonstration on the resume).
* The script continues to run periodically for personal experimentation and coin collection.

> Tip: If you keep an experiment log, list the dates and totals so your resume / portfolio has verifiable entries.

---

## Resume / Portfolio Blurb (copy-paste)

```
Get-Rewards — Selenium Automation (Personal Project)
• Built a Python + Selenium automation that simulates user search activity (Bing News) to explore browser automation and reward-collection mechanics.
• Implemented randomized wait times and configurable search lists; deployed locally with msedgedriver.
• Demonstrated results: experimental rewards collected totaling Rs. 3,000+ (personal learning project).
• Tech: Python 3.13, Selenium, Microsoft Edge WebDriver.
```

---

## Ethical & Legal Notice (read before using)

* **Do not** use automation to game, abuse, or bypass terms of service of third-party platforms. Doing so may result in account suspension, legal action, or other penalties.
* This repository is intended for **educational purposes only** (learning Selenium, automation patterns, and how services detect automation).
* If you plan to use similar automation on any service, obtain explicit written permission from the service owner or operate only on test accounts provided for automation/testing.

---

## Improvements & Future Work

* Implement randomized user agents and window sizes to study detection differences (research-only).
* Add more human-like behavior (scrolling, random mouse movement, click delays).
* Add logging of visits and rewards collected (local CSV or SQLite) to prove reproducible results.
* Add a configuration file to safely toggle which sites can be targeted.
* Implement error handling & retry logic with exponential backoff.

---

## Troubleshooting

* `selenium.common.exceptions.WebDriverException`: check that `msedgedriver.exe` matches your Edge version.
* Script fails to open Edge: confirm `edge_driver_path` is correct and accessible.
* Permissions issues: run terminal as Administrator if necessary.

---

## License

This project is provided for educational/demonstration purposes. No warranty. Use responsibly and ethically.

---

## Contact / Credits

Created by you (personal project). Add your name and contact info here if sharing publicly.

---

If you want, I can:

* produce a more professional one-page project summary you can attach to your resume,
* create a short PDF portfolio page with screenshots and the Rs. 3,000+ claim formatted, or
* generate a `CHANGELOG.md` and a `config.example.json` to make the script easier to configure.

Which of these would you like next?
