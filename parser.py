from html.parser import HTMLParser

class Ig (HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
        	# [ ('class','_8mlbc _vbtk2 _t5r8b') ]   ---- this is a post
        	# [ ('class','_pupj3') ] ---- this is the "next page" button 


    def handle_endtag(self, tag):
        #print("Encountered an end tag :", tag)
        pass

    def handle_data(self, data):
    	pass
