from selenium import webdriver 
import time
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
import myparser
import os
import urllib.request

'''
TODO : organize pictures by date 

'''

print("Don't forget to chcp 65001") #reminder to change shell text encoding so the program doesn't crash when testing

print('Please enter the username')

user = input()
#with open('users.txt', 'r') as f:
#	user = f.readline().strip()

path = 'dl/' + user + '/' #makes directory with desired username to save the media 

if not os.path.exists(path):
	os.makedirs(path) # make dl directory

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

#print(htmlparser.data) #should print a list of all links .. and it does! 

# now we can load each url into the driver
# and download the pictures after
list_of_pictures = htmlparser.data

loc = path + 'list_of_resources.txt'
with open(loc,'w') as out: #i do this just in case there's some unforeseen error, you still have the work done so far saved
	for item in list_of_pictures:
		out.write('%s\n' % item)
	out.close()

resources = []

#use urllib.request to get this stuff... man i'm dumb hahahahaha 


#with path + 'resources.txt' as loc, open(loc,'a') as out: #same reason 

loc = path + 'resources.txt'
out = open(loc, 'w')

for idx,picture in enumerate(list_of_pictures):
	if idx % 5 == 0:
		print('Fetching resource #%d.' % idx)
	try:
		resp = urllib.request.urlopen(picture)
	except Exception as e:
		print('Unable to retrieve resource: %s' % picture)
	html = bytes.decode(resp.read())
	#driver.get(picture) # loads picture into web driver
	#html = driver.execute_script('return document.documentElement.outerHTML') #html of final page 
	htmlparser.feed(html)
	out.write('%s\n' % htmlparser.current_resource) # writes resource locations as they're retrieved so in case there's a crash

out.close()

print('abc')

print(htmlparser.resources) # prints out list of all resources on page

print('def')

resources = htmlparser.resources

#with path + 'resources.txt' as loc, open(loc,'wb') as out: #same reason 
#	for item in resources:
#		out.write('%s\n' % item)

#resources = input() # delete this after

#downloads resources 
for idx,resource in enumerate(resources):
	if idx % 5 == 0:
		print('Downloading resource #%d.' % idx)
	file_name = path + resource.split('/')[-1] # everything after the last backslash
	#urllib.request.urlretrieve(resource,file_name) # not gonna use urlretrieve for now 
	while not os.path.isfile(file_name): #not sure why, but sometimes takes multiple tries for resource, this works for now 
		try:
			resp = urllib.request.urlopen(resource)
			output = open(file_name, 'wb')
			output.write(resp.read())
			output.close()
		except Exception as e:
			print('There was an error downloading the resource at: ' + resource + '. Retrying now...')
			#print(e.fp.read()) # print http error if it happens
			print(resource)
			loc = path + '400.txt'
			with open(loc, 'a') as out:
				out.write('%s\n' % resource) # if there's an error, save the resource location in this file ....
				out.close()


# class = "_8mlbc _vbtk2 _t5r8b"
# this is the class
# <a> with href = reference to picture


# from that page, we can extract the resource and download it :
# if there is a <meta> tag with property="og:video" then the resource is a video, .mp4
# if not, there is a <meta> tag with property = "og:image" and the resource is an image, .jpg 

# next page : <a class="_oidfu", href = next page 