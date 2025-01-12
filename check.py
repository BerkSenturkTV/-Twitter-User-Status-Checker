from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import os
import time

# Function to check the status of a user
def check_user_status(username):
    url = f"https://x.com/{username}"

    # Browser settings for Selenium
    options = Options()
    options.add_argument("--headless")  # Run the browser in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")  # Reduce log output

    # Prevent loading images and unnecessary content
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    # Specify the path to ChromeDriver
    driver_path = r"C:\\Users\\roost\\PycharmProjects\\TwitterUserCheck\\chromedriver.exe"
    service = Service(driver_path)

    # Start WebDriver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        time.sleep(1)  # Short wait for the page to load
        page_text = driver.page_source  # Get the HTML content

        # Check the text content
        if "Hesap askıya alındı" in page_text:
            return "suspended"
        elif "Üzgünüz, bu sayfa mevcut değil!" in page_text or "Sorry, that page doesn’t exist!" in page_text:
            return "not found"
        else:
            return "active"
    except Exception as e:
        return "error"
    finally:
        driver.quit()  # Close the browser

# Process each user's status
def process_user(username):
    status = check_user_status(username)
    print(f"{username}: {status}")
    return f"{username}: {status}"

# Main program
def main():
    base_dir = r"C:\\Users\\roost\\PycharmProjects\\TwitterUserCheck"
    input_file = os.path.join(base_dir, "usernames.txt")
    output_file = os.path.join(base_dir, "results.txt")

    # Read usernames from the file
    with open(input_file, "r") as infile:
        usernames = infile.read().splitlines()

    # Use multi-threading to speed up the process
    with ThreadPoolExecutor(max_workers=10) as executor:  # Process 5 tasks concurrently
        results = list(executor.map(process_user, usernames))

    # Write results to the output file
    with open(output_file, "w") as outfile:
        outfile.write("\n".join(results))

if __name__ == "__main__":
    main()
