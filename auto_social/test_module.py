from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, sys

# url = "http://olympus.realpython.org/profiles/aphrodite"
# data = urlopen(url)
# html = data.read().decode("utf-8")
# print(html+"\n")
# pattern = "<title.*?>.*?</title.*?>"
# result_match = re.search(pattern, html, re.IGNORECASE)
# print(result_match, "\n")
# find_data = result_match.group()

# print(find_data)

# rm = re.sub("<.*?>", "", find_data)

# print("removed : ", rm)


# Exercise for data scrapting 1
url = "http://olympus.realpython.org/profiles/dionysus"
link = urlopen(url)
find = link.read().decode("utf-8") + "\n"
start = find.find("<h2>") + len("<h2>")
end = find.find("</h2>") # + len("<h2>")
result = find[start:end]
print("name : ", result, "\n") # result must be "Name: Dionysus"


# Exercise for data scrapting 2
url = "http://olympus.realpython.org/profiles/dionysus"
re_link = urlopen(url)
re_html = re_link.read().decode("utf-8")
for string in ["Name: ", "Favorite Color:"]:
    str_start = re_html.find(string)
    text_end = str_start+len(string)
    start_html_tag = re_html[text_end:].find("<")
    end_text_index = text_end + start_html_tag
    marged_string = re_html[str_start:end_text_index]
    clean_text = marged_string.strip(" \r\n\t")
    print(clean_text)
    
print("\n")
    

# with beautifulsoup4
url = "http://olympus.realpython.org/profiles/dionysus"
bs_open = urlopen(url)
bs_html = bs_open.read().decode("utf-8")
bs_result = BeautifulSoup(bs_html, "html.parser")
print(dir(bs_result))

    


