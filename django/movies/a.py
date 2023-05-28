import requests

url = 'https://api.themoviedb.org/3/movie/155?api_key=d91307c8a96675eb52eded07c8c1099a'
print(requests.get(url).json())