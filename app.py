from selenium import webdriver
import selenium as selenium
import behaviour.login as login
import behaviour.basic_actions as basic_action
import behaviour.intermidiate_actions as inter_action
import behaviour.advanced_actions as advanced_action


driver = selenium.webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')
driver.get('https://lobby.ikariam.gameforge.com/pl_PL/')

username = 'gracz1@o2.pl'
password = 'haslo1'

login.login_process(driver, username, password)

# this makes active browser tab active
driver.switch_to.window(driver.window_handles[1])

# TUTORIAL

# island view
advanced_action.upgrade(driver, 'townHall')

