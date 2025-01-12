from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from concurrent.futures import ThreadPoolExecutor
import os
import time

# Kullanıcı durumunu kontrol eden fonksiyon
def check_user_status(username):
    url = f"https://x.com/{username}"

    # Selenium için tarayıcı ayarları
    options = Options()
    options.add_argument("--headless")  # Tarayıcıyı görünmez modda çalıştır
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")  # Log'ları azalt

    # Görüntüleri ve gereksiz içerikleri yüklemeyi engelle
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)

    # ChromeDriver yolunu belirleyin
    driver_path = r"C:\\Users\\roost\\PycharmProjects\\TwitterUserCheck\\chromedriver.exe"
    service = Service(driver_path)

    # WebDriver başlat
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        time.sleep(1)  # Kısa bir bekleme
        page_text = driver.page_source  # HTML içeriğini al

        # Metni kontrol et
        if "Hesap askıya alındı" in page_text:
            return "suspended"
        elif "Üzgünüz, bu sayfa mevcut değil!" in page_text or "Sorry, that page doesn’t exist!" in page_text:
            return "not found"
        else:
            return "active"
    except Exception as e:
        return "error"
    finally:
        driver.quit()  # Tarayıcıyı kapat

# Her kullanıcı için durumu kontrol eden işlem
def process_user(username):
    status = check_user_status(username)
    print(f"{username}: {status}")
    return f"{username}: {status}"

# Ana program
def main():
    base_dir = r"C:\\Users\\roost\\PycharmProjects\\TwitterUserCheck"
    input_file = os.path.join(base_dir, "usernames.txt")
    output_file = os.path.join(base_dir, "results.txt")

    # Kullanıcı adlarını oku
    with open(input_file, "r") as infile:
        usernames = infile.read().splitlines()

    # Çoklu iş parçacığı kullanarak işlemleri hızlandır
    with ThreadPoolExecutor(max_workers=5) as executor:  # Aynı anda 5 işlem
        results = list(executor.map(process_user, usernames))

    # Sonuçları dosyaya yaz
    with open(output_file, "w") as outfile:
        outfile.write("\n".join(results))

if __name__ == "__main__":
    main()