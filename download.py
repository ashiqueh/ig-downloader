from selenium import webdriver 
import time
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
import myparser 
#from selenium.webdriver.common.keys import keys
print("Don't forget to chcp 65001")


#print('Please enter the username')
#user = input()

with open('users.txt', 'r') as f:
	user = f.readline().strip()

driver = webdriver.Chrome('C:/webdrivers/chromedriver.exe')

print('Webdriver opened')
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-setuid-sandbox')


driver.get('https://www.instagram.com/'+ user +'/')
#assert "Python" in driver.title
print('Website opened')
#html = driver.execute_script('return document.documentElement.outerHTML')
#print (type(html))

#file_name = user + '.html'
#with open(file_name, "wb") as out:
#	out.write(html.encode('utf-8'))

print(driver.execute_script("return document.body.scrollHeight"))

next_page_path = "//a[@class='_oidfu']"
button = driver.find_element_by_xpath(next_page_path)
button.click()

#print(driver.execute_script("return document.body.scrollHeight"))

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

count = 0
max_height = 0

element_path = "//a[@class='_8mlbc _vbtk2 _t5r8b']"
element = driver.find_element_by_xpath(element_path)


#loads whole instagram page in selenium 

while (count < 3):
	#scroll down and then up again to load the next page
	element.send_keys(Keys.CONTROL, Keys.END)
	time.sleep(1) # give browser some time to load 
	element.send_keys(Keys.CONTROL, Keys.HOME)
	#store height in variable
	height = driver.execute_script("return document.body.scrollHeight")
	#max
	if (max_height == height):
		count += 1
	else:
		max_height = max(height,max_height)
		count = 0 

html = driver.execute_script('return document.documentElement.outerHTML') #html of final page 

htmlparser = myparser.IgParser()

htmlparser.feed(html)

#print(htmlparser.data) #should print the last link .. and it does! 



# class = "_8mlbc _vbtk2 _t5r8b"
# this is the class
# <a> with href = reference to picture


# from that page, we can extract the resource and download it :
# if there is a <meta> tag with property="og:video" then the resource is a video, .mp4
# if not, there is a <meta> tag with property = "og:image" and the resource is an image, .jpg 

# next page : <a class="_oidfu", href = next page 