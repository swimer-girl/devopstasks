from bs4 import BeautifulSoup
import requests
import json

def parse_top_250(file_to_write):
    url = "https://imdb.com/chart/top"
    headers = {"Accept-Language": "En-us"}
    results = requests.get(url, headers=headers)
    soup = BeautifulSoup(results.text, 'lxml')
    movies_list = []
    for container in soup.tbody.find_all('tr'):
        title = container.find('td', class_='titleColumn').a.text
        position = container.find('td', class_='posterColumn').span['data-value']
        year = container.find('span', class_='secondaryInfo').text.strip('()')
        dir_act = container.find('td', class_='titleColumn').a['title'].split(', ')
        rating = container.find('td', class_='ratingColumn imdbRating').strong.text
        movie = {
            title: {
            'Position': position,
            'Year': year,
            'Director': dir_act[0].strip(' (dir.)'),
            'Crew': f'{dir_act[1]}, {dir_act[2]}',
            'Rating': rating}
        }
        movies_list.append(movie)
    with open(file_to_write, 'w') as f_write:
            json.dump(movies_list, f_write, indent=4)

