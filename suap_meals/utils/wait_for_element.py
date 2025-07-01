from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def wait_for_element(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            expected_conditions.presence_of_element_located((by, value))
        )
        return element
    except Exception as e:
        print(f"Error waiting for element: {e}")
        return None