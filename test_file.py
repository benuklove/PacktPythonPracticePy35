# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re


class Loves(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://www.loves.com/")
        self.selenium.start()

    def test_loves(self):
        sel = self.selenium
        sel.open("/en/location-and-fuel-price-search/locationsearchresults#?state=All")
        sel.click("//div[@id='welcomePopup']/ul/li[2]/a/div")
        sel.click("link=Export")
        sel.wait_for_page_to_load("30000")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
