from html.parser import HTMLParser

class IgParser (HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            #print(attrs)
            if ('class','_8mlbc _vbtk2 _t5r8b') in attrs:
                url = 'https://instagram.com' + dict(attrs)['href']
                #print (url)
                self.data.append(url) # appends url to data
        	# [ ('class','_8mlbc _vbtk2 _t5r8b') ]   ---- this is a post
        	# [ ('class','_oidfu') ] ---- this is the "next page" button 

    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
    	pass