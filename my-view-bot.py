from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

url = [
	[
		"https://www.youtube.com/watch?v=pZ1UTRE_jmA",
		"https://www.youtube.com/watch?v=i2mF9DsjOZI",
		"https://www.youtube.com/watch?v=jJyD6Md6Dfs",
		"https://www.youtube.com/watch?v=tVDtj0hD7Ms"
	],[
		"https://www.youtube.com/watch?v=LurlNwa-uJo",
		"https://www.youtube.com/watch?v=WuKolk-p3nQ",
		"https://www.youtube.com/watch?v=TxICB8YGJmU",
		"https://www.youtube.com/watch?v=NNWEqMXnP68",
		"https://www.youtube.com/watch?v=8NRc6RuFtaw&t=41s"
	]
];

driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe");

for index, item in enumerate(url):			
	print(index)
	print("")
	for indexChild,itemChild in enumerate(item):
		driver.execute_script("window.open('" + itemChild + "')")
		print("URL : " + itemChild)					
		driver.switch_to.window(driver.window_handles[indexChild+1]);
		WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Play (k)']"))).click()
		time.sleep(5)
	
	time.sleep(180)
	driver.switch_to.window(driver.window_handles[1])
	driver.execute_script("window.close()")
	time.sleep(3)
	driver.switch_to.window(driver.window_handles[1])
	driver.execute_script("window.close()")
	time.sleep(3)
	driver.switch_to.window(driver.window_handles[1])
	driver.execute_script("window.close()")
	time.sleep(3)
	driver.switch_to.window(driver.window_handles[0])

time.sleep(5);
driver.quit();

print("DONE")