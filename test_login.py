import unittest
from selenium import webdriver

class TestUIExample(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r"C:\Windows\System32\test_automation_frameworks\tests\api\chromedriver.exe")
        self.driver.maximize_window()

    def test_homepage_loads(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertEqual(driver.title, "Python Website")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
