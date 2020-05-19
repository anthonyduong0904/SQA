from selenium import webdriver
username = 'shopeetest'
password = 'Shopee@2020'
url = 'http://newtours.demoaut.com'
driver = webdriver.Chrome("E:\Downloads\chromedriver.exe")
driver.get(url)
driver.find_element_by_xpath("//input[contains(@type,'text')]").send_keys(username)
driver.find_element_by_xpath("//input[contains(@type,'password')]").send_keys(password)
driver.find_element_by_xpath("//input[contains(@name,'login')]").click()