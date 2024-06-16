import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
import random
import time
import string
import random 
import json
import sys, os
import time



class Bot():
    def __init__(self):
        #crete posting channel 
        #assign content type 
        #gen and save wrapper and numb as class vars"'

        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        # service = ChromeService('chromedriver.exe')
        driver = webdriver.Chrome(options=chrome_options)

        chars = list(string.ascii_letters) + list(string.digits)
        name_list = [chars[random.randint(0,53)] for _ in range(15)]
        username = "".join(str(letter) for letter in name_list)
        birthday = f"0{random.randint(1,9)} {random.randint(1,12)} {random.randint(1975,2017)}"
        gender = "1"
        passlist = []
        for i in range(20):
            if i==6:
                pick = "A"
            if i==7:
                pick = "1"
            if i==8:
                pick = "!"
            else:
                pick = chr(random.randint(32,127))
            passlist.append(pick)
        password = "".join(str(letter) for letter in passlist)
        with open("cred.json","w") as f:
            json.dump([{username : password}],f)
        
        ##########

        try:
            driver.get("https://accounts.google.com/signup/v2/createaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

            # Fill in name fields
            first_name = driver.find_element(By.NAME, "firstName")
            last_name = driver.find_element(By.NAME, "lastName")
            first_name.clear()
            first_name.send_keys(username)
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
            next_button.click()

            # Wait for birthday fields to be visible
            wait = WebDriverWait(driver, 20)
            day = wait.until(EC.visibility_of_element_located((By.NAME, "day")))

            # Fill in birthday
            birthday_elements = birthday.split()
            month_dropdown = Select(driver.find_element(By.ID, "month"))
            month_dropdown.select_by_value(birthday_elements[1])
            day_field = driver.find_element(By.ID, "day")
            day_field.clear()
            day_field.send_keys(birthday_elements[0])
            year_field = driver.find_element(By.ID, "year")
            year_field.clear()
            year_field.send_keys(birthday_elements[2])

            # Select gender
            gender_dropdown = Select(driver.find_element(By.ID, "gender"))
            gender_dropdown.select_by_value(gender)
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
            next_button.click()

        # Create custom email
            time.sleep(2)
            if driver.find_elements(By.ID, "selectionc4") :
                create_own_option = wait.until(EC.element_to_be_clickable((By.ID,"selectionc4") ))
                create_own_option.click()
            
            create_own_email = wait.until(EC.element_to_be_clickable((By.NAME, "Username")))
            username_field = driver.find_element(By.NAME, "Username")
            username_field.clear()
            username_field.send_keys(username)
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
            next_button.click()
            
            # Enter and confirm password
            password_field = wait.until(EC.visibility_of_element_located((By.NAME, "Passwd")))
            password_field.clear()
            password_field.send_keys(password)
            # Locate the parent div element with the ID "confirm-passwd"
            confirm_passwd_div = driver.find_element(By.ID, "confirm-passwd")
            #Find the input field inside the parent div
            password_confirmation_field = confirm_passwd_div.find_element(By.NAME, "PasswdAgain")
            password_confirmation_field.clear()
            password_confirmation_field.send_keys(password)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "VfPpkd-LgbsSe")))
            time.sleep(10)
            next_button = driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe")
            next_button.click()

            # Skip phone number and recovery email steps
            skip_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            for button in skip_buttons:
                button.click()

            # Agree to terms
            agree_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button span.VfPpkd-vQzf8d")))
            agree_button.click()

            print(f"Your Gmail successfully created:\n{{\ngmail: {username}@gmail.com\npassword: {password}\n}}")

        except Exception as e:
            print("Failed to create your Gmail, Sorry")
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
        finally:
            driver.quit()


    def short():
        ##draw from relevent clips bin 
        ###maybe make clips subset of long form vid
        ##post
        pass
    def vid():
        ##random clips from **sub bin** 
        ##name = wrapper + subbin name + number
        ##post
        pass


##TODO maxout api calls on popular content and pool into bins (general content type) and sub bins (sub genere i.e exact game )
class Scraper():
    def __int__():
        ##init names / tokens /  passwords
        pass
    def twitch():
        ##get popular streams and classify bin and sub-bin 
        ##(or scrape given specified types whichever is esier)
        pass
    def yt():
        ##same for yt
        pass
    def insta():
        ##memes / shorts repost maybe 
        pass
    def forward():
        ##scape all at max rate 
        ##classify / make metadata (prob json)
        ##store 
        pass


def Twitch(Sub_Name):
    client_id = None
    client_secret = None

    # Get OAuth token
    response = requests.post('https://id.twitch.tv/oauth2/token', params={
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    })

    response.raise_for_status()
    access_token = response.json()['access_token']

    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }

    # Example: Get videos from a specific user
    user_login = Sub_Name
    response = requests.get(f'https://api.twitch.tv/helix/users', headers=headers, params={'login': user_login})
    response.raise_for_status()
    user_id = response.json()['data'][0]['id']

    # Get videos of the user
    videos_response = requests.get(f'https://api.twitch.tv/helix/videos', headers=headers, params={'user_id': user_id, 'first': 100})
    videos_response.raise_for_status()
    videos = videos_response.json()['data']

    video_urls = [video['url'] for video in videos]



if __name__ == "__main__":
    bot1 = Bot()