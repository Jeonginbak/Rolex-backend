import csv
import time
from selenium import webdriver


driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.rolex.com/ko/watches/find-rolex.html#p=1')
time.sleep(2)


man = driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[1]/div/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/section[1]/ul/li[1]/button/figure').click()

for page_idx in range(0,3):
	driver.get(f'https://www.rolex.com/ko/watches/find-rolex.html#p={page_idx}')
	
	# 남성용 시계 필터 클릭
	man = driver.find_element_by_xpath('//*[@id="page"]/div/div[2]/div[1]/div/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[1]/div/div/div/section[1]/ul/li[1]/button/figure').click()

	man_list = driver.find_elements_by_xpath('//*[@id="page"]/div/div[2]/div[1]/div/div[1]/div[6]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/ul/li')

	for man in man_list:
		collection_name = man.find_element_by_class_name('sc-fznMnq').text
		print(collection_name)







#driver.quit()
