import urllib.request
import urllib.parse

# x = urllib.request.urlopen('https://www.google.com')  # sends a get request to the url and returns the source code
# print(x)

'''
Variables in link
the first variable will have a ? in front of it and the subsequent variables will have an & in front of them
'''

# if we want to search in google for eg, we don't need to hard code the link every time
# we can encode the link using urllib.parse.encode
# eg

'''url = 'http://pythonprogramming.net'
values = {'s': 'basic', 'submit': 'search'}  # s and submit are the varialbes
data = urllib.parse.urlencode(values)  # the data is now encoded automatically.

data = data.encode('utf-8')  # type of encoding
req = urllib.request.Request(url, data)  # sending the request to the site in the form of post..it is basically
# opening the link
resp = urllib.request.urlopen(req)  # visiting the url
resp_data = resp.read()
print(resp_data)
'''

# sometimes  website block scripts
# eg
try:
    x = urllib.request.urlopen('htpps://www.google.com/search?=test')
    print(x.read())
except Exception as e:
    print(e)

try:
    url = 'htpps://www.google.com/search?=test'
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) "
                             "Chrome/24.0.1312.27 Safari/537.17"}
    # metadata that our request sends to url
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    print(resp.read())

except Exception as e:
    print(e)
