import time


def register(driver, mail, password):
    driver.find_element_by_xpath('//*[@id="loginRegisterTabs"]/ul/li[2]/span').click()

    # PASSES
    register_mail = driver.find_element_by_xpath('//*[@id="registerForm"]/div[1]/div/input')
    register_mail.send_keys('{}'.format(mail))
    register_password = driver.find_element_by_xpath('//*[@id="registerForm"]/div[2]/div/input')
    register_password.send_keys('{}'.format(password))

    # REGISTER
    driver.find_element_by_xpath('//*[@id="registerForm"]/p/button[1]/span').click()
    # if already registered
    time.sleep(1)
    try:
        driver.find_element_by_xpath('//*[@id="loginForm"]/p/button[1]/span').click()
    except:
        pass

    while 1:
        try:
            driver.find_element_by_xpath('//*[@id="joinGame"]/a/button/span').click()
            break
        except:
            time.sleep(0.01)
    try:
        driver.find_element_by_xpath('// *[ @ id = "serverlist"] / div / div[1] / div[2] / div[4] / div / div[8] / button').click()
        driver.switch_to.window(driver.window_handles[1])
    except:
        return False
