
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


@ensure_execution
def tutorial_ok_btn(driver):
    driver.find_element_by_xpath('//*[@id="js_tutorialOkButton_quest"]').click()


@ensure_execution
def tutorial_reward_btn(driver):
    driver.find_element_by_xpath('//*[@id="js_tutorialOkButton_reward"]').click()


@ensure_execution
def close_ika_ads(driver):
    driver.find_element_by_xpath('//*[@id="multiPopup"]/div[2]/div[2]/a').click()


@ensure_execution
def research_advisor(driver):
    driver.find_element_by_xpath('//*[@id="js_GlobalMenu_research"]').click()


@ensure_execution
def cookies_accept(driver):
    driver.find_element_by_xpath('//*[@id="accept_btn"]').click()
