#Selecionando site sky web_driver do chorme#
#Será necessário instalar pacotes para funcionar#
import time
from typing import Text
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Users/lucas/Desktop/Drivers./chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(15)

# Home Web
driver.get('https://www.sky.com.br/')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_YQcCxObpxg0J"]/div/div[2]/div/div[2]/div/div/div/div[1]/button').click()
driver.find_element_by_xpath('//*[@id="wrap-aviso-cookie"]/div[1]/div/div/div/div[3]/div/div/button').click()
driver.find_element_by_xpath('//*[@id="main-menu"]/div[2]/div[2]/ul[1]/li[3]/a').click()
time.sleep(2)

# Entra na programação
driver.find_element_by_xpath('//*[@id="portlet_com_liferay_journal_content_web_portlet_JournalContentPortlet_INSTANCE_aKJUz209eKa8"]/div/div[2]/div/div[2]/section/div/div[1]/div/div/a[2]/div').click()

# Inseri nome para buscar canal 
driver.find_element_by_id('searchChannel').send_keys("band")
time.sleep(5)

print(driver.title)

print('BAND')

driver.quit()