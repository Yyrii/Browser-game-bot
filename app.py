from selenium import webdriver
import selenium as selenium
import behaviour.login as login
import behaviour.basic_actions as basic_action
import behaviour.intermidiate_actions as inter_action
import behaviour.advanced_actions as advanced_action
import behaviour.register as register
from behaviour.tutorial import run_tutorial
from selenium.webdriver.common.keys import Keys


driver = selenium.webdriver.Chrome(executable_path='E:\chromedriver\chromedriver.exe')
driver.get('https://lobby.ikariam.gameforge.com/pl_PL/')
driver.maximize_window()

username = 'test1@o2.pl'
password = 'haslo3'

register.register(driver, username, password)

# TUTORIAL
run_tutorial(driver)

#driver.quit()
