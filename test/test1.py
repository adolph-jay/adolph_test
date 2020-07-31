from selenium import webdriver

# Chrome启动办法
# driver1 = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# driver1.get("http://www.baidu.com")

# # Firefox
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# element_keyword = driver.find_element_by_id('kw')
#
# element_keyword.send_keys('宋曲')
# element_search_button = driver.find_element_by_id('su')


import unittest

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get("http://demo.magentocommerce.com/")


    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        products = self.driver.find_element_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(2, len(products))

    def tearDown(self):
        self.driver.quit()

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.submit()
        products = self.driver.find_element_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(1, len(products))


if __name__ == '__main__':
    unittest.main(verbosity=2)


