from os import getenv
from .utils import WebDriverSetup
from .pages import SuapLoginPage, SuapBookMealPage


def suap_book_meal():
    web_driver = WebDriverSetup().driver

    username = getenv("SUAP_USERNAME")
    password = getenv("SUAP_PASSWORD")

    login_page = SuapLoginPage(web_driver)
    book_meal_page = SuapBookMealPage(web_driver)

    login_page.login(username, password)
    book_meal_page.book_meal()

    web_driver.quit()

if __name__ == "__main__":
    suap_book_meal()
