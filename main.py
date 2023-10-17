import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.keys import Keys
import TakePromptByAudio as tpba
import tkinter as tk
from googletrans import Translator
import keyboard
import time

import undetected_chromedriver as uc

continue_program = True

delete_prompt = False

delete_choice = input("Would you like to delete prompt from your account after program is finished(Yes/No):")

while delete_choice.lower() != "yes" and delete_choice.lower() != "no":
    delete_choice = input("Choose One Of The Above Choices:")

if delete_choice.lower() == "yes" : delete_prompt = True

try:
    prompt = tpba.Take_Data()
    print("Gpt Answering...\n\n")

    explorer = uc.Chrome(use_subprocess = True)
    explorer.maximize_window()
    explorer.get("https://chat.openai.com/auth/login")

    cookies = pickle.load(open("gptcookies.pkl", "rb"))

    for cookie in cookies:
        cookie["domain"] = ".openai.com"
        try:
            explorer.add_cookie(cookie)

        except:
            pass

    explorer.get("https://chat.openai.com/")
    explorer.implicitly_wait(15)
    time.sleep(5)
    try:
        buttons = explorer.find_elements(By.XPATH, '//*[@class="flex w-full gap-2 items-center justify-center"]')
        buttons[-1].click()
    except:
        pass

    #WebDriverWait(explorer, 5).until(Ec.visibility_of_element_located((By.XPATH, '//*[@id="radix-:ro:"]/div[2]/div/div[4]/button/div'))).click()
    number = 2


    while continue_program:
        WebDriverWait(explorer,10).until(Ec.visibility_of_element_located((By.CSS_SELECTOR,'#prompt-textarea'))).send_keys(prompt, Keys.ENTER)

        WebDriverWait(explorer,90).until(Ec.visibility_of_element_located((By.XPATH,  f'//*[@id="__next"]/div[1]/div[2]/main/div[1]/div[1]/div/div/div/div[{number}]/div/div/div[2]/div/div[2]/div/button'))).click()

        root = tk.Tk()

        if delete_prompt:
            WebDriverWait(explorer,10).until(Ec.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/div/div/div/nav/div[3]/div/div/span[1]/div[1]/ol/li/a/div[2]/button[2]'))).click()
            keyboard.press_and_release("Enter")

        data = root.clipboard_get()
        translator = Translator()

        chosen_language = tpba.Chosen_Language()

        print(translator.translate(data, dest = chosen_language).text)
        print("\n\n\n")

        continue_choice = input("1-Continue The Program\n2-Close The Program\nMake Your Choice:")
        while continue_choice != "1" and continue_choice != "2" : print("Choose one of the above choices:")

        if continue_choice == "2" : continue_program = False

        if continue_choice == "1":
            prompt = tpba.Take_Data()
            print("Gpt Answering...\n\n")
            if delete_prompt == False : number += 2

    explorer.close()

except Exception:
    pass
