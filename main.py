

import requester

def print_dict(dicti: dict):
    for x, y in dicti.items():
        print(x, y)



def main():

    api = requester.Requester()

    trending_tv = api.get_trending("tv", "week")
    print(trending_tv)
    print_dict(trending_tv)

    print(api.tv_genres)


if __name__ == '__main__':
    main()