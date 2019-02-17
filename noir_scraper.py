import requests
from bs4 import BeautifulSoup
import ccsv

# Feature Film/TV Movie,Film Noir (Sorted by Popularity
page = requests.get('https://www.imdb.com/search/title?title_type=feature,tv_movie&genres=film-noir&count=250')

soup = BeautifulSoup(page.content, 'html.parser')

containers = soup.body.find_all("div", class_="lister-item-content")
container = containers[0]

filename = "Noir.csv"
f = open(filename, "w")
headers = "movie_title, year, runtime, rating \n"

f.write(headers)

for container in containers:
    movie_title = container.a.text
    #movie_title = movie_title_container.get_text()

    runtime_container = container.find_all("span", class_= "runtime")
    runtime = runtime_container[0].get_text()

    rating_container = container.find_all("strong")
    rating = rating_container[0].text

    year_container = container.find_all("span", class_= "lister-item-year")
    year = year_container[0].text

    print("Movie Title: " + movie_title)
    print("Year: " + year)
    print("Runtime: " + runtime)
    print("Rating: " + rating)
    print("\n")

    f.write(movie_title + "," + year + "," + runtime + "," + rating + "\n")

f.close()
