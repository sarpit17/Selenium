from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
mail=driver.find_element(By.LINK_TEXT,"mentor@rahulshettyacademy.com").text

driver.switch_to.window(windows[0])
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(mail)
driver.find_element(By.CSS_SELECTOR,"#password").send_keys("1234")
driver.find_element(By.CSS_SELECTOR,".checkmark").click()

option=Select(driver.find_element(By.XPATH,"//div/select"))
option.select_by_visible_text("Student")

driver.find_element(By.CSS_SELECTOR,".text-info").click()
driver.find_element(By.NAME,"signin").click()
op=driver.find_element(By.NAME,"signin").click()
wait=WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, '.alert-danger').text)
