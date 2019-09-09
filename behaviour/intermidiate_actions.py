
"""
Actions that requires basic actions, can be made from specific view
"""

from .basic_actions import *
from .buildings_id import buildings_dict


def click_building_position(driver, position):
    city_view(driver)
    driver.find_element_by_xpath('// *[ @ id = "js_CityPosition{}Link"]'.format(position)).click()


def click_building(driver, building_name):
    city_view(driver)
    driver.find_element_by_xpath('//*[@id="position{}"]'.format(buildings_dict[building_name])).click()


@ensure_execution
def click_sawmill(driver):
    island_view(driver)
    driver.find_element_by_xpath('// *[ @ id = "js_islandResourceLink"]').click()


def speedup_build_time(driver, building):
    try:
        driver.find_element_by_xpath('//*[@id="js_CityPosition{}SpeedupButton"]'.format(buildings_dict[building])).click()
        time.sleep(0.5)
        driver.find_element_by_xpath('// *[ @ id = "js_buildingSpeedupActivateBtn"]').click()
    except:
        return


# 0 - żegluga, 1 - gospodarka, 2 - nauka, 3 - wojsko
@ensure_execution
def choose_field_of_study(driver, type):
    research_advisor(driver)
    driver.find_element_by_xpath('//*[@id="js_researchAdvisorChangeResearchType{}"]'.format(type)).click()



