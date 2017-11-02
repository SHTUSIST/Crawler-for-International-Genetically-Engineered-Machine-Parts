# Before using, you should install "selenium". You can use "pip install selenium" to do this.
# Also, you should download and install chrome driver. You can follow the below link 
# http://blog.csdn.net/u012359618/article/details/52556127

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

def part(x):
	driver.get("https://www.google.com")
	driver.implicitly_wait(5)
	driver.find_element_by_css_selector("input[id='lst-ib']").send_keys(x," site:parts.igem.org",Keys.ENTER)
	driver.implicitly_wait(5)
	

	while driver.find_elements_by_xpath('//*[@id="pnnext"]/span[2]'):

		# important!!!
		driver.implicitly_wait(5)
		links=driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")
		

		for link in links:
			url=link.get_attribute('href')
			
			text=link.text
			b=text.find("-")
			if ":" in text:
				a=text.find(":")
				text2=text[a+1:b-1]
			else:
				text2=text[:b-1]
			txt=text2+".txt"
			print(txt)


			driver2=webdriver.Chrome()
			driver2.get(url)
			
			try:
				driver2.implicitly_wait(10)
				driver2.find_elements_by_xpath('//*[@id="sequencePaneDiv"]/div[1]/span[9]')[0].click()
				f=open(txt,'w') 
				f.write(driver2.find_elements_by_xpath("/html/body/pre")[0].text)
				f.close()
				driver2.quit()
			except:
				driver2.quit()
				print("meet bug, and skip to the next page")

		driver.find_elements_by_xpath('//*[@id="pnnext"]/span[2]')[0].click()


	links=driver.find_elements_by_xpath("//h3[@class='r']/a[@href]")
	for link in links:
		url=link.get_attribute('href')
		
		text=link.text
		b=text.find("-")
		if ":" in text:
			a=text.find(":")
			text2=text[a+1:b-1]
		else:
			text2=text[:b-1]
		txt=text2+".txt"
		print(txt)


		driver2=webdriver.Chrome()
		driver2.get(url)
		
		try:
			driver2.implicitly_wait(10)
			driver2.find_elements_by_xpath('//*[@id="sequencePaneDiv"]/div[1]/span[9]')[0].click()
			f=open(txt,'w') 
			f.write(driver2.find_elements_by_xpath("/html/body/pre")[0].text)
			f.close()
			driver2.quit()
		except:
			driver2.quit()
			print("meet bug, and skip to the next page")





# input the key word
part("lasR")

