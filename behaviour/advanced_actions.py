
"""
Actions that require specific view, which "intermidiate actions" ensure
"""

from .intermidiate_actions import *
from .buildings_id import buildings_dict
import selenium


def build(driver, building):
    click_building_position(driver, buildings_dict[building])
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="js_{}BuildButton"]'.format(building)).click()
    except Exception as exc:
        print(exc)


def build_warehouse(driver, warehouse_id):  # notice: war_id has to be 5, 6, 7 or 8
    click_building_position(driver, warehouse_id)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="js_{}BuildButton"]'.format('warehouse')).click()


# IMPORTANT: tutorial must be turned off
def upgrade(driver, building):
    click_building_position(driver, buildings_dict[building])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="js_buildingUpgradeButton"]').click()


def set_sawmill_workers(driver, amount_of_workers):
    click_sawmill(driver)
    time.sleep(2)
    workers_number = driver.find_element_by_xpath('//*[@id="inputWorkers"]')
    workers_number.send_keys('{}'.format(amount_of_workers))
    time.sleep(0.1)
    driver.find_element_by_xpath('//*[@id="inputWorkersSubmit"]').click()
    time.sleep(0.2)
    driver.find_element_by_xpath('// *[ @ id = "resource"] / div[1] / div[2]').click()
    return

# first research - num 1, 2nd - 2 exc.
def make_reserach(driver, field_of_research, invention_number):
    choose_field_of_study(driver, field_of_research)
    time.sleep(0.5) #chose research
    driver.find_element_by_xpath('//*[@id="js_researchAdvisorCurrResearchesArr"]/li[{}]/a'.format(invention_number)).click()
    time.sleep(0.5)
    for i in range(4):
        driver.find_element_by_xpath('//*[@id="researchAdvisor"]/div[2]/div[1]/div[3]').click()
    driver.find_element_by_xpath('//*[@id="js_researchAdvisorConservationLink"]').click() # made research
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="researchAdvisor"]/div[1]/div[2]').click() #close


def set_scientist(driver, scientist_num):
    click_building(driver,'academy')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="inputScientists"]').send_keys('{}'.format(scientist_num))
    driver.find_element_by_xpath('//*[@id="inputWorkersSubmit"]').click()

