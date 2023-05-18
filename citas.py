import json
import os

import requests
#from django.http import HttpResponse



payload = {'method': 'getQuote', 'format': 'json', 'lang': 'en'}
r = requests.get('http://api.forismatic.com/api/1.0/', params=payload)
data = json.loads(r.text)

print(data['quoteText'])