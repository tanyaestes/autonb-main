from selenium import webdriver


def seleniumSetup():
#    browser = webdriver.Chrome('/Users/chromedriver') #might have to point to a different location
    service = webdriver.ChromeService(executable_path= '/Users/chromedriver')
    browser = webdriver.Chrome(service=service)

# the following two lines are used for Safari
#    browser = webdriver.Safari()
#    browser.maximize_window()
    return browser


