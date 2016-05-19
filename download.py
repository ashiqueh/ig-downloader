from selenium import webdriver 
import time
from selenium.webdriver.chrome.options import Options 
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
html = driver.execute_script('return document.documentElement.outerHTML')
#print (type(html))
file_name = user + '.html'
with open(file_name, "wb") as out:
	out.write(html.encode('utf-8'))

driver.execute_script('''!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,
document,'script','//connect.facebook.net/en_US/fbevents.js');

fbq('init', '1425767024389221');

fbq('track', 'PageView');

''')

# class = "_8mlbc _vbtk2 _t5r8b"
# this is the class
# <a> with href = reference to picture


# from that page, we can extract the resource and download it :
# if there is a <meta> tag with property="og:video" then the resource is a video, .mp4
# if not, there is a <meta> tag with property = "og:image" and the resource is an image, .jpg 

# next page : <div class="_pupj3", href = next page 