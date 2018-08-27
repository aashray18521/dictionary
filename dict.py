# Python 3 Dictionary
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
word = "<your-word-here>"
url = "https://www.vocabulary.com/dictionary/" + word
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(req).read()
soup = BeautifulSoup(page,'html.parser')
possible_ans = soup.findAll("p", {"class": "short"})
ans = str(possible_ans[0])
ans1 = ans.replace("<p class=\"short\">", "")
ans2 = ans1.replace("</i></p>","")
ans2 = ans2.replace("</p>", "")
ans3 = ans2.replace("</i>","")
ans4 = ans3.replace("<i>","")
ans4 = ans4.split('.')
print(ans4[0]+'.')
