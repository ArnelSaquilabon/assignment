from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class SeleniumTest(StaticLiveServerTestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=options)
        self.browser.set_page_load_timeout(10)

    def tearDown(self):
        self.browser.close()

    def test_login(self):
        user_name = "arnelsaquilabon@gmail.com"
        password = "password"
        self.browser.get(self.live_server_url + "/login/")
        self.browser.find_element_by_id("username").send_keys(user_name)
        self.browser.find_element_by_id("password").send_keys(password)
        self.browser.find_element_by_class_name("btn").click()

        element = self.browser.find_element_by_tag_name('h1')

        self.assertEquals(
            element.text,
            "Welcome Arnel"
        )
