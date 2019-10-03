from selenium import webdriver
import selenium as selenium
import behaviour.login as login
import behaviour.register as register
from behaviour.tutorial import run_tutorial
from selenium.webdriver.common.keys import Keys
import behaviour.basic_actions as b_a
from selenium.webdriver.chrome.options import Options
import behaviour.advanced_actions as adv_act
import database_operations.database_operation as dtb
import time
import behaviour.intermidiate_actions as int_ac
from behaviour.IDs import buildings_dict


# this part allows to run through hidden browser
chrome_options = Options()
chrome_options.add_argument("--headless")


for i in range(5,66,1):
    driver = selenium.webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')#,chrome_options=chrome_options)
    driver.get('https://lobby.ikariam.gameforge.com/pl_PL/')
    driver.maximize_window()

    passes = dtb.select_bot(i,adress='database/bot_list.db')
    login.login(driver, passes[0], passes[1])


    # ACTION


    # TUTORIAL
    """
    if run_tutorial(driver, ads=True):
        coordinates = adv_act.get_location(driver)
        dtb.add_bot(bot_id=61,mail=username,password=password,location=coordinates, adress='database/bot_list.db')
        print('tutorial done', ' player: ', i)
    """
    driver.quit()