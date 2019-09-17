
"""
Actions that require specific view, which "intermidiate actions" ensure
"""

from .intermidiate_actions import *
from .IDs import buildings_dict, plunder_army_id
from selenium.common.exceptions import *
import selenium


def build(driver, building_name):
    try:
        click_building_position(driver, buildings_dict[building_name])
    except:
        element = driver.find_element_by_xpath('//*[@id="worldmap"]')
        driver.execute_script("arguments[0].setAttribute('style','left: -2000px; top: -400px; transform: scale(0.6)')",element)
        time.sleep(1)
        click_building_position(driver, buildings_dict[building_name])

    time.sleep(2)
    for i in range(10):
        time.sleep(0.1)
        try:
            driver.find_element_by_xpath('//*[@id="js_{}BuildButton"]'.format(building_name)).click()
            break
        except ElementNotInteractableException:
            driver.find_element_by_xpath('//*[@id="buildingGround"]/div[2]/div[1]/div[3]').click()


def build_warehouse(driver, warehouse_id):  # notice: war_id has to be 5, 6, 7 or 8
    click_building_position(driver, warehouse_id)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="js_{}BuildButton"]'.format('warehouse')).click()


# IMPORTANT: tutorial must be turned off
def upgrade(driver, building_name):
    try:
        click_building_position(driver, buildings_dict[building_name])
    except:
        element = driver.find_element_by_xpath('//*[@id="worldmap"]')
        driver.execute_script("arguments[0].setAttribute('style','left: -2000px; top: -400px; transform: scale(0.6)')",element)
        time.sleep(1)
        click_building_position(driver, buildings_dict[building_name])
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
    for i in range(3):
        driver.find_element_by_xpath('//*[@id="researchAdvisor"]/div[2]/div[1]/div[3]').click()
    driver.find_element_by_xpath('//*[@id="js_researchAdvisorConservationLink"]').click() # made research
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="researchAdvisor"]/div[1]/div[2]').click() #close


def set_scientist(driver, scientist_num):
    click_building(driver,'academy')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="inputScientists"]').send_keys('{}'.format(scientist_num))
    driver.find_element_by_xpath('//*[@id="inputWorkersSubmit"]').click()


# oszczepnicy 1, procarze 2.
def recruit_army(driver, unit_id, amount):
    click_building(driver, 'barracks')
    time.sleep(0.5)
    for i in range(10):
        try:
            driver.find_element_by_xpath('//*[@id="js_barracksBuyTextfield{}"]'.format(unit_id)).send_keys('{}'.format(amount))
            break
        except NoSuchElementException:
            driver.find_element_by_xpath('// *[ @ id = "barracks"] / div[2] / div[1] / div[3]').click()
        except ElementNotInteractableException:
            driver.find_element_by_xpath('// *[ @ id = "barracks"] / div[2] / div[1] / div[3]').click()
    for i in range(10):
        try:
            driver.find_element_by_xpath('//*[@id="button_recruit"]').click() # submit
            break
        except ElementNotInteractableException:
            driver.find_element_by_xpath('//*[@id="barracks"]/div[2]/div[1]/div[1]').click()
        except StaleElementReferenceException:
            driver.find_element_by_xpath('//*[@id="barracks"]/div[2]/div[1]/div[1]').click()
        except ElementClickInterceptedException:
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="barracks"]/div[2]/div[1]/div[1]').click()

def buy_cargo_ship(driver):
    click_building(driver, 'port')
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="js_tabBuyTransporter"]/b').click()
    time.sleep(1)
    driver.find_element_by_xpath('// *[ @ id = "js_buyTransporterAction"]').click()
    driver.find_element_by_xpath('// *[ @ id = "port"] / div[1] / div[2]').click()


def attack_barbarians(driver,cargo_ships,**kwargs):
    island_view(driver)
    click_barbarians(driver)
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="js_islandBarbarianPlundering"]').click() # plądrowanie
    except:
        element = driver.find_element_by_xpath('//*[@id="sidebar"]')
        driver.execute_script("arguments[0].setAttribute('style','left: 206px; top: 230px; right: auto;'", element)
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="js_islandBarbarianPlundering"]').click()
    try:
        for el in kwargs.items():
            time.sleep(0.3)
            # sending specyfic amount of specific soldiers
            driver.find_element_by_xpath('//*[@id="cargo_army_{}"]'.format(plunder_army_id[el[0]])).send_keys('{}'.format(el[1]))
            time.sleep(0.3)
            driver.find_element_by_xpath(' // *[ @ id = "extraTransporter"]').send_keys('{}'.format(cargo_ships))

        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="plunderbutton"]').click()
    except:
        pass
