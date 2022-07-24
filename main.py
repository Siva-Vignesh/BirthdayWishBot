import time
from datetime import datetime
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from prettytable import PrettyTable


def read_excel_and_collect_birthday_list():
    current_day = datetime.now().day
    current_month = datetime.now().month
    birthday_list = list()
    with open("birthday_database.csv", "r") as data:
        data.readline()  # this will remove the first row (header)
        for each_row in data.readlines():
            dob = each_row.split(",")[2]
            if int(dob.split("-")[0]) == int(current_day) and int(dob.split("-")[1]) == int(current_month):
                birthday_list.append({"name": each_row.split(',')[1], "ph_no": each_row.split(',')[3]})
    return birthday_list


def open_whatsapp_and_wish():
    option = webdriver.ChromeOptions()
    chrome_profile_path = "C:\\Users\\PC\\AppData\\Local\\Google\\Chrome\\User Data\\whatsAppProfile"
    option.add_argument(f"user-data-dir={chrome_profile_path}")
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe", options=option)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    table = PrettyTable(["No", "Name", "Status"])
    count = 0
    try:
        search_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')))
        for each_bd_member in bd_list:
            count += 1
            print(each_bd_member.get("ph_no"))
            search_box.clear()
            search_box.send_keys(each_bd_member.get("ph_no"))
            time.sleep(2)
            search_box.send_keys(Keys.RETURN)

            # this ensures if phone number not listed in whatsapplist
            try:
                tmp_box = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="pane-side"]/div[1]/div/span')))
                print(tmp_box.text)
            except TimeoutException:
                pass
            else:
                table.add_row([count, each_bd_member.get("name"), "Failed - Phone number not seen in whatsapp"])
                search_box.clear()
                continue

            try:
                message_box = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]')))
                message_box.send_keys(f"Auto message from python selenium - {each_bd_member.get('name')}")
                # message_box.send_keys(Keys.RETURN)
            except TimeoutException:
                table.add_row([count, each_bd_member.get("name"), "Failed - unable to find message box"])
            else:
                table.add_row([count, each_bd_member.get("name"), "Success"])
            search_box.clear()

    except TimeoutException:
        print(" Browser closed - Loading took too much time")

    time.sleep(5)  # delay added to give time so message will be sent before close the browser
    print(f"Report summary\n{table}")


if __name__ == "__main__":
    bd_list = read_excel_and_collect_birthday_list()
    if bd_list:
        open_whatsapp_and_wish()
    else:
        print("Oops!!.. Seems no friends having birthday today")
