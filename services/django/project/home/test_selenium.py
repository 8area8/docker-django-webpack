"""Selenium tests."""

from django.test import TestCase, tag
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


class SeleniumTest(TestCase):
    """Base selenium class."""

    @tag('selenium')
    def setUp(self):
        """Before method."""
        self.selenium = webdriver.Remote(
            command_executor='http://selenium_hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME
        )
        print("ok")

    @tag('selenium')
    def test_button(self):
        """Main."""
        selenium = self.selenium
        # Opening the link we want to test
        selenium.get('https://nginx/')

        assert selenium.title == 'La Crèche Humaniste - Home'

        try:
            selenium.find_element_by_class_name('colored')
        except NoSuchElementException:
            pass
        else:
            raise ".colored is set in loading."

        button = selenium.find_element_by_id('selenium-test')
        button.click()

        assert selenium.find_element_by_class_name('colored')
        button.click()

        try:
            selenium.find_element_by_class_name('colored')
        except NoSuchElementException:
            pass
        else:
            raise ".colored is set after the 2nd click."
