
from urllib.request import urlopen
import time
import sys

# The url we want to target
my_address = "http://www.mfiles.co.uk/mp3-downloads/Toccata-and-Fugue-Dm.mp3"
#to download the mp3 we need a url that ends with .mp3. We first read the website and then write it to our local file in binary using wb
# with urlopen we open the url we want(my_address)
html_page = urlopen(my_address)
# we store the content of the website
html_text = html_page.read()
f=open("/home/raghav/Desktop/test_download.mp3","wb")
f.write(html_text)

for i in range(100):
    time.sleep(1)
    sys.stdout.write("\r%d%%" % i)
    sys.stdout.flush()
f.close()
