import time
import unittest
import self as self
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):
    def testPasss(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()
        driver.find_element(By.ID, 'username').send_keys('tomsmith')
        driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        driver.find_element(By.XPATH, '//i[contains(text(),Login)]').click()
        text = driver.find_element(By.XPATH, "//div[@id='flash']").text
        self.assertEqual("You logged into a secure area!\n×", text)
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    unittest.main()


class Test1(unittest.TestCase):
    def testFail(self):
        driver = webdriver.Chrome(executable_path="chromedriver.exe")
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()
        driver.find_element(By.ID, 'username').send_keys('toms')
        driver.find_element(By.ID, 'password').send_keys('SuperSecretPa')
        driver.find_element(By.XPATH, '//i[contains(text(),Login)]').click()
        text = driver.find_element(By.XPATH, "//div[@id='flash']").text
        self.assertEqual("Your username is invalid!\n×", text)
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
