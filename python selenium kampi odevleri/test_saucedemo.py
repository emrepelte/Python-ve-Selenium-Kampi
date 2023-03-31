import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# SauceDemoTest sınıfını kaldırıyoruz ve tüm fonksiyonları düz fonksiyon olarak tanımlıyoruz
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def open_site(driver):
    driver.get("https://www.saucedemo.com/")

def test_username_required(driver, open_site):
    # Login butonuna tıklayarak boş kullanıcı adı ve şifre ile deneme yapalım
    login_button = driver.find_element(By.CSS_SELECTOR, "input.btn_action")
    login_button.click()

    # Uyarı mesajını kontrol edelim
    error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error_message.text == "Epic sadface: Username is required"

    # Ekran görüntüsü alalım
    driver.save_screenshot("username_required.png")

@pytest.mark.parametrize("username,password,error_message", [
    ("", "secret_sauce", "Epic sadface: Username is required"),
    ("standard_user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out.")
])
def test_login_error_messages(driver, open_site, username, password, error_message):

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    username_input = driver.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys(username)
    
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(password)
    
    login_button = driver.find_element(By.CSS_SELECTOR, "input.btn_action")
    login_button.click()
    
    displayed_error_message = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert displayed_error_message.text == error_message

    # Ekran görüntüsü alalım
    driver.save_screenshot("login_error_messages.png")

def test_icons_disappear(driver, open_site):
    # Login butonuna tıklayarak boş kullanıcı adı ve şifre ile deneme yapalım
    login_button = driver.find_element(By.CSS_SELECTOR, "input.btn_action")
    login_button.click()

    # Kırmızı X ikonlarının olduğunu kontrol edelim
    error_icons = driver.find_elements(By.CSS_SELECTOR, ".input_error_container svg")
    assert len(error_icons) == 2


    # Uyarı mesajının kapatma butonuna tıklayalım
    close_button = driver.find_element(By.CSS_SELECTOR, "button.error-button")
    close_button.click()

    # Kırmızı X ikonlarının kaybolduğunu kontrol edelim
    error_icons = driver.find_elements(By.CSS_SELECTOR, "form svg")
    assert len(error_icons) == 0

    # Ekran görüntüsü alalım
    driver.save_screenshot("icons_disappear.png")

def test_successful_login(driver, open_site):
    # Kullanıcı adını ve şifreyi girip deneme yapalım
    username_input = driver.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys("standard_user")
    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("secret_sauce")
    login_button = driver.find_element(By.CSS_SELECTOR, "input.btn_action")
    login_button.click()

    # Kullanıcının "/inventory.html" sayfasına yönlendirildiğini kontrol edelim
    assert driver.current_url.endswith("/inventory.html")

    # Ekran görüntüsü alalım
    driver.save_screenshot("successful_login.png")

def test_inventory_count(driver):
    # Ürün sayısını kontrol edelim
    inventory_items = driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
    assert len(inventory_items) == 6

    # Ekran görüntüsü alalım
    driver.save_screenshot("inventory_count.png")

def test_add_item_to_cart(driver, open_site):
    test_successful_login(driver, open_site)

    # İlk ürünü sepete ekleyelim
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")
    add_to_cart_button.click()

    # Sepetin ürün sayısını kontrol edelim
    cart_count = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert cart_count.text == "1"

    # Ekran görüntüsü alalım
    driver.save_screenshot("add_item_to_cart.png")

def test_remove_item_from_cart(driver, open_site):
    test_successful_login(driver, open_site)

    # İlk ürünü sepete ekleyelim
    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")
    add_to_cart_button.click()

    # Ürünü sepetten çıkaralım
    remove_from_cart_button = driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) button")
    remove_from_cart_button.click()

    # Sepetin boş olduğunu kontrol edelim
    cart_badges = driver.find_elements(By.CSS_SELECTOR, ".shopping_cart_badge")
    assert len(cart_badges) == 0

    # Ekran görüntüsü alalım
    driver.save_screenshot("remove_item_from_cart.png")
