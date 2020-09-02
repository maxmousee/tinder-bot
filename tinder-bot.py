from selenium import webdriver
from selenium.webdriver.common import keys
from time import sleep

from secrets import username, password


class TinderBot():
    def __init__(self):
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = True
        caps['enableNetwork'] = True
        self.driver = webdriver.Chrome(desired_capabilities=caps)
        self.action = webdriver.ActionChains(self.driver)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        accept_cookies_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button')
        accept_cookies_btn.click()

        sleep(2)

        fb_login_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_login_btn.click()

        sleep(2)

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        sleep(5)

        self.driver.switch_to.window(base_window)

        sleep(2)

        enable_location_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        enable_location_btn.click()

        sleep(2)

        self.driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
            "latitude": 52.379189,
            "longitude": 4.899431,
            "accuracy": 100
        })

        disable_notifications_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        disable_notifications_btn.click()

        sleep(15)

    def like(self):
        self.action.send_keys(keys.Keys.ARROW_RIGHT)
        self.action.perform()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()


bot = TinderBot()
bot.login()
bot.auto_swipe()
