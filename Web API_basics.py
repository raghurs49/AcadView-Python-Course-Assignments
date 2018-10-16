>>> import requests
>>> response=requests.get(" https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?")
>>> print(response.content)
b'?({"quoteText":"Fears are nothing more than a state of mind.  ", "quoteAuthor":"Napoleon Hill ", "senderName":"", "senderLink":"", "quoteLink":"http://forismatic.com/en/aaa95522fa/"})'
