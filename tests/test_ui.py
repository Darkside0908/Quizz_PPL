import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Setup base URL (akan berjalan di localhost port 8000 saat CI/CD)
BASE_URL = "http://localhost:8000"

@pytest.fixture(scope="module")
def driver():
    # Menggunakan Chrome Driver dengan Headless mode untuk CI/CD
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# --- TEST MODUL REGISTER ---

def test_register_empty_data(driver):
    driver.get(f"{BASE_URL}/register.php")
    # Langsung klik submit tanpa mengisi form
    driver.find_element(By.NAME, "submit").click()
    
    # Validasi error message
    error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text
    assert "Data tidak boleh kosong !!" in error_msg

def test_register_password_mismatch(driver):
    driver.get(f"{BASE_URL}/register.php")
    driver.find_element(By.ID, "name").send_keys("User Test")
    driver.find_element(By.ID, "InputEmail").send_keys("test@test.com")
    driver.find_element(By.ID, "username").send_keys("usertest123")
    driver.find_element(By.ID, "InputPassword").send_keys("password123")
    driver.find_element(By.ID, "InputRePassword").send_keys("passwordsalah")
    driver.find_element(By.NAME, "submit").click()
    
    # Validasi pesan error password
    error_msg = driver.find_element(By.CLASS_NAME, "text-danger").text
    assert "Password tidak sama !!" in error_msg

# --- TEST MODUL LOGIN ---

def test_login_empty_data(driver):
    driver.get(f"{BASE_URL}/login.php")
    driver.find_element(By.NAME, "submit").click()
    
    error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text
    assert "Data tidak boleh kosong !!" in error_msg

def test_login_invalid_credentials(driver):
    driver.get(f"{BASE_URL}/login.php")
    driver.find_element(By.ID, "username").send_keys("userngasal")
    driver.find_element(By.ID, "InputPassword").send_keys("passngasal")
    driver.find_element(By.NAME, "submit").click()
    
    error_msg = driver.find_element(By.CLASS_NAME, "alert-danger").text
    # Mengacu pada code PHP, error invalid login memunculkan string ini
    assert "Register User Gagal !!" in error_msg