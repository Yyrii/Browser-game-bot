
"""
Actions that requires basic actions, can be made from specific view
"""

from .basic_actions import *


@ensure_execution
def click_position(driver, position):
    city_view(driver)
    driver.find_element_by_xpath('//*[@id="position{}"]'.format(position)).click()


