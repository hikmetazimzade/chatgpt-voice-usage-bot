from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pickle
import keyboard

import undetected_chromedriver as uc

email = input("Input Your Email:")
password = input("Input Your Password:")

try:
    if __name__ == '__main__':
        explorer = uc.Chrome(use_subprocess = True)
        explorer.maximize_window()

        explorer.get("https://chat.openai.com/auth/login?next=%2F")
        explorer.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[2]/div[1]/div/button[1]/div').click()


        WebDriverWait(explorer,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="username"]'))).send_keys(email, Keys.ENTER)#email element
        WebDriverWait(explorer,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="password"]'))).send_keys(password, Keys.ENTER)#password element

        time.sleep(2)
        keyboard.press_and_release("Enter")


        time.sleep(1)
        cookies = explorer.get_cookies()
        pickle.dump(cookies,open("gptcookies.pkl","wb"))

        time.sleep(1)
        explorer.close()

except:
    pass