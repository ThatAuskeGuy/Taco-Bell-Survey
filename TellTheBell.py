""" Taco Bell Survey Automation """
import random

import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

# Get input from user from receipt
name = input("First and Last Name (Joe Mama): ").split()
phone = input("Phone Number (ex. 555-555-5555): ")
store = input("Store Number: ")
date_of_visit = input("MM/DD/YYYY: ").split("/")
time_of_visit = input("HH:MM:AM/PM: ").split(":")

# all definitions for program
def next_button():
    driver.find_element_by_xpath('//*[@id="NextButton"]').click()

def questions():
    ids = driver.find_elements_by_xpath('//*[contains(@id, "FNSR")]')
    try:
        for ii in ids:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]/td[3]/span').format(attr)).click()
    except NoSuchElementException:
        try:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]/div[3]/div/div[2]').format(attr)).click()
        except NoSuchElementException:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]/div[2]/div/div[1]/span/span').format(attr)).click()

def textbox():
    fill_text = ['I was just not overly satisfied by my experience', 'I just found it to be satisfactory', 'It was just a quick trip to get some food. I wasn\'t looking for an excellent experience.']
    rand_text = random.choice(fill_text)
    driver.find_element_by_xpath('//*[starts-with(@id, "S")]').send_keys(rand_text)


# Open Browser
driver = webdriver.Chrome("../chromedriver")
driver.get("http://www.tellthebell.com")

# Input receipt info on page
driver.find_element_by_xpath('//*[@id="CN1"]').send_keys(store)

receipt_items = [date_of_visit[0], date_of_visit[1], date_of_visit[2], time_of_visit[0], time_of_visit[1], time_of_visit[2]]
ids = driver.find_elements_by_xpath(('//*[starts-with(@id, "Input")]'))
n = 0
for ii in ids:
    attr = ii.get_attribute('id')
    driver.find_element_by_xpath(('//*[@id="{}"]').format(attr)).send_keys(receipt_items[n])
    n+=1
next_button()

""" Survey Questionaire """
sweepstakes = False

while sweepstakes != True:
    try:
        driver.find_element_by_xpath('//*[@id="FNSR046000"]/td[2]/span').click()
        sweepstakes = True
        next_button()
        sweepstakes_items = [name[0], name[1], phone]
        ids = driver.find_elements_by_xpath('//*[starts-with(@id, "S")]')
        n = 0
        for ii in ids:
            attr = ii.get_attribute('id')
            driver.find_element_by_xpath(('//*[@id="{}"]').format(attr)).send_keys(sweepstakes_items[n])
            n+=1
        next_button()
        driver.quit()
    except NoSuchElementException:
        try: 
            textbox()
            next_button()
        except NoSuchElementException:
            try:
                questions()
                next_button()
            except:
                break
