import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://www.taobao.com/")
        cls.driver.title


    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("phones")
        self.search_field.submit()

        products = self.driver.find_element_by_xpath("//h2[@class='product-name']/a")
        self.asserEqual(2, len(products))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.send_keys("salt shaker")
        self.search_field.submit()
        products = self.driver.find_element_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    if __name__ == '__main__':
        unittest.main()
