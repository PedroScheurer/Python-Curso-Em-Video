from urllib.error import URLError
from urllib import request
try:
    request.urlopen("https://www.pudim.com.br/")
except URLError:
    print("Não foi possível acessar")
else:
    print("Consegui acessar")