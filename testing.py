import requests

def main():

    api_key = open('api_key.txt', 'r').read()
    media_type = "tv"
    time_window = "week"

    trending = requests.get(f"https://api.themoviedb.org/3/trending/{media_type}/{time_window}?api_key={api_key}").json()
    print(trending)
    shows = trending['results']

    for show in shows:
        print(show['name'])





if __name__ == '__main__':
    main()