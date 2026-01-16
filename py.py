from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# =========================
# CHROME BEÁLLÍTÁSOK
# =========================
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("--disable-infobars")
options.add_argument("--disable-web-security")
options.add_argument("--disable-site-isolation-trials")
options.add_argument("--disable-features=IsolateOrigins,site-per-process")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"
)

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """
    },
)

# =========================
# SEGÉDFÜGGVÉNYEK
# =========================
def reset_local_storage():
    driver.execute_script("localStorage.clear();")
    driver.refresh()
    time.sleep(1)

# =========================
# TESZTEK
# =========================
try:
    # ⚠️ ÁLLÍTSD BE A SAJÁT ÚTVONALADAT
    driver.get("file:///C:/Users/gombosb/Desktop/termekek.html")
    driver.get(path)
    time.sleep(2)

    # -------- TÖRLÉS TESZT --------
    print("🔴 Törlés teszt indul")

    reset_local_storage()

    termekek_elotte = driver.find_elements(By.CLASS_NAME, "card")
    darab_elotte = len(termekek_elotte)

    torles_gomb = driver.find_element(
        By.XPATH, "(//button[contains(text(),'Törlés')])[1]"
    )
    torles_gomb.click()
    time.sleep(1)

    termekek_utana = driver.find_elements(By.CLASS_NAME, "card")
    darab_utana = len(termekek_utana)

    assert darab_utana == darab_elotte - 1
    print("✅ Törlés teszt sikeres")

    # -------- MÓDOSÍTÁS TESZT --------
    print("🟡 Módosítás teszt indul")

    reset_local_storage()

    modositas_gomb = driver.find_element(
        By.XPATH, "(//button[contains(text(),'Módosítás')])[1]"
    )
    modositas_gomb.click()

    alert = driver.switch_to.alert
    alert.send_keys("Teszt termék")
    alert.accept()

    alert = driver.switch_to.alert
    alert.send_keys("Selenium módosította")
    alert.accept()

    time.sleep(1)

    nev = driver.find_element(By.XPATH, "//h4").text
    leiras = driver.find_element(By.XPATH, "//p").text

    assert nev == "Teszt termék"
    assert leiras == "Selenium módosította"

    print("✅ Módosítás UI teszt sikeres")

    # -------- localStorage ellenőrzés --------
    termekek = driver.execute_script(
        "return JSON.parse(localStorage.getItem('termekek'));"
    )

    assert termekek[0]["nev"] == "Teszt termék"
    assert termekek[0]["leiras"] == "Selenium módosította"

    print("✅ localStorage ellenőrzés sikeres")

    print("\n🎉 MINDEN TESZT SIKERES 🎉")

finally:
    time.sleep(3)
    driver.quit()
