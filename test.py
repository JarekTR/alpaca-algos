import requests
from config import *

r = requests.get(ACCOUNT_URL, headers=HEADERS)
print(r.content)
