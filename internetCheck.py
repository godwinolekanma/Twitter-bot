from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time



class TwitterBot:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):

        self.driver.get(url="https://www.speedtest.net/")
        try:
            go = (WebDriverWait(self.driver, 1)
                  .until(EC.presence_of_element_located((By.CLASS_NAME, "start-text"))))
            go.click()
        except:
            self.driver.quit()

        time.sleep(60)
        self.down = self.driver.find_element(By.CSS_SELECTOR, ".u-align-left span").text
        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        return f"{self.down}down/{self.up}up"

    def tweet(self, email, phone, password, msg):

        self.driver.get(url='https://twitter.com/i/flow/login')
        email_enter = (WebDriverWait(self.driver, 10)
                       .until(EC.presence_of_element_located((By.NAME, "text"))))
        email_enter.send_keys(email, Keys.ENTER)
        phone_enter = (WebDriverWait(self.driver, 10)
                       .until(EC.presence_of_element_located((By.NAME, "text"))))
        phone_enter.send_keys(phone, Keys.ENTER)
        password_enter = (WebDriverWait(self.driver, 10)
                          .until(EC.presence_of_element_located((By.NAME, "password"))))
        password_enter.send_keys(password, Keys.ENTER)
        tweet_enter = (WebDriverWait(self.driver, 10)
                       .until(EC.presence_of_element_located((By.CSS_SELECTOR, ".DraftEditor-editorContainer div"))))
        tweet_enter.send_keys(msg)
