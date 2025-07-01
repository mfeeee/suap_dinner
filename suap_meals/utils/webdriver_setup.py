from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverSetup:
    def __init__(self):
        self.driver = self.get_driver()

    def get_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("window-size=1920x1080")

        service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(options=options, service=service)
    
    def quit_driver(self):
        if self.driver:
            self.driver.quit()
