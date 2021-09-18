from selenium import webdriver
import time

url = [
	[
		"http://localhost/bot iklan/link1.html",
		"http://localhost/bot iklan/link2.html",
		"http://localhost/bot iklan/link3.html",
	],[
		"http://localhost/bot iklan/link4.html",
		"http://localhost/bot iklan/link5.html",
		"http://localhost/bot iklan/link6.html",
	]
];

driver = webdriver.Firefox(executable_path="D:\\driver\\geckodriver.exe");

for index, item in enumerate(url):			
	print(index)
	print("")
	for indexChild,itemChild in enumerate(item):
		driver.execute_script("window.open('" + itemChild + "')")
		print("URL : " + itemChild)				
		time.sleep(5)
		
	time.sleep(10)
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