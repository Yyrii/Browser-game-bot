from selenium import webdriver
import selenium as selenium
import behaviour.login as login
import behaviour.basic_actions as basic_action
import behaviour.intermidiate_actions as inter_action
import behaviour.advanced_actions as advanced_action
import behaviour.register as register


driver = selenium.webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')
driver.get('https://lobby.ikariam.gameforge.com/pl_PL/')
driver.maximize_window()

username = 'yjfqghcrzk@o2.pl'
password = 'haslo3'

register.register(driver, username, password)

# this makes active browser tab active
#driver.switch_to.window(driver.window_handles[1])

# TUTORIAL
import time
basic_action.cookies_accept(driver)
basic_action.close_ika_ads(driver)
basic_action.tutorial_ok_btn(driver)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
advanced_action.set_sawmill_workers(driver,20)
time.sleep(0.5)
basic_action.city_view(driver)
basic_action.tutorial_reward_btn(driver)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
advanced_action.build(driver, 'academy')
basic_action.tutorial_reward_btn(driver)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
inter_action.speedup_build_time(driver, 'academy')
time.sleep(0.5)
inter_action.speedup_build_time(driver, 'academy')
basic_action.tutorial_reward_btn(driver)
time.sleep(0.5)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
# research
advanced_action.make_reserach(driver,1,1)
basic_action.tutorial_reward_btn(driver)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
time.sleep(0.5)
advanced_action.set_scientist(driver, 8)
basic_action.tutorial_reward_btn(driver)
time.sleep(0.5)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
# warehouse
advanced_action.build_warehouse(driver, 7) # first warehouse
basic_action.tutorial_reward_btn(driver)
basic_action.tutorial_popup(driver)
basic_action.tutorial_ok_btn(driver)
time.sleep(0.5)
inter_action.speedup_build_time(driver, 'warehouse')
time.sleep(0.5)
inter_action.speedup_build_time(driver, 'warehouse')
basic_action.tutorial_reward_btn(driver)