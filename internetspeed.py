from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.common.exceptions import NoSuchElementException
import time

class InternetSpeedTwitterBot():
    def __init__(self):
        super().__init__()
        self.up = 0
        self.down = 0
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        
    def get_internet_speed(self, url):
        self.driver.get(url)
        start_speed_test = self.driver.find_element(By.CSS_SELECTOR, "span[class*='start-text']")
        start_speed_test.click()
        time.sleep(60)
        download_speed = self.driver.find_element(By.CSS_SELECTOR, "span[class*='download-speed']")
        upload_speed = self.driver.find_element(By.CSS_SELECTOR, "span[class*='upload-speed']")
        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)
        print(self.up, self.down)
    
    def tweet_at_provider(self, url, email, username, password):
        self.driver.get(url)
        log_in = self.driver.find_element(By.CSS_SELECTOR, "div[class*='css-1dbjc4n']>a")
        log_in.click()
        input_email = self.driver.find_element(By.CSS_SELECTOR, "input[autocomplete*='username']")
        input_email.send_keys(email + Keys.ENTER)

        try:
            input_username = self.driver.find_element(By.CSS_SELECTOR, "input[autocomplete*='username']")
            input_username.send_keys(username + Keys.ENTER)
        except NoSuchElementException:
            input_username = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid*='ocfEnterTextTextInput']")
            input_username.send_keys(username + Keys.ENTER)
        finally:
            input_password = self.driver.find_element(By.CSS_SELECTOR, "input[name*='password']")
            input_password.send_keys(password + Keys.ENTER)
        
        input_tweet = self.driver.find_element(By.CSS_SELECTOR, "div[class*='public-DraftStyleDefault-block']")
        input_tweet.send_keys(f"Hey internet provider, my internet speed for today is {self.down}down/{self.up}up.")
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, "div[data-testid*='tweetButtonInline']")
        tweet_button.click()
