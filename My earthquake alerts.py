import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import os
import base64

capabilities = dict(

   platformName = 'Android',
   deviceName = 'K5AXB600H485RD3',
   automationName = 'uiautomator2',
   appPackage = 'com.jrustonapps.myearthquakealerts',
   appActivity='.controllers.MainActivity',
   language='en',
   locale='US'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_My_earthquake(self) -> None:
        self.driver.start_recording_screen()

        # Notificação 1
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="OK"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="OK"]')
        el.click()

       # Notificação 2      
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.android.packageinstaller:id/permission_message"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="ALLOW"]')
        el.click()
        
        # Selecionar localidade logo ao abrir
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/titles"]')))
        actions = ActionChains(self.driver)
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/titles"]')
        el.click()          

        # Print 1
        directory = '%s/' % os.getcwd()
        file_name = 'screenshot-My_earthquake-1.png'
        self.driver.save_screenshot(directory + file_name)               

        #voltar para tela inicial
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Navigate up"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Navigate up"]')
        el.click()

        #Clicando em search
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/action_search"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/action_search"]')
        el.click()
         
        # Print 2
        file_name = 'screenshot-My_earthquake-2.png'
        self.driver.save_screenshot(directory + file_name)

        # escolher região 
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="android:id/text1"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="All Regions"]')
        el.click()
        
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@text="Asia"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Asia"]')
        el.click()

       #Data 1
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateFromText"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateFromText"]')
        el.click()

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="android:id/button1"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="android:id/button1"]')
        el.click()

        # Data 2
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateToText"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/dateToText"]')
        el.click()

        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="android:id/button1"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="android:id/button1"]')
        el.click()
        
         # Print 3
        file_name = 'screenshot-My_earthquake-3.png'
        self.driver.save_screenshot(directory + file_name)

        # escolher região 2
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@resource-id="com.jrustonapps.myearthquakealerts:id/titles"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@resource-id="com.jrustonapps.myearthquakealerts:id/titles"]')
        el.click()

        #voltar para tela inicial 2
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Navigate up"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Navigate up"]')
        el.click()

        #voltar para tela inicial 3
        WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Navigate up"]')))
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Navigate up"]')
        el.click()

        # Escolher localidade pelo maps
        #WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, '//*[@content-desc="Spain (1.80). 04:06: Canary Islands, Spain Region."]')))
        #el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Spain (1.80). 04:06: Canary Islands, Spain Region."]')
        #el.click()


       # Gravar tela
        filepath = os.path.join(directory, "screen_recording_My_earthquake.mp4")
        payload = self.driver.stop_recording_screen()
        with open(filepath, "wb") as fd:
            fd.write(base64.b64decode(payload))

        # Print 4
        file_name = 'screenshot-My_earthquake-4.png'
        self.driver.save_screenshot(directory + file_name) 

if __name__ == '__main__':
    unittest.main()
