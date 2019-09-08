
"""
Actions that require specific view, which "intermidiate actions" ensure
"""

from .intermidiate_actions import *
from .buildings_id import buildings_dict
import selenium


def build(driver, building):
    click_position(driver, buildings_dict[building])
    time.sleep(3)
    try:
        driver.find_element_by_xpath('//*[@id="js_{}BuildButton"]'.format(building)).click()
    except Exception as exc:
        print(exc)


def build_warehouse(driver, war_id):  # notice: war_id has to be 5, 6, 7 or 8
    click_position(driver, war_id)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="js_{}BuildButton"]'.format('warehouse'))


# IMPORTANT: tutorial must be turned off
def upgrade(driver, building):
    click_position(driver, buildings_dict[building])
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="js_buildingUpgradeButton"]').click()
