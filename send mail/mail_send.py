from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Edge(
    "C://Users//dell//Documents//programing//python//selenium//msedgedriver.exe")
driver.get("C:/Users/dell/Documents/programing/python/send mail/mail.html")

element1 = driver.find_element_by_id('email_to')
element2 = driver.find_element_by_id('name_from')
element4 = driver.find_element_by_id('txt_subject')
element5 = driver.find_element_by_id('txt_message')

 
# send keys
element1.send_keys("devnamdevcse@gmail.com")
element2.send_keys("devnamdev@gsoc.com")
element4.send_keys("Mail from jarvish")
element5.send_keys("<h1>This mail is sent by Jarvis Program and the message is:</h1> ")
# driver.find_element_by_id("enter_btn").send_keys(Keys.ENTER)