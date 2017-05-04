
#!/usr/bin/python3

#asdfd
import urllib.request
from bs4 import BeautifulSoup

symbols=['GOOG','FB','AAPL']
#this will scrap data for google, facebook , apple


for i in symbols:
    print("For " + i)
    url="https://finance.yahoo.com/quote/" + i +"?p="+i


    # browser identifies itself by user agent. Needed because some websites block off programs
    header={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

    req=urllib.request.Request(url,headers=header)  #http works on requests....We are mirroring this by creating a Request object

    #sending the request
    response= urllib.request.urlopen(req)

    html=response.read() #reading the html that the browser will normally read

    #passing the html to BeautifulSoup for parsing

    soup= BeautifulSoup(html, 'html.parser') # second argument tells which parser to user

    # now we want to inspect the html page for the data that we need to scrape and find the tags between which the data is located. and the class of that tags
    # in this we find that  the data is in <td> tags

    tag=soup.find_all( "td",{'class':'Ta(end) Fw(b)'})  # finding all the td tags that have the class mentioned
    print(tag)

    #extracting the actual data
    values=[]
    for tv in tag:
        values.append(tv.get_text())   # gets the text of each of the elements of the array

    for value in values:
        print(value)

    print('\n\n')

