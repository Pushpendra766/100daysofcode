from bs4 import BeautifulSoup
import requests
response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:

    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)

scores = soup.find_all(name="span", class_="score")

article_upvotes = [score_tag.getText()  for score_tag in scores]
article_upvotes = [article.split()[0] for article in article_upvotes]
article_upvotes = [int(article) for article in article_upvotes]

max_upvote = max(article_upvotes)
largest_index = article_upvotes.index(max_upvote)
print(article_texts[largest_index])
print(article_links[largest_index])




# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)


# all_tag = soup.find_all(name="a")
# for tag in all_tag:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# middle_heading = soup.find(name="h3", class_="heading")
# print(middle_heading)

# company_link = soup.select(selector="p a")
# print(company_link)

# name = soup.select_one(selector="#name") #selector is first attribute so we can leave it. as we have done down in next fragment
# print(name)
#
# headings = soup.select(".heading")
# print(headings)