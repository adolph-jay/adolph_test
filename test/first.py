from selenium import webdriver  # 导入webdriver包

browser = webdriver.Chrome()
browser.get("https://www.baidu.com")

# browser.find_element_by_id("kw").send_keys("Selenium")
# browser.find_element_by_tag_name("input").send_keys("Selenium")
# browser.find_element_by_link_text("地图").click()  # 查找地图并且点击跳转

# browser.find_element_by_id("su").click()

# browser.find_element_by_xpath("//input[@id='kw']").send_keys("谷歌")
# browser.find_element_by_xpath("//*[@id='kw']").send_keys("谷歌")
# browser.find_element_by_xpath("//*[@name='wd']").send_keys("必应")
# browser.find_element_by_xpath("//input[@class='s_ipt']").send_keys("Google")
# browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[5]/div[1]/div/form/span[1]/input").send_keys("baidu")
browser.find_element_by_xpath("//span[@class='soutu-btn']/input")


browser.find_element_by_xpath("//input[@id='su']").click()