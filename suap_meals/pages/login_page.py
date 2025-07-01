from suap_meals.utils import wait_for_element
from selenium.webdriver.common.by import By


class SuapLoginPage:
    def __init__(self, web_driver):
        self.web_driver = web_driver
        self.url = "https://suap.ifpi.edu.br/accounts/login/?next=/"
        self.username_field = "username"
        self.password_field = "password"
        self.submit_button = "//input[@type='submit' and @value='Acessar']"

    def login(self, username, password):
        self.web_driver.get(self.url)

        username_field = wait_for_element(self.web_driver, By.NAME, "username")
        password_field = wait_for_element(self.web_driver, By.NAME, "password")
        submit_button = wait_for_element(
            self.web_driver, By.XPATH, "//input[@type='submit' and @value='Acessar']"
        )

        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()
