import  time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoFindByLinkText:
    driver = webdriver.Chrome(ChromeDriverManager().install())

    def find_by_linktext(self):
        self.driver.get("https://www.saucedemo.com/")
        user_name = self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        password = self.driver.find_element(By.ID, "password").send_keys("secret_sauce")

    def find_by_login(self):
        login = self.driver.find_element(By.ID, "login-button"). click()


obj = DemoFindByLinkText()
obj.find_by_linktext()
obj.find_by_login()



