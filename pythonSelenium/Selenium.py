import time
from argparse import Action
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains

email="cebrailyyy57@outlook.com"
pasword="cebrail147"

def  test_verify_registration():

        driver = webdriver.Chrome(executable_path="C:\Users\ASUS\PycharmProjects\pythonSelenium\chrome\chromedriver.exe")
        driver.get("https://www.amazon.com.tr/")
        driver.maximize_window()
        print (driver.title)
        driver.find_element_by_id("sp-cc-accept").click()

        #Login

        action = ActionChains(driver)
        LogiButton = driver.find_element_by_xpath("//span[@class='nav-action-inner']")
        LoginButton1 = driver.find_element_by_id("nav-link-accountList")
        action.move_to_element(LoginButton1).perform()
        LogiButton.click()

        Resume =driver.find_element_by_id("ap_email");
        ResumeButton = driver.find_element_by_id("continue")
        Resume.send_keys(email)
        ResumeButton.click()
        PasswordArea = driver.find_element_by_id("ap_password")
        PasswordButton = driver.find_element_by_id("signInSubmit")
        PasswordArea.send_keys(pasword)
        PasswordButton.click()


        #Search
        driver.find_element_by_id("twotabsearchtextbox").send_keys("telefon") #search area
        time.sleep(1)
        driver.find_element_by_id("nav-search-submit-button").click() #search button

        #urun secme
        driver.find_element_by_xpath("//div[@data-asin='B091PSGJYT']").click()

        #sepete ekleme
        driver.find_element_by_id("add-to-cart-button").click()

        #sepete gitme
        driver.find_element_by_id("hlb-view-cart-announce").click()
        time.sleep(2)

        #urunu kaldirma
        driver.find_element_by_xpath("//input[@data-action='delete']").click()










