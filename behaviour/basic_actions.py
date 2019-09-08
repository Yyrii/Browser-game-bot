
"""
Actions that can be made from any place
"""

from .ensure_execution import *


@ensure_execution
def city_view(driver):
    driver.find_element_by_xpath('//*[@id="js_cityLink"]/a').click()


@ensure_execution
def island_view(driver):
    driver.find_element_by_xpath('//*[@id="js_islandLink"]/a').click()


@ensure_execution
def world_view(driver):
    driver.find_element_by_xpath('//*[@id="js_worldMapLink"]/a').click()


@ensure_execution
def tutorial_popup(driver):
    driver.find_element_by_xpath('//*[@id="advisorImage"]').click()





