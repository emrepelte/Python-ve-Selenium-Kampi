from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SauceDemoTest:

    def __init__(self):
        self.driver = webdriver.Firefox()

    def open_site(self):
        self.driver.get("https://www.saucedemo.com/")

    def close_site(self):
        self.driver.quit()

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def test_username_required(self):
        self.open_site()

        # Login butonuna tıklayarak boş kullanıcı adı ve şifre ile deneme yapalım
        login_button = self.find_element(By.CSS_SELECTOR, "input.btn_action")
        login_button.click()

        # Uyarı mesajını kontrol edelim
        error_message = self.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.text == "Epic sadface: Username is required"

        self.close_site()

    def test_password_required(self):
        self.open_site()

        # Kullanıcı adını girip, boş şifre ile deneme yapalım
        username_input = self.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        login_button = self.find_element(By.CSS_SELECTOR, "input.btn_action")
        login_button.click()

        # Uyarı mesajını kontrol edelim
        error_message = self.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.text == "Epic sadface: Password is required"

        self.close_site()

    def test_locked_out_user(self):
        self.open_site()

        # Kullanıcı adını ve şifreyi girip deneme yapalım
        username_input = self.find_element(By.ID, "user-name")
        username_input.send_keys("locked_out_user")
        password_input = self.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.find_element(By.CSS_SELECTOR, "input.btn_action")
        login_button.click()

        # Uyarı mesajını kontrol edelim
        error_message = self.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

        self.close_site()

    def test_icons_disappear(self):
        self.open_site()

        # Login butonuna tıklayarak boş kullanıcı adı ve şifre ile deneme yapalım
        login_button = self.find_element(By.CSS_SELECTOR, "input.btn_action")
        login_button.click()

        # Kırmızı X ikonlarının olduğunu kontrol edelim
        error_icons = self.driver.find_elements(By.CSS_SELECTOR, "form svg")
        assert len(error_icons) == 2

        # Uyarı mesajının kapatma butonuna tıklayalım
        close_button = self.find_element(By.CSS_SELECTOR, "button.error-button")
        close_button.click()

        # Kırmızı X ikonlarının kaybolduğunu kontrol edelim
        error_icons = self.driver.find_elements(By.CSS_SELECTOR, "form svg")
        assert len(error_icons) == 0

        self.close_site()

    def test_successful_login(self):
        self.open_site()

        # Kullanıcı adını ve şifreyi girip deneme yapalım
        username_input = self.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.find_element(By.CSS_SELECTOR, "input.btn_action")
        login_button.click()

        # Kullanıcının "/inventory.html" sayfasına yönlendirildiğini kontrol edelim
        assert self.driver.current_url.endswith("/inventory.html")

        self.close_site()

    def test_inventory_count(self):
        self.test_successful_login()  # Önce başarılı bir giriş yapalım

        # Ürün sayısını kontrol edelim
        inventory_items = self.driver.find_elements(By.CSS_SELECTOR, ".inventory_item")
        assert len(inventory_items) == 6

        self.close_site()

if __name__ == "__main__":
    test_sauce_demo = SauceDemoTest()

    test_sauce_demo.test_username_required()
    test_sauce_demo.test_password_required()
    test_sauce_demo.test_locked_out_user()
    test_sauce_demo.test_icons_disappear()
    test_sauce_demo.test_successful_login()
    test_sauce_demo.test_inventory_count()