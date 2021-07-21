import requests
from config import *

test = requests.get(ACCOUNT_URL, headers = HEADERS)
print(test.content)
