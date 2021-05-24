from bs4 import BeautifulSoup
import requests
URL="https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
content = response.text
soup = BeautifulSoup(content, "html.parser")
# movie = soup.find(name="h1", class_="jsx-4245974604")
# print(movie)
all_movies = soup.find_all(name="h3", class_="jsx-4245974604")
# all_movies = soup.select(selector="h3.jsx-4245974604")
print(all_movies)
