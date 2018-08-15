import sys
from bs4 import BeautifulSoup

with open(sys.argv[1]) as markup:
    soup = BeautifulSoup(markup.read())

with open("example.txt", "w") as f: 
    f.write(soup.get_text())
