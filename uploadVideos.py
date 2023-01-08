import time, os
import undetected_chromedriver as webdriver
# from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options



#options = Options()
options = webdriver.ChromeOptions()
profile = "Your profile of Chrome"
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
options.add_argument(f"--user-data-dir={profile}")
options.add_argument("--detach")

print("\033[1;31;40m IMPORTANT:Videos should be inside videos folder of the project and name should be like vid1.mp4, vid2.mp4...")
time.sleep(6)
answer = input("\033[1;32;40m Press 1 if you want to upload one video or Press 2 if you want to upload multiple videos: ")

if(int(answer) == 1):
    nameofvid = input("\033[1;33;40m Put the name of the video you want to upload (Ex: vid.mp4 or myshort.mp4 etc..) ---> ")
    howmany = input("\033[1;33;40m How many times you want to upload this video ---> ")

    for i in range(int(howmany)):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options, use_subprocess=True)
        driver.get("https://studio.youtube.com")
        time.sleep(3)
        upload_button = driver.find_element(By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()
        time.sleep(5)

        file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')
        simp_path = 'videos/{}'.format(str(nameofvid))
        abs_path = os.path.abspath(simp_path)
        file_input.send_keys(abs_path)

        time.sleep(7)

        next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
            time.sleep(5)

        done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]')
        done_button.click()
        time.sleep(5)
        driver.quit()

elif(int(answer) == 2):
    dir_path = '.\\videos'
    count = 0

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print("   ", count, " Videos found in the videos folder, ready to upload...")
    time.sleep(6)

    for i in range(count):
        chrome_options = webdriver.ChromeOptions()
        profile = "Your profile data "
        chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
        chrome_options.add_argument(f"--user-data-dir={profile}")
        chrome_options.add_argument("--detach")
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=chrome_options, use_subprocess=True)
       
        driver.get("https://studio.youtube.com")
        time.sleep(3)
        upload_button = driver.find_element(By.XPATH, '//*[@id="upload-icon"]')
        upload_button.click()
        time.sleep(5)

        file_input = driver.find_element(By.XPATH, '//*[@id="content"]/input')
        simp_path = 'videos/vid{}.mp4'.format(str(i+1))
        abs_path = os.path.abspath(simp_path)
        
        file_input.send_keys(abs_path)

        time.sleep(7)

        next_button = driver.find_element(By.XPATH, '//*[@id="next-button"]')
        for i in range(3):
            next_button.click()
            time.sleep(5)

        done_button = driver.find_element(By.XPATH, '//*[@id="done-button"]')
        done_button.click()
        time.sleep(5)
        driver.quit()




