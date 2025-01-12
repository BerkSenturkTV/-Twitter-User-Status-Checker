
# Twitter User Status Checker

A Python project to check the status of Twitter (X) user accounts. This script uses Selenium to scrape user profile pages and determine if an account is active, suspended, or not found. It supports multi-threading for faster performance.

## Features
- Scrapes user profile pages to determine account status.
- Supports `active`, `suspended`, or `not found` statuses.
- Multi-threaded execution for improved speed.
- Lightweight and headless browser configuration.

## Prerequisites
1. **Python**: Ensure Python 3.7+ is installed.
2. **Google Chrome**: Install the latest version of Google Chrome.
3. **ChromeDriver**: Download the compatible version of ChromeDriver for your Chrome version from [ChromeDriver](https://chromedriver.chromium.org/downloads).
4. **Dependencies**: Install required Python packages:
   ```bash
   pip install selenium
   ```

## Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/twitter-user-status-checker.git
   ```
2. Navigate to the project directory:
   ```bash
   cd twitter-user-status-checker
   ```
3. Place `chromedriver.exe` in the project root directory.
4. Create a file named `usernames.txt` in the project root and list Twitter usernames, one per line.

## Usage
Run the script:
```bash
python twitter_user_check.py
```

### Output
- The statuses of the usernames will be written to `results.txt` in the project root.
- Each line in `results.txt` will contain the username and its status, e.g.,:
  ```
  user1: active
  user2: suspended
  user3: not found
  ```

## Notes
- This project uses Selenium in headless mode to minimize resource usage.
- Multi-threading accelerates account checks by running multiple requests in parallel.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---
**Disclaimer**: This project is for educational purposes only. Scraping websites may violate their terms of service. Use responsibly.
