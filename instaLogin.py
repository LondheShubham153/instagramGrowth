from selenium import webdriver
from time import sleep
from config import password

class InstaBot:
    def __init__(self, username,password):
        self.diver = webdriver.Chrome()
        self.username = username
        self.diver.get("https://www.instagram.com/")
        sleep(2)
        self.diver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.diver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        self.diver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(4)
        self.diver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(4)
        self.diver.find_element_by_xpath("//button[contains(text(),'Not Now')]").click()
        sleep(2)

my_bot = InstaBot('shubhamlondhe96', password)