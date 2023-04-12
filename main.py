

import requester

def print_dict(dicti: dict):
    for x, y in dicti.items():
        print(x, y)



def main():

    api = requester.Requester()

    trending_tv = api.get_trending("movie", "week")
    print(trending_tv)
    print_dict(trending_tv)


if __name__ == '__main__':
    main()