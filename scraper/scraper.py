import os
import threading
import zipfile
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime

# ANDROID-SAFE BASE PATH
BASE_DIR = "/sdcard/Download/MediaScraper"
os.makedirs(BASE_DIR, exist_ok=True)

lock = threading.Lock()
downloaded_files = []

HEADERS = {"User-Agent": "Mozilla/5.0"}

def log(msg):
    with open(os.path.join(BASE_DIR, "scrape.log"), "a") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def download_file(url, folder):
    os.makedirs(folder, exist_ok=True)
    filename = os.path.join(folder, os.path.basename(url.split("?")[0]))

    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            with open(filename, "wb") as f:
                f.write(r.content)

            with lock:
                downloaded_files.append(filename)

            log(f"Downloaded: {filename}")
    except Exception as e:
        log(f"ERROR downloading {url}: {e}")

def scrape(url, depth=1):
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(r.text, "html.parser")

        for tag in soup.find_all(["img", "video", "audio", "a"]):
            src = tag.get("src") or tag.get("href")
            if not src:
                continue

            full_url = urljoin(url, src)
            ext = full_url.split(".")[-1].lower()

            if ext in ["jpg", "jpeg", "png", "gif"]:
                download_file(full_url, f"{BASE_DIR}/images")

            elif ext in ["mp4", "webm"]:
                download_file(full_url, f"{BASE_DIR}/videos")

            elif ext in ["mp3", "wav"]:
                download_file(full_url, f"{BASE_DIR}/audio")

    except Exception as e:
        log(f"SCRAPE ERROR: {e}")

def zip_results():
    zip_path = f"{BASE_DIR}/media.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in downloaded_files:
            zipf.write(file, arcname=os.path.basename(file))
    log("ZIP created")

def start_scrape(url):
    def runner():
        log("Scrape started")
        scrape(url)
        zip_results()
        log("Scrape finished")

    threading.Thread(target=runner, daemon=True).start()
