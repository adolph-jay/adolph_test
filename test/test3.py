import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from __builtin__ import classmethod

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("https://www.taobao.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,"q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID,"select-language"))

    def tst_shopping_cart_empty_message(self):
        shopping_cart_icon = self.driver.find_element_by_css_selector("div.header-minicart span.icon")
        shopping_cart_icon.click()
        shopping_cart_status = self.driver.find_element_by_css_selector("p.empty").test
        self.assertEqual("You have no items in your shopping cart.",shopping_cart_status)
        close_button = self.driver.find_element_by_css_selector("div.minicart-wrapper a.close")
        close_button.click()


    @classmethod
    def tesrDown(cls):
        cls.driver.quit()

    def is_element_present(self, how, what):
        try: self.driver.find_element(by = how, value=what)
        except NoSuchElementException, e: return False
        return True


    if __name__ == '__main__':
        unittest.main(verbosity=2)
