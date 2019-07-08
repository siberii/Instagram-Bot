import time
import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        self.bot.get(
            "https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
        # Leave time for page load
        time.sleep(1)
        username = self.bot.find_element_by_name("username")
        password = self.bot.find_element_by_name("password")
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def remove_pop_up(self):
        try:
            pop_up = self.bot.find_element_by_class_name(
                "_7UhW9.x-6xq.yUEEX.KV-D4.uL8Hv")
            not_now_boutton = self.bot.find_element_by_class_name(
                "aOOlW.HoLwm")
            not_now_boutton.click()
        except:
            print("No pop-up was found.")
            return

    def like_post(self):
        hashtag = "conding"
        self.bot.get(
            f"https://www.instagram.com/explore/tags/{hashtag}/?hl=en")
        time.sleep(3)
        for i in range(1, 10):
            self.bot.execute_script(
                "window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(3)

        posts = self.bot.find_elements_by_class_name("v1Nh3.kIKUG._bz0w")
        links = [post.find_element_by_tag_name(
            'a').get_attribute("href") for post in posts]
        print(links)
        print(len(links))
        for link in links:
            self.bot.get(link)
            try:
                self.bot.find_element_by_class_name(
                    "dCJp8.afkep._0mzm-").click()
                time.sleep(3)
            except:
                time.sleep(60)


username = input("What is your Instagram username or email? : ")
print("What's your password? (Your password will be hidden.) : ")
try:
    password = getpass.getpass()
except Exception as error:
    print('ERROR', error)

# TODO: Check if login infos are valid

ig_bot = InstagramBot("username", "password")
ig_bot.login()
ig_bot.remove_pop_up()
ig_bot.like_post()
