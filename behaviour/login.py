import time


def login_process(driver, username, password):
    driver.find_element_by_xpath('//*[@id="loginRegisterTabs"]/ul/li[1]/span').click()

    # PASSES
    login_name = driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div/input')
    login_name.send_keys('{}'.format(username))
    login_password = driver.find_element_by_xpath('//*[@id="loginForm"]/div[2]/div/input')
    login_password.send_keys('{}'.format(password))

    #LOGIN
    driver.find_element_by_xpath('//*[@id="loginForm"]/p/button[1]/span').click()

    #PLAY
    while 1:
        try:
            driver.find_element_by_css_selector('#joinGame > a > button > span').click()
            break
        except:
            time.sleep(0.01)

    try:
        driver.find_element_by_xpath('//*[@id="accountlist"]/div/div[1]/div[2]/div/div/div[11]/button/span').click()
        return True
    except:
        return False

